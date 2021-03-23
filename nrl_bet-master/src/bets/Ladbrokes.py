import requests
from bs4 import BeautifulSoup
import pandas as pd

from .SeleniumDriver import SeleniumDriver

ALL_EVENTS = "https://www.ladbrokes.com.au/sports/rugby-league/"
EVENT = "https://www.ladbrokes.com.au/api/1/sport/getMarketsByEventId"

MARKETS = {
    'FTS': 4,
    'FTS 2H': 15,
    'FTS Team 1': 16,
    'FTS Team 2': 17,
    'LTS Team 1': None,
    'LTS Team 2': None,
    'LTS': 26,
    'ATS': 1,
    '2+': 32,
}


class Ladbrokes(SeleniumDriver):

    def __init__(self):
        super().__init__()
        self._event_urls = []
        self._page_source = None

    def __get_events(self):
        """ Retrieves all the event ids that represent upcoming matches.

        Returns:
            A list containing event urls

        """
        r = requests.get(ALL_EVENTS)
        soup = BeautifulSoup(r.text, 'html.parser')
        current_round = soup.find('div', {'class': 'round'})
        all_events = ["https://www.ladbrokes.com.au" + i['href'] for i in current_round.find_all('a') if '#bet' not in i['href']]
        for i, v in enumerate(all_events):
            if i % 2 == 0:
                self._event_urls.append(v)

    def download_url(self, url):
        self._driver.get(url)
        self._page_source = self._driver.page_source

    def markets(self, market):
        """ Retrieves all first try scorer odds for a game.

        Returns:
            A dictionary where player is mapped to odds. ie. dict["David Fusitu'a"] = 9.0
        """
        self.__get_events()
        seasons = {}
        for url in self._event_urls:

            game = ' '.join([i.title() if i != 'vs' else 'v' for i in url.split('/')[-2].split('-')[1:]])

            if market in ('LTS Team 1', 'LTS Team 2'):
                seasons[game] = (pd.DataFrame({}.items(), columns=['Player', 'Ladbrokes']))
                continue

            self.download_url(url)
            soup = BeautifulSoup(self._page_source, 'html.parser')
            all_markets = soup.select('div.fullbox > div.additional-market')

            if len(all_markets) < 70:
                seasons[game] = (pd.DataFrame({}.items(), columns=['Player', 'Ladbrokes']))
                continue

            try:
                odds_table = all_markets[MARKETS[market]]
                rows = odds_table.find_all('tr')[1:]

                player_odds = {}
                for r in rows:
                    player_odds[r['data-teamname'].split(' (')[0]] = float(r['data-winoddsboost'])
                seasons[game] = pd.DataFrame(player_odds.items(), columns=['Player', 'Ladbrokes'])
            except:
                seasons[game] = pd.DataFrame({}.items(), columns=['Player', 'Ladbrokes'])
        return seasons


if __name__ == "__main__":
    l = Ladbrokes()
    odds = l.markets('FTS')
    l.cleanup()
    print(odds)

