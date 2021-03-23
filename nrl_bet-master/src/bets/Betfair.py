import pandas as pd
import requests

ALL_EVENTS = "https://www.betfair.com.au/exchange/plus/rugby-league"
MARKETS_URL = "https://www.betfair.com.au/www/sports/exchange/readonly/v1/bymarket?_ak=nzIFcwyWhrlwYMrh&alt=json&currencyCode=AUD&locale=en&marketIds={}&rollupLimit=25&rollupModel=STAKE&types=MARKET_STATE,MARKET_RATES,MARKET_DESCRIPTION,EVENT,RUNNER_DESCRIPTION,RUNNER_STATE,RUNNER_EXCHANGE_PRICES_BEST,RUNNER_METADATA,MARKET_LICENCE,MARKET_LINE_RANGE_INFO"
MARKETS = {
    'FTS': 3,
    'ATS': 5,
}


class Betfair:
    def __init__(self):
        pass

    def get_event_ids(self):
        payload = {"filter":
                        {
                            "marketBettingTypes": ["ASIAN_HANDICAP_SINGLE_LINE", "ASIAN_HANDICAP_DOUBLE_LINE", "ODDS"],
                            "productTypes": ["EXCHANGE"],
                            "marketTypeCodes": ["MATCH_ODDS", "MATCH_ODDS_UNMANAGED", "MONEYLINE", "MONEY_LINE"],
                            "selectBy": "FIRST_TO_START_AZ",
                            "contentGroup": {"language": "en", "regionCode": "NZAUS"},
                            "maxResults": 0,
                            "competitionIds": [10564377]
                        },
                    "facets": [
                        {
                            "type": "EVENT_TYPE",
                            "skipValues": 0,
                            "maxValues": 10,
                            "next": {
                                "type": "EVENT", "skipValues": 0, "maxValues": 50,
                                "next": {"type": "MARKET", "maxValues": 1}
                            }
                        }
                    ],
            "currencyCode": "AUD",
            "locale": "en"
        }
        r = requests.post('https://www.betfair.com.au/www/sports/navigation/facet/v1/search?_ak=nzIFcwyWhrlwYMrh&alt=json', json=payload)
        event_ids = sorted(r.json()['attachments']['events'].keys())
        return event_ids

    def get_market_ids(self, mkt, event):
        payload = {
            "filter":
                {"marketBettingTypes": ["ASIAN_HANDICAP_SINGLE_LINE", "ASIAN_HANDICAP_DOUBLE_LINE", "ODDS"] ,
                 "eventTypeIds": [1477],
                 "productTypes": ["EXCHANGE"],
                 "selectBy": "RANK",
                 "contentGroup": {"language":"en","regionCode":"NZAUS"},
                 "maxResults": 0,
                 "attachments": ["MARKET_LITE"],
                 "eventIds": [int(event)]},
                 "facets": [
                     {"type": "EVENT", "maxValues": 0, "skipValues": 0, "applyNextTo": 0,
                      "next":
                         {"type": "MARKET", "maxValues": 0, "skipValues": 0,"applyNextTo": 0}
                      }
                 ],
                "currencyCode": "AUD", "locale": "en"}

        r = requests.post('https://www.betfair.com.au/www/sports/navigation/facet/v1/search?_ak=nzIFcwyWhrlwYMrh&alt=json', json=payload)
        game = next(iter(r.json()['attachments']['events'].values()))['name']
        try:
            # TODO: missing a whole bunch of other markets
            market_id = r.json()['facets'][0]['values'][0]['next']['values'][MARKETS[mkt]]['key']['marketId']
        except KeyError:
            return game, {'raise error'}
        return game, market_id

    def markets(self, mkt):
        round = {}
        for event in self.get_event_ids():
            try:
                game, market_ids = self.get_market_ids(mkt, event)
                r = requests.get(MARKETS_URL.format(market_ids))
                data = r.json()
                player_odds = {}
                market_odds = data['eventTypes'][0]['eventNodes'][0]['marketNodes'][0]['runners']

                if len(market_odds) < 6:
                    raise IndexError

                for i in market_odds:
                    player_name = ' '.join(i['description']['runnerName'].split(' ')[:2])
                    try:
                        odds = i['exchange']['availableToBack'][0]['price']
                    except KeyError:
                        odds = ''
                    player_odds[player_name] = odds
                round[game] = (pd.DataFrame(player_odds.items(), columns=['Player', 'Betfair']))
            except Exception as e:
                if e is 'eventTypes':
                    print("Betfair does not have market {}".format(mkt))
                else:
                    print("Betfair: {}".format(e))
                round[game] = (pd.DataFrame({}.items(), columns=['Player', 'Betfair']))
        return round


if __name__ == "__main__":
    b = Betfair()
    odds = b.markets('FTS 2H')
    print(odds)
