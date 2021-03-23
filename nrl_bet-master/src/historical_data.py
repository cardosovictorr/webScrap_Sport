from bs4 import BeautifulSoup
import requests
import json
from typing import List
import os
from sheets import GoogleSheets
from collections import defaultdict

MATCH_CSV = os.path.join(os.path.dirname(os.path.abspath(__name__)), 'src', 'match.csv')
YEARS = [2015, 2016, 2017, 2018, 2019]
LEAGUE = {'Telstra': 111}
SEASON_URL = 'https://www.nrl.com/draw/data?competition={}&season={}&round={}'


def match_urls(league):
    match_urls = []
    for year in YEARS:
        for round in range(1, 31):  # rounds 1-30
            r = requests.get(SEASON_URL.format(LEAGUE[league], year, round))
            s = SEASON_URL.format(LEAGUE[league], year, round)
            data = r.json()
            for day in data['drawGroups']:
                if 'byes' not in day:
                    for match in day['matches']:
                        match_urls.append(''.join(['https://www.nrl.com/', match['matchCentreUrl']]))
    return match_urls


def download_match_statistics(urls: List[str]):
    """ Downloads Match statistics from the official NRL website and stores information into a database.

    Args:
        urls (List of Strings): direct urls to match information

    Returns:
        df (Pandas DataFrame) containing all relevant information of matches in the round

    """
    round_data = []
    for url in urls:
        r = requests.get(url)

        # Select relevant information from HTML
        soup = BeautifulSoup(r.text, 'html.parser')
        game_info = soup.find('div', {'id': 'vue-match-centre'})['q-data']
        game_json = json.loads(game_info)

        if 'homeTeam' not in game_json['match'] or 'score' not in game_json['match']['homeTeam']:
            continue

        # General Match Info
        round_number = game_json['match']['roundNumber']
        start_time = game_json['match']['startTime']

        home_team = game_json['match']['homeTeam']['name']
        home_score = game_json['match']['homeTeam']['score']

        away_team = game_json['match']['awayTeam']['name']
        away_score = game_json['match']['awayTeam']['score']

        try:
            home_scoring = game_json['match']['homeTeam']['scoring']
        except KeyError:
            home_scoring = {}

        try:
            away_scoring = game_json['match']['awayTeam']['scoring']
        except KeyError:
            away_scoring = {}

        match_data = {
            'round_number': round_number,
            'start_time': start_time,
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            'home_scoring': home_scoring,
            'away_scoring': away_scoring
        }

        round_data.append(match_data)
    return round_data


def parse_match_data(match_data):
    total_number_of_rounds = 30
    seasons = [
        {'year': '2015',
         'rounds': [[] for _ in range(total_number_of_rounds)]
         },
        {'year': '2016',
         'rounds': [[] for _ in range(total_number_of_rounds)]
         },
        {'year': '2017',
         'rounds': [[] for _ in range(total_number_of_rounds)]
         },
        {'year': '2018',
         'rounds': [[] for _ in range(total_number_of_rounds)]
         },
        {'year': '2019',
         'rounds': [[] for _ in range(total_number_of_rounds)]
         },
    ]

    for match in match_data:
        match_year = match['start_time'].split('-')[0]
        season = [i for i in seasons if i['year'] == match_year][0]

        fts_team_1 = lts_team_1 = fts_team_1_time = lts_team_1_time = fts_team_2 = lts_team_2 = fts_team_2_time = lts_team_2_time = ''

        try:
            home_scoring = match['home_scoring']['tries']['summaries']
        except:
            home_scoring = []

        try:
            away_scoring = match['away_scoring']['tries']['summaries']
        except:
            away_scoring = []

        home_scorers = [(' '.join(i.split(' ')[:2]), int(i.split(' ')[-1].split('\'')[0])) for i in home_scoring]
        away_scorers = [(' '.join(i.split(' ')[:2]), int(i.split(' ')[-1].split('\'')[0])) for i in away_scoring]
        fts_team_1 = home_scorers[0] if home_scorers else []
        fts_team_2 = away_scorers[0] if away_scorers else []
        lts_team_1 = home_scorers[-1] if home_scorers else []
        lts_team_2 = away_scorers[-1] if away_scorers else []

        try:
            fts = fts_team_1[0] if fts_team_1[1] < fts_team_2[1] else fts_team_2[0]
        except:
            if not fts_team_1 or not fts_team_2:
                fts = ''
            else:
                fts = fts_team_1[0] if fts_team_1 else fts_team_2[0]

        try:
            lts = lts_team_1[0] if lts_team_1[1] > lts_team_2[1] else lts_team_2[0]
        except:
            if not lts_team_1 or not lts_team_2:
                lts = ''
            else:
                lts = lts_team_1[0] if lts_team_1 else lts_team_2[0]

        try:
            all_home_try_scorers = [' '.join(player.split(' ')[:2]) for player in home_scoring]
        except:
            all_home_try_scorers = []

        try:
            all_away_try_scorers = [' '.join(player.split(' ')[:2]) for player in away_scoring]
        except:
            all_away_try_scorers = []

        try:
            all_scorers = list(set(all_home_try_scorers + all_away_try_scorers))
            ats = ', '.join(all_scorers)
        except:
            ats = []

        scorers_2h_team_1 = [home_player for home_player in home_scorers if home_player[1] > 40]
        scorers_2h_team_2 = [away_player for away_player in away_scorers if away_player[1] > 40]
        try:
            fts_2h = scorers_2h_team_1[0][0] if scorers_2h_team_1[0][1] < scorers_2h_team_2[0][1] else scorers_2h_team_2[0][0]
        except:
            if not scorers_2h_team_1 and not scorers_2h_team_2:
                fts_2h = ''
            else:
                fts_2h = scorers_2h_team_1[0][0] if scorers_2h_team_1 else scorers_2h_team_2[0][0]

        total_tries_scored_by_each_player = defaultdict(int)
        for player in (all_home_try_scorers + all_away_try_scorers):
            total_tries_scored_by_each_player[player] += 1

        more_than_two_scored = [i for i in total_tries_scored_by_each_player.keys() if total_tries_scored_by_each_player[i] > 1]
        more_than_two_scored = ', '.join(more_than_two_scored) if more_than_two_scored else ''

        game = {
            'Name': ' v '.join([match['home_team'], match['away_team']]),
            'FTS': fts,
            'FTS Team 1': fts_team_1[0] if fts_team_1 else '',
            'FTS Team 2': fts_team_2[0] if fts_team_2 else '',
            'FTS 2H': fts_2h,
            'LTS': lts,
            'LTS Team 1': lts_team_1[0] if lts_team_1 else '',
            'LTS Team 2': lts_team_2[0] if lts_team_2 else '',
            'ATS': ats,
            '2+': more_than_two_scored
        }
        season['rounds'][match['round_number'] - 1].append(game)
    return seasons


def write_historic(season):
    gs = GoogleSheets()
    gs.clear_sheet('HIST', season['year'])
    for i, round in enumerate(season['rounds']):
        if i == 0:
            gs.write_historical(round, i + 1, 'HIST', season['year'], first_row=True)
        else:
            gs.write_historical(round, i + 1, 'HIST', season['year'])


if __name__ == "__main__":
    urls = match_urls('Telstra')
    matches = download_match_statistics(urls)
    seasons = parse_match_data(matches)
    for s in seasons:
        write_historic(s)
