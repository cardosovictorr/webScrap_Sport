from selenium import webdriver

# Chrome driver resources at https://chromedriver.chromium.org/downloads

chrome_driver_path = r'C:/Users/victo/workspace/WebScrapping_Bets/resources/chromedriver.exe'

#url = 'https://www.sportsbet.com.au/betting/rugby-league/nrl'
#url = 'https://www.sportsbet.com.au/betting/rugby-league/nrl/St-George-Illawarra-Dragons-v-Cronulla-Sharks-5524780'
#url = 'https://www.tab.com.au/sports/betting/Rugby%20League/competitions/NRL/matches/St%20George%20Ill%20v%20Cronulla?betOption=undefined'
# tab
url_tab = 'https://www.tab.com.au/sports/betting/Rugby%20League/competitions/NRL/matches/Parramatta%20v%20Melbourne?betOption=undefined'

#driver = webdriver.Chrome(chrome_driver_path)

# the code below is to stop an web browser error to be showing in my terminal.
opt = webdriver.ChromeOptions()
opt.add_argument("--log-level=3")
driver = webdriver.Chrome(chrome_driver_path, options=opt)

# driver.get(url)
driver.get(url_tab)

first_try_scorer_tab = driver.find_elements_by_class_name('_uzx34z ')
#hth_elements = driver.find_elements_by_class_name('participantRow_fklqmim')
#line_tab = driver.find_elements_by_class_name('animate-odd')

#print(hth_elements[0].text + "TESTE")
#
# print(len(hth_elements))

print(len(first_try_scorer_tab))
print(first_try_scorer_tab[0].text)
print(first_try_scorer_tab[1].text)
print(first_try_scorer_tab[2].text)
print(first_try_scorer_tab[3].text)
print(first_try_scorer_tab[4].text)


# print(line_tab[0].text)
# print(len(line_tab))

input("Press enter to close the program")

#fisrt_try_scorer = driver.find_elements_by_class_name('priceText_f71sibe')

#first_try_scorer_tab = driver.find_elements_by_class_name('_po9vpe')

# driver.close()
