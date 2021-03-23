import requests
import pandas as pd

ALL_EVENTS = "https://o1-api.aws.kambicdn.com/offering/v2018/ubau/listView/rugby_league.json?lang=en_AU&market=AU&client_id=2&channel_id=1&ncid=1561788726241&useCombined=true"
EVENT = "https://o1-api.aws.kambicdn.com/offering/v2018/ubau/betoffer/event/{}.json?lang=en_AU&market=AU"
MARKETS = {
    'FTS': 'First',
    'FTS 2H': None,
    'FTS Team 1': 'First Try Scorer - Home Team. Including Overtime',
    'FTS Team 2': 'First Try Scorer - Away Team. Including Overtime',
    'LTS Team 1': 'Last Try Scorer - Home Team. Including Overtime',
    'LTS Team 2': 'Last Try Scorer - Away Team. Including Overtime',
    'LTS': 'Last',
    'ATS': 'Yes',
    '2+': 'To score 2 or more tries - Including Overtime',
}


class Unibet:

    def __init__(self):
        pass

    def __get_event_ids(self):
        """ Retrieves all the most recent event ids from the NRL home page.

        """
        r = requests.get(ALL_EVENTS)
        data = r.json()
        events = {}
        for event in data['events']:
            if event['event']['group'] == 'NRL':
                events[event['event']['name'].replace('-', 'v')] = event['event']['id']
        return events

    @staticmethod
    def __parse_data(item, player_label):
        if 'unlisted' in item[player_label]:
            player_name = "Unlisted"
        elif 'Drop Goal' in item[player_label]:
            player_name = item[player_label]
        else:
            split_name = item[player_label].split(', ')
            player_name = ' '.join([split_name[1], split_name[0]])

        odds = item['odds'] / 1000
        return player_name, odds

    def markets(self, market):
        round = {}
        for game, event in self.__get_event_ids().items():
            r = requests.get(EVENT.format(event))
            data = r.json()

            try:
                market_data = None
                if market in ('FTS', 'LTS', 'ATS'):
                    market_data = [item for item in data['betOffers'] if item['betOfferType']['name'] == "Scorer"]
                    if market_data:
                        market_data[0]['outcomes'] = [i for i in market_data[0]['outcomes'] if i['criterion']['name'] == MARKETS[market]]
                elif market in ('FTS Team 1', 'FTS Team 2', 'LTS Team 1', 'LTS Team 2'):
                    market_data = [item for item in data['betOffers'] if item['criterion']['label'] == MARKETS[market]]
                elif market in '2+':
                    market_data = [item for item in data['betOffers'] if item['criterion']['label'] == MARKETS[market]]

                player_odds = {}
                if market_data:
                    if market in '2+':
                        for i in market_data:
                            player = i['outcomes'][0]
                            player_name, odds = self.__parse_data(player, 'participant')
                            player_odds[player_name] = odds
                    else:
                        if isinstance(market_data, list):
                            market_data = market_data[0]
                        for item in market_data['outcomes']:
                            player_name, odds = self.__parse_data(item, 'englishLabel')
                            player_odds[player_name] = odds
                round[game] = (pd.DataFrame(player_odds.items(), columns=['Player', 'Unibet']))
            except Exception as e:
                print("Unibet: {}".format(e))
                round[game] = (pd.DataFrame({}.items(), columns=['Player', 'Unibet']))
        return round


if __name__ == "__main__":
    u = Unibet()
    odds = u.markets('FTS Team 1')
    print(odds)
