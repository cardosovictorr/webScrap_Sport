import gspread
import gspread_dataframe as gd
from gspread_formatting import *
from oauth2client.service_account import ServiceAccountCredentials
import time

MARKETS = ['FTS', 'FTS 2H', 'FTS Team 1', 'FTS Team 2', 'LTS Team 1', 'LTS Team 2', 'LTS', 'ATS', '2+']
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
SHEET = {
    'FTS': '1EJc4RLUqZrjGnpVu9-6Wt8Lq-wmKu4tIJzkrzJ_tZX0',
    'FTS 2H': '1qZNlp0rTK0wgtaceLUU5IZBMTKnBEzFbc-wZttJs4yo',
    'FTS Team 1': '1kbBU_8Fa1hxbhWKFvJZdXaM-mu4onOapU-uyqirAiss',
    'FTS Team 2': '1yo0KHyY-WWd85wi5CyT33F8jp0CbY2zpY0EFREsJT0c',
    'LTS Team 1': '1n3EjM3_ypGSH0LwlXWa3D1m0psfPkOdPfEDcVvn2Zzc',
    'LTS Team 2': '1lYtQQu9jgDNkPgSTr66x6njn1Xot_6AdyuK3bwkJSoY',
    'LTS': '1vg1RYFoaowFehg_VNNUdISZApKkE37zSxwvG447bwr4',
    'ATS': '1V0_qyXhJlC--sCzFeiTWvFpjS-Q_eT3os-VWf-OX5wc',
    '2+': '1EsguFs23gfrqa3gDplLnkrz3AX8xsHM84YGpBwLxnck',
    'HIST': '1cVKArlNRuoKWwxtJLLiht6TD9rIgh8iBnhf9yZWDj_0'
}

COLUMN_COORD = {0: 'B', 1: 'C', 2: 'D', 3: 'E', 4: 'F', 5: 'G'}

CELL_COLOURS = {
    'red': {
        'background': Color(1, 0.9, 0.9),
        'foreground': Color(1, 0, 0)
    },
    'green': {
        'background': Color(0.85, 0.92, 0.83),
        'foreground': Color(0.4, 0.82, 0.60)
    },
    'blue': {
        'background': Color(0.78, 0.85, 0.97),
        'foreground': Color(0.25, 0.65, 1)
    },
    'white': {
        'background': Color(1, 1, 1),
        'foreground': Color(0, 0, 0)
    }
}


class GoogleSheets:
    def __init__(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
        self._gc = gspread.authorize(credentials)

    def write(self, df, sh_name, sh):
        sht = self._gc.open_by_key(SHEET[sh])
        worksheet = sht.add_worksheet(title=sh_name, rows="100", cols="20")
        gd.set_with_dataframe(worksheet, df)

    def update(self, df, sh, sh_name,):
        sht = self._gc.open_by_key(SHEET[sh])
        if sh_name in [i.title for i in sht.worksheets()]:
            worksheet = sht.worksheet(sh_name)
            self.clear_sheet(sh, sh_name)
        else:
            worksheet = sht.add_worksheet(title=sh_name, rows="100", cols="20")
        gd.set_with_dataframe(worksheet, df)

    def write_historical(self, round, round_number, sh, worksheet_name, first_row=False):
        """ Only for historical data
        :param row_list: dataframe
        :param sh: sheet key
        :param worksheet_name: name of worksheet to edit
        """
        sheet = self._gc.open_by_key(SHEET[sh])
        worksheet = sheet.worksheet(worksheet_name)

        next_row = self.next_available_row(worksheet) if first_row else self.next_filled_row(worksheet)
        next_row_index = next_row if first_row else next_row + 1

        headers = ['Round {} {}'.format(round_number, worksheet_name)]
        for i in range(1, 9):
            headers.append('Game {}'.format(i))

        worksheet.insert_row(headers, index=next_row_index)
        self.__highlight_cell(worksheet, 'white', "A{}:J{}".format(next_row_index, next_row_index), bold=True)
        self.__highlight_cell(worksheet, 'white', "A1:A100", bold=True)

        for market in MARKETS:
            odds = [market]
            for match in round:
                odds.append(match[market])
            next_row_index += 1
            worksheet.insert_row(odds, index=next_row_index)
            time.sleep(1.5)

    def clear_sheet(self, sh, ws):
        sheet = self._gc.open_by_key(SHEET[sh])
        if ws in [i.title for i in sheet.worksheets()]:
            worksheet = sheet.worksheet(ws)
            final_row = self.next_available_row(worksheet)
            for alpha in ['B', 'C', 'D', 'E', 'F', 'G']:
                self.__highlight_cell(worksheet, 'white', "{}2:{}{}".format(alpha, alpha, final_row), bold=False)
            worksheet.clear()

    def reset_all_sheets(self):
        for i in MARKETS:
            self.reset_sheet(i)

    def reset_sheet(self, sh):
        sht = self._gc.open_by_key(SHEET[sh])
        try:
            sht.add_worksheet(title="Sheet1", rows="100", cols="20")
        except:
            sht.add_worksheet(title="Sheet10", rows="100", cols="20")
        for i in sht.worksheets()[:-1]:
            sht.del_worksheet(i)

    def delete_placeholder_sheet(self, mkt):
        sht = self._gc.open_by_key(SHEET[mkt])
        if 'Sheet1' in sht.worksheets()[0].title or 'Sheet10' in sht.worksheets()[0].title:
            sht.del_worksheet(sht.worksheets()[0])

    def next_filled_row(self, sheet):
        str_list = list(filter(lambda x: x is not None, sheet.col_values(1)))
        return len(str_list) + 1

    def next_available_row(self, sht):
        str_list = list(filter(None, sht.col_values(1)))
        return len(str_list) + 1

    def __highlight_cell(self, sheet, colour, coordinate, bold=True):
        fmt = CellFormat(
            backgroundColor=CELL_COLOURS[colour]['background'],
            textFormat=TextFormat(bold=bold, foregroundColor=CELL_COLOURS[colour]['foreground']),
        )
        format_cell_range(sheet, coordinate, fmt)

    def refresh_authentication(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
        self._gc = gspread.authorize(credentials)

    def highlight_markets(self):
        for market in MARKETS:
            sheet = self._gc.open_by_key(SHEET[market])
            for ws in sheet.worksheets():
                self.highlight_cells(market, ws)

    def highlight_cells(self, mkt, game):
        sheet = self._gc.open_by_key(SHEET[mkt])
        worksheet = sheet.worksheet(game)
        for row_number in range(2, self.next_available_row(worksheet)):
            row_vals = [float(i) if i.strip() else 0 for i in worksheet.row_values(row_number)[1:]]
            if row_vals:
                max_val = max(row_vals)
                next_max_val = max(row_vals, key=lambda x: x if x != max_val else float('-inf'))
                for idx, val in enumerate(row_vals):
                    if val == 0:
                        continue
                    elif val == max_val and next_max_val != 0 and (max_val - next_max_val) / max_val >= 0.4:
                        colour = 'red'
                    elif val == max_val and next_max_val != 0 and (max_val - next_max_val) / max_val >= 0.2:
                        colour = 'green'
                    elif val == max_val:
                        colour = 'white'
                    else:
                        continue
                    self.__highlight_cell(worksheet, colour, COLUMN_COORD[idx] + str(row_number))
                    time.sleep(1.1)
            else:
                continue
        self.refresh_authentication()
