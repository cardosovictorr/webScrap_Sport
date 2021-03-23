from sheets import GoogleSheets
from collections import defaultdict
import pandas as pd
from functools import reduce
import re

from bets.BetEasy import BetEasy
from bets.SportsBet import SportsBet
from bets.Betfair import Betfair
from bets.Unibet import Unibet
from bets.Ubet import Ubet
from bets.Ladbrokes import Ladbrokes

MARKETS = ['FTS', 'FTS 2H', 'FTS Team 1', 'FTS Team 2', 'LTS Team 1', 'LTS Team 2', 'LTS', 'ATS', '2+']
BOOKMAKERS = {
    'BetEasy': BetEasy(),
    'Sportsbet': SportsBet(),
    'Unibet': Unibet(),
    'UBET': Ubet(),
    # 'Ladbrokes': Ladbrokes(),
    # 'Betfair': Betfair()
}


def normalise_dataframe(dataframe):
    """ Normalises player names in dataframe
    Args:
        dataframe (Pandas DataFrame): contains player name and odds
    Returns:
        Normalised DataFrame

    """
    # key (regex): val(string note. not regex)
    name_replacement = {
        r'\bZac\b': 'Zachary',
        r'^Tim Lafai$': 'Timoteo Lafai',
        r'^(?:Tryscorer No|No Tryscorer|No Scorer|.* Try Scored|No Try|No Tryscorerscorer)$': 'No Try Scorer',
        r'(?<=\s)(?:Uele|Hamlin)$': 'Hamlin-Uele',
        r'Charnze\(Can\)': 'Charnze',
        r'\b(?:Matt|Matthewhew)\b': 'Matthew',
        r'Havilli': 'Havili',
        r'(?:Mau Ah|Leeson Ah)$': 'Leeson Ah Mau',
        r'Jake\(NQl\)': 'Jake',
        r'Matautia': 'Mata\'utia',
        r'Eseese': 'Ese\'ese',
        r'Too': 'To\'o',
        r'Cam': 'Cameron',
        r'Campbell-Gill': 'Campbell-Gillard',
        r'(?:Sua|SuA)': 'Su\'a',
        r'Pangai$': 'Pangai Junior',
        r'OSullivan': 'O\'Sullivan',
        r'Patty': 'Patrick',
        r'(?:Sio Siua|Sio|Siosiuasiua)$': 'Siosiua',
        r'Hutchinson': 'Hutchison',
        r'(?:Watene-Zelez|Watene)$': 'Watene-Zelezniak',
        r'Ray': 'Raymond',
        r'^(?:Joe|Jo)\s': 'Joseph',
        r'AJ': 'Alex',
        r'Fusitua': 'Fusitu\'a',
        r'Kenny': 'Kenneath',
        r'Mitch': 'Mitchell',
        r'Cameroneron': 'Cameron',
        r'^Josh Addo$': 'Josh Addo-Carr',
        r'^Nelson Asofa$': 'Nelson Asofa-Solomona',
        r'Alex': 'Alexander',
        r'^Brendan Elliott$': 'Brendan Elliot',
        r'^Daly Cherry$': 'Daly Cherry-Evans',
        r'^Addin Fonua$': 'Addin Fonua-Blake',
        r'^Richie': 'Richard',
        r'Kenneath$': 'Kenneath-Dowall',
        r'^JosephOfahengaue$': 'Joseph Ofahengaue',
        r'\bClint\b': 'Clinton',
        r"(?:Papalii|Papali\\'i|Pappalii)$": "Papali'i",
        r'^James Fisher$': r'James Fisher-Harris',
        r"\bTo\'omaga\b": "To'omaga",
        r'\bWill\b': 'William',
        r'Harawira$': 'Harawira-Naera',
        r'Cameronpbell-Gill$': 'Cameronpbell-Gillard',
        r'Tuivasa$': 'Tuivasa-Sheck',
        r'^(?:J Waerea-Hargreaves|Jarred Waerea-Hargreaves|Jared Waerea)$': 'J Waerea-Hargreaves',
        r'Safiti$': 'Saifiti',

    }

    for key, value in name_replacement.items():
        dataframe['Player'] = dataframe.Player.str.replace(key, value, regex=True)
    return dataframe


def normalise_team_name(team):
    team_replacement = {
        r'^St\.': 'St',
        r'^Saint': 'St',
    }
    replaced_team = team
    for key, value in team_replacement.items():
        replaced_team = re.sub(key, value, team)
    return replaced_team


def summarise_bets(gs):
    for mkt in MARKETS:
        try:
            market = {key: value.markets(mkt) for key, value in BOOKMAKERS.items()}
            grouped_odds = defaultdict(list)
            for website_games in market.values():
                for k, v in website_games.items():
                    if len(v.index > 0):
                        grouped_odds[normalise_team_name(k)].append(normalise_dataframe(v))
            for game, website_odds in grouped_odds.items():
                df = reduce(lambda x, y: pd.merge(x, y, on='Player', how='outer'), website_odds)
                gs.update(df, mkt, game)
            gs.delete_placeholder_sheet(mkt)
        except:
            for b in ('Sportsbet',): #'Ladbrokes'):
                BOOKMAKERS[b].cleanup()
            raise

    for b in ('Sportsbet',): #'Ladbrokes'):
        BOOKMAKERS[b].cleanup()


def highlight_sheets(gs):
    gs.highlight_markets()


if __name__ == "__main__":
    gs = GoogleSheets()
    # gs.reset_all_sheets()
    summarise_bets(gs)

