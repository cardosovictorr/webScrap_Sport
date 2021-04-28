import json

# Database connection:
# DB_HOST = "localhost"
# DB_NAME = "Adv_Studio_Stock_Bot"
# DB_USER = "my_user"
# DB_PASS = "root"

# open json File

f = open('./Markets23March2021.json')

data = json.load(f)

first_tryscorer_dict = dict(data[0])
anytime_tryscorer_dict = dict(data[1])

print(type(first_tryscorer_dict))
# print(first_tryscorer_dict)

print("NAME SELECTION: ")
print(first_tryscorer_dict.get("name"))

first_tryscorer = first_tryscorer_dict.get("selections")
dictionary_values_of_first_tryscorer = dict(first_tryscorer[0])
print()


def players_function():
    player_name = ""
    player_first_tryscorer = 0
    player_dictionary = {}
    for x in range(len(first_tryscorer)):
        first_try_scorer_dict = dict(first_tryscorer[x])
        # print(first_try_scorer_dict.get("name"))
        player_name = first_try_scorer_dict.get("name")
        player_first_tryscorer = dict(first_try_scorer_dict.get("price"))
        # print(player_market_dict.get("winPrice"))
        # print()
        # print("----------------")
        # print()
        player_dictionary.update(
            {"player_name": player_name, "player_first_tryscorer": player_first_tryscorer})
        print(player_dictionary)

    return player_dictionary


f.close
