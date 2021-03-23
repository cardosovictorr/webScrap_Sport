import requests
import pandas as pd

MARKETS = {
    'FTS': 0,
    'FTS 2H': 11,
    'FTS Team 1': 3,
    'FTS Team 2': 4,
    'LTS Team 1': 13,
    'LTS Team 2': 14,
    'LTS': 12,
    'ATS': 1,
    '2+': 5,
}

# Possible to extract all this information from json

class BetEasy:

    def __init__(self):
        self._events = {}
        self._event_url = "https://beteasy.com.au/api/sports/navigation/rugby-league/nrl/nrl-matches/"
        self._match_odds = "https://beteasy.com.au/api/sports/event-group/?id={}&ecGroupOrderByIds%5B%5D=17"

    def __get_event_ids(self):
        """ Retrieves all the event ids that represent upcoming matches.

        Returns:
            A list containing event ids (strings)

        """
        r = requests.get(self._event_url)
        games = [i['name'] for i in r.json()['result']['events'] if '(Round ' not in i['name']]
        event_codes = [i['masterEventId'] for i in r.json()['result']['events']][:len(games)]
        self._events = dict(zip(games, event_codes))

    def markets(self, market):
        """ Retrieves market odds for all upcoming games.

        """
        self.__get_event_ids()
        round = {}
        for game, event in self._events.items():
            r = requests.get(self._match_odds.format(str(event)))
            try:
                first_try_odds = r.json()['result']['17']['BettingType'][MARKETS[market]]['Outcomes']
                player_odds = {}
                for player in first_try_odds:
                    player_odds[player['OutcomeName']] = float(player['BetTypes'][0]['Price'])
                round[game] = (pd.DataFrame(player_odds.items(), columns=['Player', 'BetEasy']))
            except TypeError as e:
                print("BetEasy: {}".format(e))
                round[game] = (pd.DataFrame({}.items(), columns=['Player', 'BetEasy']))
        return round


if __name__ == "__main__":
    b = BetEasy()
    odds = b.markets('FTS')
    print(odds)

