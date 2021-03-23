import requests
import pandas as pd

MEETING_IDS = "https://tab.ubet.com/api/sportsNavigation/leagueMeetings/false/10"
EVENTS_IDS = "https://tab.ubet.com/api/sports/meetingdetails/{}/false"
EVENT_DETAILS = "https://tab.ubet.com/api/sports/maineventdetails/{}/false/true"
MARKETS = {
    'FTS': 0,
    'FTS 2H': 1,
    'FTS Team 1': None,
    'FTS Team 2': None,
    'LTS': 2,
    'ATS': 3,
    '2+': 4,
}


class Ubet:

    def __init__(self):
        pass

    def __get_event_ids(self):
        """ Retrieves all the event ids that represent upcoming matches.

        Returns:
            A list containing event ids (strings)

        """
        meeting_id = requests.get(MEETING_IDS).json()[0]['meetings'][0]['meetingId']
        events_list = requests.get(EVENTS_IDS.format(meeting_id)).json()['mainEvents']
        events = {}
        for i in events_list:
            game = ' '.join(i['mainEventName'].split(' ')[:-2]) if 'LIVE' in i['mainEventName'] else ' '.join(
                i['mainEventName'].split(' ')[:-1]).replace("Bulldogs", "Canterbury Bulldogs")
            events[game] = i['mainEventId']
        return events

    def markets(self, market):
        """ Retrieves all first try scorer odds for a game.

        Returns:
            A dictionary where player is mapped to odds. ie. dict["David Fusitu'a"] = 9.0
        """
        round = {}
        for game, event_code in self.__get_event_ids().items():
            r = requests.get(EVENT_DETAILS.format(event_code))
            try:
                player_odds = {}
                if market in ('FTS Team 1', 'FTS Team 2'):
                    odds = r.json()['subEventGroups'][4]['subEvents'][MARKETS[market]]['offerGroups'][0]
                    if odds:
                        for item in odds:
                            name_split = item['offerName'].split(' ')
                            player_name = 'No Tryscorer' if 'Tryscorer' in name_split else ' '.join(
                                name_split[:2][::-1])
                            player_odds.update({player_name: item['winReturn']})
                else:
                    players = r.json()['subEventGroups'][0]['collatedSubEvents']['collatedOffers']
                    if players:
                        for p in players:
                            name_split = p['offerName'].split(' ')
                            player_name = 'No Tryscorer' if 'Tryscorer' in name_split else ' '.join(
                                name_split[:2][::-1])
                            try:
                                player_odds[player_name] = p['offers'][MARKETS[market]]['winReturn']
                            except TypeError:
                                player_odds[player_name] = 0
                round[game] = (pd.DataFrame(player_odds.items(), columns=['Player', 'UBET']))
            except:
                round[game] = (pd.DataFrame({}.items(), columns=['Player', 'UBET']))
        return round


if __name__ == "__main__":
    u = Ubet()
    odds = u.markets('FTS')
    print(odds)
