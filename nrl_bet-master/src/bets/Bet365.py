from bs4 import BeautifulSoup
import time

from .SeleniumDriver import SeleniumDriver
from selenium.common.exceptions import NoSuchElementException


class Bet365(SeleniumDriver):

    def __init__(self):
        super().__init__()
        self._event_url = "https://www.bet365.com.au/#/AC/B19/C20459137/D512/E190032/F512/"
        self._page_source = None

    def __get_events(self):
        pass

    def download_url(self):

        self._driver.get(self._event_url)
        time.sleep(5)

        try:
            self._driver.find_element_by_css_selector('a[id=TopPromotionBetNow]').click()
            time.sleep(5)
            self._driver.save_screenshot("screen.png")
            self._page_source = self._driver.page_source
        except NoSuchElementException:
            raise

    def first_try_odds(self):
        self.download_url()
        # soup = BeautifulSoup(self._page_source, 'html.parser')

        print(self._page_source)
        # first_tryscorers = soup.select('div.accordionItemDesktop_f1pa6f05')[3].select('span[data-automation-id*=column-grid-outcome-name]')
        # odds = soup.select('div.accordionItemDesktop_f1pa6f05')[3].select('span[data-automation-id*=price-text]')

        # player_odds = {}
        # for p, o in zip(first_tryscorers, odds):
        #     player_odds[p.string] = float(o.string)

        # return player_odds


if __name__ == "__main__":
    b = Bet365()
    b.first_try_odds()
