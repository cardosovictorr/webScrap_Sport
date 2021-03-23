import pandas as pd
from bs4 import BeautifulSoup
import requests

from .SeleniumDriver import SeleniumDriver

ALL_EVENTS = "https://www.sportsbet.com.au/betting/rugby-league/nrl"
MARKETS_URL = "https://www.sportsbet.com.au/apigw/sportsbook-sports/Sportsbook/Sports/Events/{}/MarketGroupings/112/Markets"

# Probs need to wait for better updates
MARKETS = {
    'FTS': 0,
    'FTS 2H': 6,
    'FTS Team 1': 11,
    'FTS Team 2': 12,
    'LTS Team 1': 13,
    'LTS Team 2': 14,
    'LTS': 15,
    'ATS': 1,
    '2+': 2,
}


class SportsBet(SeleniumDriver):

    def __init__(self):
        super().__init__()
        self._event_codes = {}
        self._page_source = None

    def __get_events(self):
        self._driver.get(ALL_EVENTS)
        soup = BeautifulSoup(self._driver.page_source, 'html.parser')
        events_info = soup.find_all('a', {'class': 'linkMultiMarket_fcmecz0'})
        games = [' '.join(word.title() if word != 'v' else word for word in i['href'].split('/')[-1].split('-')[:-1]) for i in events_info]
        event_codes = [i['href'].split('-')[-1] for i in events_info]
        self._event_codes = dict(zip(games, event_codes))

    def markets(self, market):
        self.__get_events()
        round = {}
        for game, event_code in self._event_codes.items():

            r = requests.get(MARKETS_URL.format(event_code))
            markets = r.json()

            if 'message' in markets:
                round[game] = (pd.DataFrame({}.items(), columns=['Player', 'Sportsbet']))
                continue

            player_odds = {}
            try:
                odds = markets[MARKETS[market]]['selections']
                for i in odds:
                    player_odds[i['name']] = i['price']['winPrice']
                    round[game] = (pd.DataFrame(player_odds.items(), columns=['Player', 'Sportsbet']))
            except IndexError as e:
                print("Sportsbet: {}".format(e))
                round[game] = (pd.DataFrame({}.items(), columns=['Player', 'Sportsbet']))
        return round


if __name__ == "__main__":
    s = SportsBet()
    odds = s.markets('FTS')
    print(odds)


