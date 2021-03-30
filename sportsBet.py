from selenium import webdriver

# Chrome driver resources at https://chromedriver.chromium.org/downloads

chrome_driver_path = r'C:/Users/victo/workspace/WebScrapping_Bets/resources/chromedriver.exe'

url = 'https://www.sportsbet.com.au/betting/rugby-league/nrl/penrith-panthers-v-melbourne-storm-57306320'
#url = 'https://www.sportsbet.com.au/betting/rugby-league/nrl/St-George-Illawarra-Dragons-v-Cronulla-Sharks-5524780'
#url = 'https://www.tab.com.au/sports/betting/Rugby%20League/competitions/NRL/matches/St%20George%20Ill%20v%20Cronulla?betOption=undefined'
# tab
#url_tab = 'https://www.tab.com.au/sports/betting/Rugby%20League/competitions/NRL'

#driver = webdriver.Chrome(chrome_driver_path)

# the code below is to stop an web browser error to be showing in my terminal.
opt = webdriver.ChromeOptions()
opt.add_argument("--log-level=3")
driver = webdriver.Chrome(chrome_driver_path, options=opt)

driver.get(url)
# driver.get(url_tab)

# maybe: priceButtonContainer_f18m2cag
first_try_scorer_sports_bet = driver.find_elements_by_class_name(
    'priceButtonContentSingleLine_f2o3bd8')
print(len(first_try_scorer_sports_bet[0].text))
print(first_try_scorer_sports_bet[0].text)
print(first_try_scorer_sports_bet[1].text)
print(first_try_scorer_sports_bet[2].text)
print(first_try_scorer_sports_bet[3].text)
print(first_try_scorer_sports_bet[4].text)
print(first_try_scorer_sports_bet[5].text)
print(first_try_scorer_sports_bet[6].text)
print(first_try_scorer_sports_bet[7].text)
print(first_try_scorer_sports_bet[8].text)
print(first_try_scorer_sports_bet[9].text)
print(first_try_scorer_sports_bet[10].text)


# team_name_elements = driver.find_elements_by_class_name(
#    'participantRow_fklqmim')
#line_tab = driver.find_elements_by_class_name('animate-odd')
#head_to_head_elements = driver.find_elements_by_class_name('priceText_f71sibe')

# print(team_name_elements[0].text)
# print(len(team_name_elements))


# Have to map the data and make a dictionary. So I can organize it in the right way.
# team_name_saving = ""
# for x in team_name_elements:
#    print(x.text)


# print(head_to_head_elements[0].text)
# print(head_to_head_elements[1].text)
# print(head_to_head_elements[6].text)
# print(head_to_head_elements[7].text)
# print(head_to_head_elements[12].text)
# print(head_to_head_elements[13].text)

# print('Quantity Head to Head List:')
# print(len(head_to_head_elements))

# i = 0
# while i < 48:
#     if i % 5 == 0:
#         print(head_to_head_elements[i].text)
#     i += 1


#print(line_tab[0].text + "TESTE")
# print(len(line_tab))

input("Press enter to close the program")

#fisrt_try_scorer = driver.find_elements_by_class_name('priceText_f71sibe')

#first_try_scorer_tab = driver.find_elements_by_class_name('_po9vpe')

# driver.close()
