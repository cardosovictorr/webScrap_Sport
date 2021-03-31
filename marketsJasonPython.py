import json

# MARKETS for Manly Sea Eagles V Penrith Panthers
# Date released: 30/03/2021
# SportsBet website

# Data in Json
markets_in_json = '''
[
    {
        "id": 121732833,
        "externalId": 258201266,
        "name": "First Tryscorer",
        "statusCode": "A",
        "sort": 15,
        "marketType": "-",
        "marketSort": "FS",
        "BIR": false,
        "blurb": "Quote Others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833",
        "selections": [
            {
                "id": 646195778,
                "name": "Jason Saab",
                "resultType": "H",
                "externalId": 1196498410,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195778/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195778",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195773,
                "name": "Reuben Garrick",
                "resultType": "H",
                "externalId": 1196498405,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195773/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195773",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195782,
                "name": "Dylan Walker",
                "resultType": "H",
                "externalId": 1196498414,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195782/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195782",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195776,
                "name": "Brad Parker",
                "resultType": "H",
                "externalId": 1196498408,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195776/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195776",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195780,
                "name": "Moses Suli",
                "resultType": "H",
                "externalId": 1196498412,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195780/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195780",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195769,
                "name": "Daly Cherry-Evans",
                "resultType": "H",
                "externalId": 1196498401,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195769/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195769",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195771,
                "name": "Cade Cust",
                "resultType": "H",
                "externalId": 1196498403,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195771/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195771",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195779,
                "name": "Joshua Schuster",
                "resultType": "H",
                "externalId": 1196498411,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195779/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195779",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195772,
                "name": "Kieran Foran",
                "resultType": "H",
                "externalId": 1196498404,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195772/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195772",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195774,
                "name": "Jack Gosiewski",
                "resultType": "H",
                "externalId": 1196498406,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195774/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195774",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195781,
                "name": "Jake Trbojevic",
                "resultType": "H",
                "externalId": 1196498413,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195781/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195781",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195767,
                "name": "Josh Alolai",
                "resultType": "H",
                "externalId": 1196498399,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195767/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195767",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195770,
                "name": "Lachlan Croker",
                "resultType": "H",
                "externalId": 1196498402,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195770/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195770",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195783,
                "name": "Martin Taupau",
                "resultType": "H",
                "externalId": 1196498415,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195783/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195783",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195775,
                "name": "Sean Keppie",
                "resultType": "H",
                "externalId": 1196498407,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195775/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195775",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195768,
                "name": "Morgan Boyle",
                "resultType": "H",
                "externalId": 1196498400,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195768/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195768",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195777,
                "name": "Taniela Paseka",
                "resultType": "H",
                "externalId": 1196498409,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195777/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195777",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195799,
                "name": "Brian To'o",
                "resultType": "A",
                "externalId": 1196498431,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195799/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195799",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195798,
                "name": "Charlie Staines",
                "resultType": "A",
                "externalId": 1196498430,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195798/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195798",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195787,
                "name": "Stephen Crichton",
                "resultType": "A",
                "externalId": 1196498419,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195787/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195787",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195791,
                "name": "Viliame Kikau",
                "resultType": "A",
                "externalId": 1196498423,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195791/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195791",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195797,
                "name": "Paul Momirovski",
                "resultType": "A",
                "externalId": 1196498429,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195797/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195797",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195784,
                "name": "Matt Burton",
                "resultType": "A",
                "externalId": 1196498416,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195784/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195784",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195796,
                "name": "Tyrone May",
                "resultType": "A",
                "externalId": 1196498428,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195796/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195796",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195785,
                "name": "Kurt Capewell",
                "resultType": "A",
                "externalId": 1196498417,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195785/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195785",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195795,
                "name": "Liam Martin",
                "resultType": "A",
                "externalId": 1196498427,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195795/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195795",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195786,
                "name": "Nathan Cleary",
                "resultType": "A",
                "externalId": 1196498418,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195786/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195786",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195794,
                "name": "Jarome Luai",
                "resultType": "A",
                "externalId": 1196498426,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195794/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195794",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195800,
                "name": "Isaah Yeo",
                "resultType": "A",
                "externalId": 1196498432,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195800/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195800",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195788,
                "name": "Matt Eisenhuth",
                "resultType": "A",
                "externalId": 1196498420,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195788/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195788",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195790,
                "name": "Mitch Kenny",
                "resultType": "A",
                "externalId": 1196498422,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195790/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195790",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195789,
                "name": "James Fisher-Harris",
                "resultType": "A",
                "externalId": 1196498421,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195789/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195789",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195792,
                "name": "Spencer Leniu",
                "resultType": "A",
                "externalId": 1196498424,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195792/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195792",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195793,
                "name": "Moses Leota",
                "resultType": "A",
                "externalId": 1196498425,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195793/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732833/Selections/646195793",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732882,
        "externalId": 258201272,
        "name": "Anytime Tryscorer",
        "statusCode": "A",
        "sort": 20,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote Others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882",
        "selections": [
            {
                "id": 646196368,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498524,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.4,
                    "winPriceNum": 2400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196368/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196368",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196363,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498519,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.2,
                    "winPriceNum": 2200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196363/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196363",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196366,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498522,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196366/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196366",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196372,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498528,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196372/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196372",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196359,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498515,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196359/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196359",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196370,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498526,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196370/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196370",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196361,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498517,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196361/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196361",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196369,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498525,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196369/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196369",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196364,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498520,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196364/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196364",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196362,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498518,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196362/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196362",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196357,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498513,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196357/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196357",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196360,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498516,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196360/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196360",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196371,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498527,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196371/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196371",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196373,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498529,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196373/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196373",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196365,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498521,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196365/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196365",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196358,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498514,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196358/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196358",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196367,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498523,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196367/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196367",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196389,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498545,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.57,
                    "winPriceNum": 570,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196389/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196389",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196388,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498544,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.62,
                    "winPriceNum": 620,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196388/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196388",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196374,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498530,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.75,
                    "winPriceNum": 1750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196374/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196374",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196387,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498543,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.63,
                    "winPriceNum": 1630,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196387/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196387",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196377,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498533,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.1,
                    "winPriceNum": 1100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196377/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196377",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196386,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498542,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.75,
                    "winPriceNum": 1750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196386/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196386",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196381,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498537,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.25,
                    "winPriceNum": 1250,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196381/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196381",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196384,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498540,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.3,
                    "winPriceNum": 2300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196384/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196384",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196375,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498531,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.1,
                    "winPriceNum": 2100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196375/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196375",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196385,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498541,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.1,
                    "winPriceNum": 2100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196385/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196385",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196376,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498532,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.3,
                    "winPriceNum": 2300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196376/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196376",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196390,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498546,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196390/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196390",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196378,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498534,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196378/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196378",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196380,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498536,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196380/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196380",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196379,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498535,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196379/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196379",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196382,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498538,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196382/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196382",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196383,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498539,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196383/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732882/Selections/646196383",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732816,
        "externalId": 258201275,
        "name": "To Score 2 or more Tries",
        "statusCode": "A",
        "sort": 25,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote Others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816",
        "selections": [
            {
                "id": 646195662,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498626,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195662/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195662",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195657,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498621,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195657/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195657",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195660,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498624,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195660/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195660",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195666,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498630,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195666/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195666",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195664,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498628,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195664/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195664",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195653,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498617,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195653/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195653",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195655,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498619,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195655/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195655",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195663,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498627,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195663/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195663",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195658,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498622,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195658/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195658",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195665,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498629,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195665/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195665",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195651,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498615,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195651/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195651",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195656,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498620,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195656/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195656",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195654,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498618,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195654/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195654",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195667,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498631,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195667/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195667",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195652,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498616,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195652/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195652",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195659,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498623,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195659/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195659",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195661,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498625,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195661/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195661",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195683,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498647,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195683/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195683",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195682,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498646,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.2,
                    "winPriceNum": 3200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195682/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195682",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195671,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498635,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195671/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195671",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195675,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498639,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195675/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195675",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195681,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498645,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195681/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195681",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195668,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498632,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195668/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195668",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195680,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498644,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195680/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195680",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195669,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498633,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195669/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195669",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195679,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498643,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195679/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195679",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195678,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498642,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195678/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195678",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195670,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498634,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195670/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195670",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195684,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498648,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195684/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195684",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195672,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498636,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195672/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195672",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195674,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498638,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195674/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195674",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195673,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498637,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195673/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195673",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195676,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498640,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195676/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195676",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195677,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498641,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195677/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732816/Selections/646195677",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732842,
        "externalId": 258201276,
        "name": "To Score 3 or more Tries",
        "statusCode": "A",
        "sort": 30,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote Others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842",
        "selections": [
            {
                "id": 646195960,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498655,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195960/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195960",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195965,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498660,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195965/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195965",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195969,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498664,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195969/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195969",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195963,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498658,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195963/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195963",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195958,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498653,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195958/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195958",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195956,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498651,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195956/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195956",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195961,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498656,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195961/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195961",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195968,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498663,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195968/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195968",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195954,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498649,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195954/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195954",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195966,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498661,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195966/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195966",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195959,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498654,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195959/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195959",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195957,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498652,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195957/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195957",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195970,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498665,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195970/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195970",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195955,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498650,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195955/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195955",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195967,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498662,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195967/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195967",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195962,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498657,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195962/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195962",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195964,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498659,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195964/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195964",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195986,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498681,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195986/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195986",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195985,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498680,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195985/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195985",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195974,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498669,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195974/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195974",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195978,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498673,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195978/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195978",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195984,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498679,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195984/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195984",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195971,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498666,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195971/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195971",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195983,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498678,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195983/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195983",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195972,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498667,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195972/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195972",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195982,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498677,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195982/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195982",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195981,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498676,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195981/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195981",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195973,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498668,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195973/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195973",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195987,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498682,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195987/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195987",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195975,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498670,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195975/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195975",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195977,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498672,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195977/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195977",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195976,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498671,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195976/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195976",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195980,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498675,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195980/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195980",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195979,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498674,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195979/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732842/Selections/646195979",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732814,
        "externalId": 258201334,
        "name": "Win Try Combo",
        "statusCode": "A",
        "sort": 35,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17. If the match is a draw after extra time all bets in this market will be deemed losers as neither team has won the match.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814",
        "selections": [
            {
                "id": 646195630,
                "name": "Brian To'o to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499775,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.53,
                    "winPriceNum": 530,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195630/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195630",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195629,
                "name": "Charlie Staines to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499774,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.57,
                    "winPriceNum": 570,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195629/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195629",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195616,
                "name": "Kurt Capewell to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499761,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.88,
                    "winPriceNum": 1880,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195616/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195616",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195626,
                "name": "Liam Martin to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499771,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.88,
                    "winPriceNum": 1880,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195626/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195626",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195615,
                "name": "Matt Burton to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499760,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.7,
                    "winPriceNum": 1700,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195615/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195615",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195628,
                "name": "Paul Momirovski to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499773,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.5,
                    "winPriceNum": 1500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195628/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195628",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195618,
                "name": "Stephen Crichton to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499763,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2,
                    "winPriceNum": 1000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195618/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195618",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195627,
                "name": "Tyrone May to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499772,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.7,
                    "winPriceNum": 1700,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195627/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195627",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195622,
                "name": "Viliame Kikau to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499767,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.2,
                    "winPriceNum": 1200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195622/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195622",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195625,
                "name": "Jarome Luai to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499770,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.1,
                    "winPriceNum": 2100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195625/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195625",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195643,
                "name": "Jason Saab to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499788,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.6,
                    "winPriceNum": 2600,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195643/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195643",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195617,
                "name": "Nathan Cleary to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499762,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.1,
                    "winPriceNum": 2100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195617/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195617",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195638,
                "name": "Reuben Garrick to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499783,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.5,
                    "winPriceNum": 2500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195638/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195638",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195631,
                "name": "Isaah Yeo to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499776,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.2,
                    "winPriceNum": 3200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195631/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195631",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195619,
                "name": "Matt Eisenhuth to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499764,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.2,
                    "winPriceNum": 3200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195619/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195619",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195621,
                "name": "Mitch Kenny to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499766,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195621/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195621",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195641,
                "name": "Brad Parker to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499786,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195641/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195641",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195647,
                "name": "Dylan Walker to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499792,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195647/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195647",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195634,
                "name": "Daly Cherry-Evans to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499779,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195634/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195634",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195620,
                "name": "James Fisher-Harris to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499765,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195620/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195620",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195624,
                "name": "Moses Leota to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499769,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195624/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195624",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195645,
                "name": "Moses Suli to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499790,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195645/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195645",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195623,
                "name": "Spencer Leniu to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499768,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195623/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195623",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195636,
                "name": "Cade Cust to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499781,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195636/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195636",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195644,
                "name": "Joshua Schuster to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499789,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195644/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195644",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195639,
                "name": "Jack Gosiewski to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499784,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195639/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195639",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195637,
                "name": "Kieran Foran to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499782,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195637/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195637",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195632,
                "name": "Josh Alolai to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499777,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195632/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195632",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195635,
                "name": "Lachlan Croker to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499780,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195635/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195635",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195646,
                "name": "Jake Trbojevic to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499791,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195646/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195646",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195609,
                "name": "Jason Saab to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499754,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195609/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195609",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195604,
                "name": "Reuben Garrick to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499749,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195604/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195604",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195648,
                "name": "Martin Taupau to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499793,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195648/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195648",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195640,
                "name": "Sean Keppie to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499785,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195640/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195640",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195596,
                "name": "Brian To'o to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499741,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195596/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195596",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195633,
                "name": "Morgan Boyle to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499778,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195633/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195633",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195642,
                "name": "Taniela Paseka to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499787,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195642/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195642",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195595,
                "name": "Charlie Staines to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499740,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195595/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195595",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195613,
                "name": "Dylan Walker to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499758,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195613/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195613",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195611,
                "name": "Moses Suli to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499756,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195611/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195611",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195607,
                "name": "Brad Parker to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499752,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195607/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195607",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195584,
                "name": "Stephen Crichton to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499729,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195584/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195584",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195600,
                "name": "Daly Cherry-Evans to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499745,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195600/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195600",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195602,
                "name": "Cade Cust to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499747,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195602/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195602",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195610,
                "name": "Joshua Schuster to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499755,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195610/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195610",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195581,
                "name": "Matt Burton to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499726,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195581/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195581",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195594,
                "name": "Paul Momirovski to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499739,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195594/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195594",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195593,
                "name": "Tyrone May to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499738,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195593/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195593",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195588,
                "name": "Viliame Kikau to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499733,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195588/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195588",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195605,
                "name": "Jack Gosiewski to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499750,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195605/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195605",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195603,
                "name": "Kieran Foran to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499748,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195603/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195603",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195591,
                "name": "Jarome Luai to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499736,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195591/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195591",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195598,
                "name": "Josh Alolai to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499743,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195598/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195598",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195582,
                "name": "Kurt Capewell to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499727,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195582/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195582",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195601,
                "name": "Lachlan Croker to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499746,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195601/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195601",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195592,
                "name": "Liam Martin to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499737,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195592/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195592",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195583,
                "name": "Nathan Cleary to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499728,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195583/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195583",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195597,
                "name": "Isaah Yeo to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499742,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195597/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195597",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195612,
                "name": "Jake Trbojevic to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499757,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195612/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195612",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195585,
                "name": "Matt Eisenhuth to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499730,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195585/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195585",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195614,
                "name": "Martin Taupau to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499759,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195614/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195614",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195606,
                "name": "Sean Keppie to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499751,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195606/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195606",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195599,
                "name": "Morgan Boyle to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499744,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195599/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195599",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195608,
                "name": "Taniela Paseka to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499753,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195608/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195608",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195587,
                "name": "Mitch Kenny to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499732,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195587/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195587",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195586,
                "name": "James Fisher-Harris to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499731,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195586/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195586",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195589,
                "name": "Spencer Leniu to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499734,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195589/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195589",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195590,
                "name": "Moses Leota to score a try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499735,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195590/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732814/Selections/646195590",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732905,
        "externalId": 258201335,
        "name": "Win First Try Combo",
        "statusCode": "A",
        "sort": 40,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17. If the match is a draw after extra time all bets in this market will be deemed losers as neither team has won the match.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905",
        "selections": [
            {
                "id": 646196784,
                "name": "Brian To'o to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499843,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196784/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196784",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196783,
                "name": "Charlie Staines to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499842,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196783/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196783",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196772,
                "name": "Stephen Crichton to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499831,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196772/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196772",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196776,
                "name": "Viliame Kikau to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499835,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196776/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196776",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196769,
                "name": "Matt Burton to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499828,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196769/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196769",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196782,
                "name": "Paul Momirovski to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499841,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196782/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196782",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196781,
                "name": "Tyrone May to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499840,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196781/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196781",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196770,
                "name": "Kurt Capewell to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499829,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196770/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196770",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196780,
                "name": "Liam Martin to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499839,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196780/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196780",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196771,
                "name": "Nathan Cleary to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499830,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196771/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196771",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196779,
                "name": "Jarome Luai to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499838,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196779/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196779",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196792,
                "name": "Reuben Garrick to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499851,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196792/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196792",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196797,
                "name": "Jason Saab to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499856,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196797/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196797",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196785,
                "name": "Isaah Yeo to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499844,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196785/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196785",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196773,
                "name": "Matt Eisenhuth to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499832,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196773/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196773",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196775,
                "name": "Mitch Kenny to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499834,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196775/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196775",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196801,
                "name": "Dylan Walker to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499860,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196801/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196801",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196795,
                "name": "Brad Parker to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499854,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196795/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196795",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196799,
                "name": "Moses Suli to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499858,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196799/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196799",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196774,
                "name": "James Fisher-Harris to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499833,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196774/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196774",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196778,
                "name": "Moses Leota to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499837,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196778/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196778",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196777,
                "name": "Spencer Leniu to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499836,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196777/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196777",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196790,
                "name": "Cade Cust to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499849,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196790/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196790",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196788,
                "name": "Daly Cherry-Evans to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499847,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196788/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196788",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196798,
                "name": "Joshua Schuster to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499857,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196798/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196798",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196763,
                "name": "Jason Saab to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499822,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196763/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196763",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196791,
                "name": "Kieran Foran to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499850,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196791/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196791",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196758,
                "name": "Reuben Garrick to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499817,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196758/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196758",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196793,
                "name": "Jack Gosiewski to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499852,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196793/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196793",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196750,
                "name": "Brian To'o to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499809,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196750/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196750",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196800,
                "name": "Jake Trbojevic to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499859,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196800/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196800",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196786,
                "name": "Josh Alolai to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499845,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196786/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196786",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196789,
                "name": "Lachlan Croker to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499848,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196789/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196789",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196749,
                "name": "Charlie Staines to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499808,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196749/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196749",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196754,
                "name": "Daly Cherry-Evans to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499813,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196754/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196754",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196802,
                "name": "Martin Taupau to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499861,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196802/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196802",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196765,
                "name": "Moses Suli to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499824,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196765/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196765",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196794,
                "name": "Sean Keppie to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499853,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196794/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196794",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196761,
                "name": "Brad Parker to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499820,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196761/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196761",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196756,
                "name": "Cade Cust to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499815,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196756/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196756",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196767,
                "name": "Dylan Walker to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499826,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196767/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196767",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196764,
                "name": "Joshua Schuster to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499823,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196764/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196764",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196738,
                "name": "Stephen Crichton to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499797,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196738/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196738",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196757,
                "name": "Kieran Foran to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499816,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196757/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196757",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196787,
                "name": "Morgan Boyle to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499846,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196787/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196787",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196796,
                "name": "Taniela Paseka to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1196499855,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196796/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196796",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196736,
                "name": "Kurt Capewell to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499795,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196736/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196736",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196746,
                "name": "Liam Martin to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499805,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196746/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196746",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196735,
                "name": "Matt Burton to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499794,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196735/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196735",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196747,
                "name": "Tyrone May to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499806,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196747/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196747",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196759,
                "name": "Jack Gosiewski to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499818,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196759/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196759",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196748,
                "name": "Paul Momirovski to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499807,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196748/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196748",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196742,
                "name": "Viliame Kikau to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499801,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196742/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196742",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196745,
                "name": "Jarome Luai to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499804,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196745/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196745",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196752,
                "name": "Josh Alolai to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499811,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196752/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196752",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196755,
                "name": "Lachlan Croker to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499814,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196755/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196755",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196753,
                "name": "Morgan Boyle to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499812,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196753/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196753",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196762,
                "name": "Taniela Paseka to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499821,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196762/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196762",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196751,
                "name": "Isaah Yeo to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499810,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196751/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196751",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196739,
                "name": "Matt Eisenhuth to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499798,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196739/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196739",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196766,
                "name": "Jake Trbojevic to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499825,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196766/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196766",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196768,
                "name": "Martin Taupau to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499827,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196768/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196768",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196760,
                "name": "Sean Keppie to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499819,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196760/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196760",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196737,
                "name": "Nathan Cleary to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499796,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196737/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196737",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196740,
                "name": "James Fisher-Harris to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499799,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196740/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196740",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196744,
                "name": "Moses Leota to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499803,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196744/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196744",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196743,
                "name": "Spencer Leniu to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499802,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196743/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196743",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196741,
                "name": "Mitch Kenny to score the first try and Manly Sea Eagles to win",
                "resultType": "-",
                "externalId": 1196499800,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196741/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732905/Selections/646196741",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732837,
        "externalId": 258201273,
        "name": "To Score A Try - First Half",
        "statusCode": "A",
        "sort": 175,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837",
        "selections": [
            {
                "id": 646195868,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498558,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195868/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195868",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195863,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498553,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195863/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195863",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195872,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498562,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195872/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195872",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195866,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498556,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195866/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195866",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195870,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498560,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195870/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195870",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195859,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498549,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195859/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195859",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195861,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498551,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195861/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195861",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195869,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498559,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195869/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195869",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195864,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498554,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195864/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195864",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195862,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498552,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195862/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195862",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195857,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498547,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195857/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195857",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195860,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498550,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195860/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195860",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195871,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498561,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195871/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195871",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195873,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498563,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195873/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195873",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195865,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498555,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195865/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195865",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195858,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498548,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195858/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195858",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195867,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498557,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195867/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195867",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195889,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498579,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.5,
                    "winPriceNum": 1500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195889/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195889",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195888,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498578,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.63,
                    "winPriceNum": 1630,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195888/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195888",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195877,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498567,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.6,
                    "winPriceNum": 2600,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195877/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195877",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195881,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498571,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195881/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195881",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195874,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498564,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195874/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195874",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195887,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498577,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195887/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195887",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195886,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498576,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195886/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195886",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195875,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498565,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195875/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195875",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195885,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498575,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195885/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195885",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195884,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498574,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195884/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195884",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195876,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498566,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195876/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195876",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195890,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498580,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195890/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195890",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195878,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498568,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195878/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195878",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195880,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498570,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195880/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195880",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195879,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498569,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195879/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195879",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195882,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498572,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195882/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195882",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195883,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498573,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195883/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732837/Selections/646195883",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732867,
        "externalId": 258201280,
        "name": "First 2nd Half Tryscorer",
        "statusCode": "A",
        "sort": 240,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote Others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867",
        "selections": [
            {
                "id": 646196194,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498760,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196194/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196194",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196199,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498765,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196199/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196199",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196197,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498763,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196197/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196197",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196203,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498769,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196203/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196203",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196201,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498767,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196201/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196201",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196192,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498758,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196192/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196192",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196190,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498756,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196190/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196190",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196200,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498766,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196200/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196200",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196195,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498761,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196195/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196195",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196193,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498759,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196193/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196193",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196202,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498768,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196202/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196202",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196188,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498754,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196188/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196188",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196191,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498757,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196191/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196191",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196204,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498770,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196204/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196204",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196189,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498755,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196189/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196189",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196196,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498762,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196196/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196196",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196198,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498764,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196198/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196198",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196222,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196498788,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196222/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196222",
                "outcomeVariants": []
            },
            {
                "id": 646196220,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498786,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196220/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196220",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196219,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498785,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196219/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196219",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196208,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498774,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196208/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196208",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196212,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498778,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196212/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196212",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196205,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498771,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196205/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196205",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196218,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498784,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196218/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196218",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196217,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498783,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196217/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196217",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196206,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498772,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196206/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196206",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196216,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498782,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196216/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196216",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196215,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498781,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196215/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196215",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196207,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498773,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196207/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196207",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196221,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498787,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196221/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196221",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196209,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498775,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196209/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196209",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196211,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498777,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196211/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196211",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196210,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498776,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196210/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196210",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196213,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498779,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196213/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196213",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196214,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498780,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196214/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732867/Selections/646196214",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732795,
        "externalId": 258201312,
        "name": "Try Scorer - Exacta",
        "statusCode": "A",
        "sort": 406,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795",
        "selections": [
            {
                "id": 646195337,
                "name": "1st: Brian To'o, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499488,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195337/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195337",
                "outcomeVariants": []
            },
            {
                "id": 646195336,
                "name": "1st: Brian To'o, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499487,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195336/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195336",
                "outcomeVariants": []
            },
            {
                "id": 646195327,
                "name": "1st: Charlie Staines, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499478,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195327/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195327",
                "outcomeVariants": []
            },
            {
                "id": 646195326,
                "name": "1st: Charlie Staines, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499477,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195326/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195326",
                "outcomeVariants": []
            },
            {
                "id": 646195307,
                "name": "1st: Stephen Crichton, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499458,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195307/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195307",
                "outcomeVariants": []
            },
            {
                "id": 646195306,
                "name": "1st: Stephen Crichton, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499457,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195306/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195306",
                "outcomeVariants": []
            },
            {
                "id": 646195334,
                "name": "1st: Brian To'o, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499485,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195334/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195334",
                "outcomeVariants": []
            },
            {
                "id": 646195324,
                "name": "1st: Charlie Staines, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499475,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195324/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195324",
                "outcomeVariants": []
            },
            {
                "id": 646195333,
                "name": "1st: Brian To'o, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499484,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195333/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195333",
                "outcomeVariants": []
            },
            {
                "id": 646195297,
                "name": "1st: Matt Burton, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499448,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195297/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195297",
                "outcomeVariants": []
            },
            {
                "id": 646195335,
                "name": "1st: Brian To'o, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499486,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195335/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195335",
                "outcomeVariants": []
            },
            {
                "id": 646195296,
                "name": "1st: Matt Burton, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499447,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195296/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195296",
                "outcomeVariants": []
            },
            {
                "id": 646195317,
                "name": "1st: Paul Momirovski, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499468,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195317/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195317",
                "outcomeVariants": []
            },
            {
                "id": 646195316,
                "name": "1st: Paul Momirovski, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499467,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195316/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195316",
                "outcomeVariants": []
            },
            {
                "id": 646195323,
                "name": "1st: Charlie Staines, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499474,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195323/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195323",
                "outcomeVariants": []
            },
            {
                "id": 646195325,
                "name": "1st: Charlie Staines, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499476,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195325/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195325",
                "outcomeVariants": []
            },
            {
                "id": 646195349,
                "name": "1st: Reuben Garrick, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499498,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195349/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195349",
                "outcomeVariants": []
            },
            {
                "id": 646195348,
                "name": "1st: Reuben Garrick, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499497,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195348/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195348",
                "outcomeVariants": []
            },
            {
                "id": 646195304,
                "name": "1st: Stephen Crichton, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499455,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195304/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195304",
                "outcomeVariants": []
            },
            {
                "id": 646195339,
                "name": "1st: Brian To'o, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499489,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195339/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195339",
                "outcomeVariants": []
            },
            {
                "id": 646195328,
                "name": "1st: Charlie Staines, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499479,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195328/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195328",
                "outcomeVariants": []
            },
            {
                "id": 646195368,
                "name": "1st: Jason Saab, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499517,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195368/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195368",
                "outcomeVariants": []
            },
            {
                "id": 646195315,
                "name": "1st: Paul Momirovski, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499466,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195315/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195315",
                "outcomeVariants": []
            },
            {
                "id": 646195314,
                "name": "1st: Paul Momirovski, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499465,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195314/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195314",
                "outcomeVariants": []
            },
            {
                "id": 646195342,
                "name": "1st: Brian To'o, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499491,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195342/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195342",
                "outcomeVariants": []
            },
            {
                "id": 646195330,
                "name": "1st: Charlie Staines, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499481,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195330/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195330",
                "outcomeVariants": []
            },
            {
                "id": 646195389,
                "name": "1st: Dylan Walker, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499538,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195389/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195389",
                "outcomeVariants": []
            },
            {
                "id": 646195369,
                "name": "1st: Jason Saab, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499518,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195369/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195369",
                "outcomeVariants": []
            },
            {
                "id": 646195295,
                "name": "1st: Matt Burton, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499446,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195295/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195295",
                "outcomeVariants": []
            },
            {
                "id": 646195294,
                "name": "1st: Matt Burton, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499445,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195294/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195294",
                "outcomeVariants": []
            },
            {
                "id": 646195346,
                "name": "1st: Reuben Garrick, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499495,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195346/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195346",
                "outcomeVariants": []
            },
            {
                "id": 646195305,
                "name": "1st: Stephen Crichton, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499456,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195305/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195305",
                "outcomeVariants": []
            },
            {
                "id": 646195366,
                "name": "1st: Jason Saab, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499515,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195366/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195366",
                "outcomeVariants": []
            },
            {
                "id": 646195313,
                "name": "1st: Paul Momirovski, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499464,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195313/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195313",
                "outcomeVariants": []
            },
            {
                "id": 646195303,
                "name": "1st: Stephen Crichton, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499454,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195303/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195303",
                "outcomeVariants": []
            },
            {
                "id": 646195308,
                "name": "1st: Stephen Crichton, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499459,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195308/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195308",
                "outcomeVariants": []
            },
            {
                "id": 646195341,
                "name": "1st: Brian To'o, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499490,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195341/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195341",
                "outcomeVariants": []
            },
            {
                "id": 646195343,
                "name": "1st: Brian To'o, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499492,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195343/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195343",
                "outcomeVariants": []
            },
            {
                "id": 646195332,
                "name": "1st: Charlie Staines, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499483,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195332/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195332",
                "outcomeVariants": []
            },
            {
                "id": 646195331,
                "name": "1st: Charlie Staines, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499482,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195331/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195331",
                "outcomeVariants": []
            },
            {
                "id": 646195298,
                "name": "1st: Matt Burton, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499449,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195298/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195298",
                "outcomeVariants": []
            },
            {
                "id": 646195320,
                "name": "1st: Paul Momirovski, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499471,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195320/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195320",
                "outcomeVariants": []
            },
            {
                "id": 646195347,
                "name": "1st: Reuben Garrick, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499496,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195347/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195347",
                "outcomeVariants": []
            },
            {
                "id": 646195344,
                "name": "1st: Brian To'o, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499493,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195344/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195344",
                "outcomeVariants": []
            },
            {
                "id": 646195329,
                "name": "1st: Charlie Staines, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499480,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195329/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195329",
                "outcomeVariants": []
            },
            {
                "id": 646195365,
                "name": "1st: Jason Saab, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499514,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195365/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195365",
                "outcomeVariants": []
            },
            {
                "id": 646195370,
                "name": "1st: Jason Saab, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499519,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195370/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195370",
                "outcomeVariants": []
            },
            {
                "id": 646195300,
                "name": "1st: Matt Burton, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499451,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195300/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195300",
                "outcomeVariants": []
            },
            {
                "id": 646195293,
                "name": "1st: Matt Burton, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499444,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195293/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195293",
                "outcomeVariants": []
            },
            {
                "id": 646195345,
                "name": "1st: Reuben Garrick, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499494,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195345/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195345",
                "outcomeVariants": []
            },
            {
                "id": 646195310,
                "name": "1st: Stephen Crichton, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499461,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195310/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195310",
                "outcomeVariants": []
            },
            {
                "id": 646195359,
                "name": "1st: Brad Parker, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499508,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195359/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195359",
                "outcomeVariants": []
            },
            {
                "id": 646195379,
                "name": "1st: Moses Suli, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1196499528,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195379/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195379",
                "outcomeVariants": []
            },
            {
                "id": 646195378,
                "name": "1st: Moses Suli, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499527,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195378/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195378",
                "outcomeVariants": []
            },
            {
                "id": 646195352,
                "name": "1st: Reuben Garrick, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499501,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195352/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195352",
                "outcomeVariants": []
            },
            {
                "id": 646195388,
                "name": "1st: Dylan Walker, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499537,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195388/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195388",
                "outcomeVariants": []
            },
            {
                "id": 646195372,
                "name": "1st: Jason Saab, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499521,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195372/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195372",
                "outcomeVariants": []
            },
            {
                "id": 646195350,
                "name": "1st: Reuben Garrick, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499499,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195350/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195350",
                "outcomeVariants": []
            },
            {
                "id": 646195312,
                "name": "1st: Stephen Crichton, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499463,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195312/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195312",
                "outcomeVariants": []
            },
            {
                "id": 646195385,
                "name": "1st: Dylan Walker, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499534,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195385/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195385",
                "outcomeVariants": []
            },
            {
                "id": 646195367,
                "name": "1st: Jason Saab, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499516,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195367/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195367",
                "outcomeVariants": []
            },
            {
                "id": 646195321,
                "name": "1st: Paul Momirovski, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499472,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195321/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195321",
                "outcomeVariants": []
            },
            {
                "id": 646195318,
                "name": "1st: Paul Momirovski, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499469,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195318/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195318",
                "outcomeVariants": []
            },
            {
                "id": 646195375,
                "name": "1st: Moses Suli, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499524,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195375/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195375",
                "outcomeVariants": []
            },
            {
                "id": 646195358,
                "name": "1st: Brad Parker, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1196499507,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195358/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195358",
                "outcomeVariants": []
            },
            {
                "id": 646195376,
                "name": "1st: Moses Suli, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499525,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195376/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195376",
                "outcomeVariants": []
            },
            {
                "id": 646195353,
                "name": "1st: Reuben Garrick, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499502,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195353/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195353",
                "outcomeVariants": []
            },
            {
                "id": 646195357,
                "name": "1st: Brad Parker, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499506,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195357/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195357",
                "outcomeVariants": []
            },
            {
                "id": 646195392,
                "name": "1st: Dylan Walker, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499541,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195392/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195392",
                "outcomeVariants": []
            },
            {
                "id": 646195390,
                "name": "1st: Dylan Walker, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499539,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195390/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195390",
                "outcomeVariants": []
            },
            {
                "id": 646195373,
                "name": "1st: Jason Saab, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499522,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195373/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195373",
                "outcomeVariants": []
            },
            {
                "id": 646195309,
                "name": "1st: Stephen Crichton, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499460,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195309/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195309",
                "outcomeVariants": []
            },
            {
                "id": 646195360,
                "name": "1st: Brad Parker, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499509,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 401,
                    "winPriceNum": 400000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195360/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195360",
                "outcomeVariants": []
            },
            {
                "id": 646195356,
                "name": "1st: Brad Parker, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499505,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 401,
                    "winPriceNum": 400000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195356/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195356",
                "outcomeVariants": []
            },
            {
                "id": 646195387,
                "name": "1st: Dylan Walker, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499536,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 401,
                    "winPriceNum": 400000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195387/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195387",
                "outcomeVariants": []
            },
            {
                "id": 646195386,
                "name": "1st: Dylan Walker, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499535,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 401,
                    "winPriceNum": 400000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195386/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195386",
                "outcomeVariants": []
            },
            {
                "id": 646195374,
                "name": "1st: Jason Saab, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499523,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195374/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195374",
                "outcomeVariants": []
            },
            {
                "id": 646195299,
                "name": "1st: Matt Burton, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499450,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195299/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195299",
                "outcomeVariants": []
            },
            {
                "id": 646195377,
                "name": "1st: Moses Suli, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499526,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195377/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195377",
                "outcomeVariants": []
            },
            {
                "id": 646195380,
                "name": "1st: Moses Suli, 2nd: Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499529,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195380/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195380",
                "outcomeVariants": []
            },
            {
                "id": 646195322,
                "name": "1st: Paul Momirovski, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499473,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195322/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195322",
                "outcomeVariants": []
            },
            {
                "id": 646195311,
                "name": "1st: Stephen Crichton, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499462,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195311/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195311",
                "outcomeVariants": []
            },
            {
                "id": 646195361,
                "name": "1st: Brad Parker, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499510,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195361/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195361",
                "outcomeVariants": []
            },
            {
                "id": 646195364,
                "name": "1st: Brad Parker, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499513,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195364/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195364",
                "outcomeVariants": []
            },
            {
                "id": 646195362,
                "name": "1st: Brad Parker, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499511,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195362/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195362",
                "outcomeVariants": []
            },
            {
                "id": 646195355,
                "name": "1st: Brad Parker, 2nd: Matt Burton",
                "resultType": "-",
                "externalId": 1196499504,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195355/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195355",
                "outcomeVariants": []
            },
            {
                "id": 646195363,
                "name": "1st: Brad Parker, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499512,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195363/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195363",
                "outcomeVariants": []
            },
            {
                "id": 646195391,
                "name": "1st: Dylan Walker, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499540,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195391/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195391",
                "outcomeVariants": []
            },
            {
                "id": 646195394,
                "name": "1st: Dylan Walker, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499543,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195394/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195394",
                "outcomeVariants": []
            },
            {
                "id": 646195393,
                "name": "1st: Dylan Walker, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499542,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195393/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195393",
                "outcomeVariants": []
            },
            {
                "id": 646195371,
                "name": "1st: Jason Saab, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499520,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195371/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195371",
                "outcomeVariants": []
            },
            {
                "id": 646195302,
                "name": "1st: Matt Burton, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499453,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195302/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195302",
                "outcomeVariants": []
            },
            {
                "id": 646195301,
                "name": "1st: Matt Burton, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499452,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195301/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195301",
                "outcomeVariants": []
            },
            {
                "id": 646195381,
                "name": "1st: Moses Suli, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499530,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195381/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195381",
                "outcomeVariants": []
            },
            {
                "id": 646195384,
                "name": "1st: Moses Suli, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499533,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195384/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195384",
                "outcomeVariants": []
            },
            {
                "id": 646195382,
                "name": "1st: Moses Suli, 2nd: Jason Saab",
                "resultType": "-",
                "externalId": 1196499531,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195382/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195382",
                "outcomeVariants": []
            },
            {
                "id": 646195383,
                "name": "1st: Moses Suli, 2nd: Moses Suli",
                "resultType": "-",
                "externalId": 1196499532,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195383/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195383",
                "outcomeVariants": []
            },
            {
                "id": 646195319,
                "name": "1st: Paul Momirovski, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499470,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195319/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195319",
                "outcomeVariants": []
            },
            {
                "id": 646195351,
                "name": "1st: Reuben Garrick, 2nd: Brad Parker",
                "resultType": "-",
                "externalId": 1196499500,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195351/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195351",
                "outcomeVariants": []
            },
            {
                "id": 646195354,
                "name": "1st: Reuben Garrick, 2nd: Dylan Walker",
                "resultType": "-",
                "externalId": 1196499503,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195354/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732795/Selections/646195354",
                "outcomeVariants": []
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732891,
        "externalId": 258201313,
        "name": "Try Scorer - Quinella",
        "statusCode": "A",
        "sort": 407,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891",
        "selections": [
            {
                "id": 646196567,
                "name": "Charlie Staines / Brian To'o",
                "resultType": "-",
                "externalId": 1196499572,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196567/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196567",
                "outcomeVariants": []
            },
            {
                "id": 646196552,
                "name": "Stephen Crichton / Brian To'o",
                "resultType": "-",
                "externalId": 1196499557,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196552/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196552",
                "outcomeVariants": []
            },
            {
                "id": 646196551,
                "name": "Stephen Crichton / Charlie Staines",
                "resultType": "-",
                "externalId": 1196499556,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196551/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196551",
                "outcomeVariants": []
            },
            {
                "id": 646196573,
                "name": "Brian To'o / Brian To'o",
                "resultType": "-",
                "externalId": 1196499578,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196573/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196573",
                "outcomeVariants": []
            },
            {
                "id": 646196543,
                "name": "Matt Burton / Brian To'o",
                "resultType": "-",
                "externalId": 1196499548,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196543/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196543",
                "outcomeVariants": []
            },
            {
                "id": 646196560,
                "name": "Paul Momirovski / Brian To'o",
                "resultType": "-",
                "externalId": 1196499565,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196560/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196560",
                "outcomeVariants": []
            },
            {
                "id": 646196566,
                "name": "Charlie Staines / Charlie Staines",
                "resultType": "-",
                "externalId": 1196499571,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196566/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196566",
                "outcomeVariants": []
            },
            {
                "id": 646196542,
                "name": "Matt Burton / Charlie Staines",
                "resultType": "-",
                "externalId": 1196499547,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196542/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196542",
                "outcomeVariants": []
            },
            {
                "id": 646196559,
                "name": "Paul Momirovski / Charlie Staines",
                "resultType": "-",
                "externalId": 1196499564,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196559/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196559",
                "outcomeVariants": []
            },
            {
                "id": 646196574,
                "name": "Brian To'o / Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499579,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196574/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196574",
                "outcomeVariants": []
            },
            {
                "id": 646196568,
                "name": "Charlie Staines / Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499573,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196568/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196568",
                "outcomeVariants": []
            },
            {
                "id": 646196570,
                "name": "Charlie Staines / Jason Saab",
                "resultType": "-",
                "externalId": 1196499575,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196570/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196570",
                "outcomeVariants": []
            },
            {
                "id": 646196576,
                "name": "Brian To'o / Jason Saab",
                "resultType": "-",
                "externalId": 1196499581,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196576/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196576",
                "outcomeVariants": []
            },
            {
                "id": 646196550,
                "name": "Stephen Crichton / Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499555,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196550/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196550",
                "outcomeVariants": []
            },
            {
                "id": 646196541,
                "name": "Matt Burton / Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499546,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196541/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196541",
                "outcomeVariants": []
            },
            {
                "id": 646196540,
                "name": "Matt Burton / Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499545,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196540/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196540",
                "outcomeVariants": []
            },
            {
                "id": 646196553,
                "name": "Stephen Crichton / Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499558,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196553/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196553",
                "outcomeVariants": []
            },
            {
                "id": 646196578,
                "name": "Brian To'o / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499583,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196578/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196578",
                "outcomeVariants": []
            },
            {
                "id": 646196575,
                "name": "Brian To'o / Brad Parker",
                "resultType": "-",
                "externalId": 1196499580,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196575/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196575",
                "outcomeVariants": []
            },
            {
                "id": 646196571,
                "name": "Charlie Staines / Moses Suli",
                "resultType": "-",
                "externalId": 1196499576,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196571/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196571",
                "outcomeVariants": []
            },
            {
                "id": 646196544,
                "name": "Matt Burton / Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499549,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196544/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196544",
                "outcomeVariants": []
            },
            {
                "id": 646196555,
                "name": "Stephen Crichton / Jason Saab",
                "resultType": "-",
                "externalId": 1196499560,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196555/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196555",
                "outcomeVariants": []
            },
            {
                "id": 646196577,
                "name": "Brian To'o / Moses Suli",
                "resultType": "-",
                "externalId": 1196499582,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196577/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196577",
                "outcomeVariants": []
            },
            {
                "id": 646196572,
                "name": "Charlie Staines / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499577,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196572/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196572",
                "outcomeVariants": []
            },
            {
                "id": 646196563,
                "name": "Paul Momirovski / Jason Saab",
                "resultType": "-",
                "externalId": 1196499568,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196563/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196563",
                "outcomeVariants": []
            },
            {
                "id": 646196558,
                "name": "Paul Momirovski / Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499563,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196558/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196558",
                "outcomeVariants": []
            },
            {
                "id": 646196561,
                "name": "Paul Momirovski / Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499566,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196561/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196561",
                "outcomeVariants": []
            },
            {
                "id": 646196581,
                "name": "Reuben Garrick / Jason Saab",
                "resultType": "-",
                "externalId": 1196499586,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196581/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196581",
                "outcomeVariants": []
            },
            {
                "id": 646196549,
                "name": "Stephen Crichton / Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499554,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196549/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196549",
                "outcomeVariants": []
            },
            {
                "id": 646196569,
                "name": "Charlie Staines / Brad Parker",
                "resultType": "-",
                "externalId": 1196499574,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196569/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196569",
                "outcomeVariants": []
            },
            {
                "id": 646196546,
                "name": "Matt Burton / Jason Saab",
                "resultType": "-",
                "externalId": 1196499551,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196546/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196546",
                "outcomeVariants": []
            },
            {
                "id": 646196557,
                "name": "Stephen Crichton / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499562,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196557/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196557",
                "outcomeVariants": []
            },
            {
                "id": 646196564,
                "name": "Paul Momirovski / Moses Suli",
                "resultType": "-",
                "externalId": 1196499569,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196564/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196564",
                "outcomeVariants": []
            },
            {
                "id": 646196582,
                "name": "Reuben Garrick / Moses Suli",
                "resultType": "-",
                "externalId": 1196499587,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196582/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196582",
                "outcomeVariants": []
            },
            {
                "id": 646196590,
                "name": "Jason Saab / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499595,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196590/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196590",
                "outcomeVariants": []
            },
            {
                "id": 646196548,
                "name": "Matt Burton / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499553,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196548/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196548",
                "outcomeVariants": []
            },
            {
                "id": 646196539,
                "name": "Matt Burton / Matt Burton",
                "resultType": "-",
                "externalId": 1196499544,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196539/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196539",
                "outcomeVariants": []
            },
            {
                "id": 646196547,
                "name": "Matt Burton / Moses Suli",
                "resultType": "-",
                "externalId": 1196499552,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196547/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196547",
                "outcomeVariants": []
            },
            {
                "id": 646196554,
                "name": "Stephen Crichton / Brad Parker",
                "resultType": "-",
                "externalId": 1196499559,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196554/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196554",
                "outcomeVariants": []
            },
            {
                "id": 646196556,
                "name": "Stephen Crichton / Moses Suli",
                "resultType": "-",
                "externalId": 1196499561,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196556/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196556",
                "outcomeVariants": []
            },
            {
                "id": 646196562,
                "name": "Paul Momirovski / Brad Parker",
                "resultType": "-",
                "externalId": 1196499567,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196562/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196562",
                "outcomeVariants": []
            },
            {
                "id": 646196565,
                "name": "Paul Momirovski / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499570,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196565/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196565",
                "outcomeVariants": []
            },
            {
                "id": 646196583,
                "name": "Reuben Garrick / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499588,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196583/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196583",
                "outcomeVariants": []
            },
            {
                "id": 646196588,
                "name": "Jason Saab / Jason Saab",
                "resultType": "-",
                "externalId": 1196499593,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196588/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196588",
                "outcomeVariants": []
            },
            {
                "id": 646196589,
                "name": "Jason Saab / Moses Suli",
                "resultType": "-",
                "externalId": 1196499594,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196589/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196589",
                "outcomeVariants": []
            },
            {
                "id": 646196545,
                "name": "Matt Burton / Brad Parker",
                "resultType": "-",
                "externalId": 1196499550,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196545/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196545",
                "outcomeVariants": []
            },
            {
                "id": 646196580,
                "name": "Reuben Garrick / Brad Parker",
                "resultType": "-",
                "externalId": 1196499585,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196580/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196580",
                "outcomeVariants": []
            },
            {
                "id": 646196579,
                "name": "Reuben Garrick / Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499584,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196579/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196579",
                "outcomeVariants": []
            },
            {
                "id": 646196585,
                "name": "Brad Parker / Jason Saab",
                "resultType": "-",
                "externalId": 1196499590,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196585/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196585",
                "outcomeVariants": []
            },
            {
                "id": 646196593,
                "name": "Moses Suli / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499597,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 401,
                    "winPriceNum": 400000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196593/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196593",
                "outcomeVariants": []
            },
            {
                "id": 646196587,
                "name": "Brad Parker / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499592,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196587/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196587",
                "outcomeVariants": []
            },
            {
                "id": 646196584,
                "name": "Brad Parker / Brad Parker",
                "resultType": "-",
                "externalId": 1196499589,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196584/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196584",
                "outcomeVariants": []
            },
            {
                "id": 646196586,
                "name": "Brad Parker / Moses Suli",
                "resultType": "-",
                "externalId": 1196499591,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196586/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196586",
                "outcomeVariants": []
            },
            {
                "id": 646196595,
                "name": "Dylan Walker / Dylan Walker",
                "resultType": "-",
                "externalId": 1196499598,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196595/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196595",
                "outcomeVariants": []
            },
            {
                "id": 646196591,
                "name": "Moses Suli / Moses Suli",
                "resultType": "-",
                "externalId": 1196499596,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196591/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732891/Selections/646196591",
                "outcomeVariants": []
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732864,
        "externalId": 258201267,
        "name": "Second Tryscorer",
        "statusCode": "A",
        "sort": 408,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864",
        "selections": [
            {
                "id": 646196140,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498440,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196140/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196140",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196146,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498445,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196146/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196146",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196144,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498443,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196144/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196144",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196150,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498449,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196150/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196150",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196148,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498447,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196148/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196148",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196135,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498436,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196135/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196135",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196137,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498438,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196137/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196137",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196142,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498441,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196142/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196142",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196147,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498446,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196147/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196147",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196133,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498434,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196133/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196133",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196138,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498439,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196138/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196138",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196136,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498437,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196136/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196136",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196149,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498448,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196149/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196149",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196151,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498450,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196151/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196151",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196143,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498442,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196143/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196143",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196134,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498435,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196134/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196134",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196145,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498444,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196145/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196145",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196169,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196498468,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196169/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196169",
                "outcomeVariants": []
            },
            {
                "id": 646196167,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498466,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196167/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196167",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196166,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498465,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196166/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196166",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196155,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498454,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196155/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196155",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196159,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498458,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196159/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196159",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196152,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498451,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196152/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196152",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196165,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498464,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196165/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196165",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196164,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498463,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196164/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196164",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196153,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498452,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196153/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196153",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196163,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498462,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196163/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196163",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196162,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498461,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196162/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196162",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196154,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498453,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196154/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196154",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196168,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498467,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196168/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196168",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196156,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498455,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196156/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196156",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196158,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498457,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196158/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196158",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196157,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498456,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196157/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196157",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196161,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498460,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196161/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196161",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196160,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498459,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196160/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732864/Selections/646196160",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732909,
        "externalId": 258201268,
        "name": "Third Tryscorer",
        "statusCode": "A",
        "sort": 409,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909",
        "selections": [
            {
                "id": 646196822,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498480,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196822/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196822",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196817,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498475,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196817/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196817",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196820,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498478,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196820/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196820",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196826,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498484,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196826/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196826",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196824,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498482,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196824/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196824",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196813,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498471,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196813/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196813",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196815,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498473,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196815/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196815",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196823,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498481,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196823/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196823",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196818,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498476,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196818/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196818",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196811,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498469,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196811/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196811",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196814,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498472,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196814/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196814",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196825,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498483,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196825/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196825",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196816,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498474,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196816/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196816",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196827,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498485,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196827/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196827",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196819,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498477,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196819/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196819",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196812,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498470,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196812/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196812",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196821,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498479,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196821/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196821",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196845,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196498503,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196845/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196845",
                "outcomeVariants": []
            },
            {
                "id": 646196843,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498501,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196843/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196843",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196842,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498500,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196842/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196842",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196831,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498489,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196831/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196831",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196835,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498493,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196835/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196835",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196828,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498486,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196828/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196828",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196841,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498499,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196841/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196841",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196840,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498498,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196840/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196840",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196829,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498487,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196829/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196829",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196839,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498497,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196839/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196839",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196830,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498488,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196830/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196830",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196838,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498496,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196838/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196838",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196844,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498502,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196844/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196844",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196832,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498490,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196832/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196832",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196834,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498492,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196834/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196834",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196833,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498491,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196833/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196833",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196836,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498494,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196836/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196836",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196837,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498495,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196837/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732909/Selections/646196837",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732866,
        "externalId": 258201278,
        "name": "First Tryscorer - Manly Sea Eagles",
        "statusCode": "A",
        "sort": 410,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866",
        "selections": [
            {
                "id": 646196181,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498729,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196181/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196181",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196187,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196498735,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196187/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196187",
                "outcomeVariants": []
            },
            {
                "id": 646196176,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498724,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196176/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196176",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196185,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498733,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196185/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196185",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196179,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498727,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196179/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196179",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196183,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498731,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196183/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196183",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196172,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498720,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196172/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196172",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196174,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498722,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196174/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196174",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196182,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498730,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196182/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196182",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196177,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498725,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196177/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196177",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196175,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498723,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196175/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196175",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196170,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498718,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196170/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196170",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196173,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498721,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196173/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196173",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196184,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498732,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196184/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196184",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196186,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498734,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196186/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196186",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196171,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498719,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196171/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196171",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196178,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498726,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196178/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196178",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196180,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498728,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196180/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732866/Selections/646196180",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732904,
        "externalId": 258201279,
        "name": "First Tryscorer - Penrith Panthers",
        "statusCode": "A",
        "sort": 415,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904",
        "selections": [
            {
                "id": 646196732,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498751,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196732/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196732",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196731,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498750,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196731/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196731",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196720,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498739,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196720/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196720",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196724,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498743,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196724/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196724",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196717,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498736,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196717/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196717",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196730,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498749,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196730/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196730",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196729,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498748,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196729/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196729",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196718,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498737,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196718/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196718",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196728,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498747,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196728/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196728",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196727,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498746,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196727/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196727",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196719,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498738,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196719/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196719",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196733,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498752,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196733/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196733",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196721,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498740,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196721/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196721",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196723,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498742,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196723/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196723",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196722,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498741,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196722/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196722",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196725,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498744,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196725/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196725",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196726,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498745,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196726/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196726",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196734,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196498753,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196734/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732904/Selections/646196734",
                "outcomeVariants": []
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732835,
        "externalId": 258201281,
        "name": "Last Tryscorer - Manly Sea Eagles",
        "statusCode": "A",
        "sort": 420,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835",
        "selections": [
            {
                "id": 646195822,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196498806,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195822/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195822",
                "outcomeVariants": []
            },
            {
                "id": 646195811,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498795,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195811/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195811",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195816,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498800,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195816/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195816",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195820,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498804,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195820/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195820",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195814,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498798,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195814/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195814",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195818,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498802,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195818/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195818",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195807,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498791,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195807/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195807",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195809,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498793,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195809/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195809",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195817,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498801,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195817/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195817",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195810,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498794,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195810/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195810",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195812,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498796,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195812/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195812",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195805,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498789,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195805/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195805",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195808,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498792,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195808/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195808",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195819,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498803,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195819/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195819",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195821,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498805,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195821/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195821",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195806,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498790,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195806/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195806",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195813,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498797,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195813/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195813",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195815,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498799,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195815/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732835/Selections/646195815",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732800,
        "externalId": 258201282,
        "name": "Last Tryscorer - Penrith Panthers",
        "statusCode": "A",
        "sort": 425,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800",
        "selections": [
            {
                "id": 646195420,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498822,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195420/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195420",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195418,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498821,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195418/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195418",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195407,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498810,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195407/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195407",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195411,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498814,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195411/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195411",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195404,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498807,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195404/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195404",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195417,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498820,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195417/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195417",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195416,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498819,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195416/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195416",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195405,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498808,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195405/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195405",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195415,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498818,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195415/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195415",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195406,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498809,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195406/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195406",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195414,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498817,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195414/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195414",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195421,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498823,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195421/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195421",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195408,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498811,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195408/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195408",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195410,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498813,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195410/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195410",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195409,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498812,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195409/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195409",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195412,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498815,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195412/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195412",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195413,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498816,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195413/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195413",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646195423,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196498824,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195423/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732800/Selections/646195423",
                "outcomeVariants": []
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732863,
        "externalId": 258201277,
        "name": "Last Tryscorer",
        "statusCode": "A",
        "sort": 430,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863",
        "selections": [
            {
                "id": 646196104,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498689,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196104/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196104",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196109,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498694,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196109/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196109",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196107,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498692,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196107/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196107",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196113,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498698,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196113/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196113",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196100,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498685,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196100/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196100",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196111,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498696,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196111/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196111",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196102,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498687,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196102/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196102",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196110,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498695,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196110/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196110",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196103,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498688,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196103/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196103",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196105,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498690,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196105/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196105",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196098,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498683,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196098/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196098",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196101,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498686,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196101/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196101",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196112,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498697,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196112/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196112",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196114,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498699,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196114/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196114",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196106,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498691,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196106/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196106",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196099,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498684,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196099/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196099",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196108,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498693,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196108/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196108",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196132,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196498717,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196132/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196132",
                "outcomeVariants": []
            },
            {
                "id": 646196130,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498715,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196130/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196130",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196129,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498714,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196129/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196129",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196118,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498703,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196118/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196118",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196122,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498707,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196122/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196122",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196116,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498701,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196116/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196116",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196126,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498711,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196126/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196126",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196115,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498700,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196115/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196115",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196128,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498713,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196128/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196128",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196127,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498712,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196127/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196127",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196125,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498710,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196125/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196125",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196117,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498702,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196117/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196117",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196131,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498716,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196131/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196131",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196119,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498704,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196119/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196119",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196121,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498706,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196121/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196121",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196120,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498705,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196120/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196120",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196123,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498708,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196123/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196123",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196124,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498709,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196124/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732863/Selections/646196124",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732881,
        "externalId": 258201283,
        "name": "First or Last Tryscorer",
        "statusCode": "A",
        "sort": 435,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881",
        "selections": [
            {
                "id": 646196328,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196498831,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196328/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196328",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196333,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196498836,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196333/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196333",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196337,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196498840,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196337/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196337",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196331,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196498834,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196331/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196331",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196335,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196498838,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196335/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196335",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196324,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196498827,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196324/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196324",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196326,
                "name": "Cade Cust",
                "resultType": "-",
                "externalId": 1196498829,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196326/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196326",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196334,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196498837,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196334/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196334",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196329,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196498832,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196329/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196329",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196327,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196498830,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196327/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196327",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196322,
                "name": "Josh Alolai",
                "resultType": "-",
                "externalId": 1196498825,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196322/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196322",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196325,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196498828,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196325/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196325",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196336,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196498839,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196336/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196336",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196338,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196498841,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196338/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196338",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196330,
                "name": "Sean Keppie",
                "resultType": "-",
                "externalId": 1196498833,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196330/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196330",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196323,
                "name": "Morgan Boyle",
                "resultType": "-",
                "externalId": 1196498826,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196323/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196323",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196332,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196498835,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196332/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196332",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196356,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196498859,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196356/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196356",
                "outcomeVariants": []
            },
            {
                "id": 646196354,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196498857,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196354/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196354",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196353,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196498856,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4,
                    "winPriceNum": 3000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196353/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196353",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196342,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196498845,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196342/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196342",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196346,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196498849,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196346/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196346",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196339,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196498842,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196339/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196339",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196352,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196498855,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196352/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196352",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196351,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1196498854,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196351/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196351",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196340,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196498843,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196340/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196340",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196350,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1196498853,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196350/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196350",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196341,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196498844,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196341/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196341",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196349,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196498852,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196349/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196349",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196355,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196498858,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196355/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196355",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196343,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1196498846,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196343/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196343",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196345,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196498848,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196345/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196345",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196344,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196498847,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196344/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196344",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196347,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1196498850,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196347/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196347",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 646196348,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196498851,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196348/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732881/Selections/646196348",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732830,
        "externalId": 258201348,
        "name": "Jersey Number of First Try Scorer",
        "statusCode": "A",
        "sort": 445,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Includes extra time. Bets void if any other number scores the first try.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732830",
        "selections": [
            {
                "id": 646195752,
                "name": "Backs (No's 1, 2, 3, 4, 5, 6, 7)",
                "resultType": "-",
                "externalId": 1196500043,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.28,
                    "winPriceNum": 280,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732830/Selections/646195752/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732830/Selections/646195752",
                "outcomeVariants": []
            },
            {
                "id": 646195753,
                "name": "Forwards (No's 8, 9, 10, 11, 12, 13)",
                "resultType": "-",
                "externalId": 1196500044,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.6,
                    "winPriceNum": 2600,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732830/Selections/646195753/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732830/Selections/646195753",
                "outcomeVariants": []
            },
            {
                "id": 646195754,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196500045,
                "sort": 40,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732830/Selections/646195754/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732830/Selections/646195754",
                "outcomeVariants": []
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732844,
        "externalId": 258201350,
        "name": "Jersey Number of Home First Tryscorer",
        "statusCode": "A",
        "sort": 455,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Includes extra time. Bets void if any other number scores the first try.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732844",
        "selections": [
            {
                "id": 646195992,
                "name": "Backs (No's 1, 2, 3, 4, 5, 6, 7)",
                "resultType": "-",
                "externalId": 1196500049,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.45,
                    "winPriceNum": 450,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732844/Selections/646195992/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732844/Selections/646195992",
                "outcomeVariants": []
            },
            {
                "id": 646195993,
                "name": "Forwards (No's 8, 9, 10, 11, 12, 13)",
                "resultType": "-",
                "externalId": 1196500050,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732844/Selections/646195993/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732844/Selections/646195993",
                "outcomeVariants": []
            },
            {
                "id": 646195994,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196500051,
                "sort": 40,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732844/Selections/646195994/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732844/Selections/646195994",
                "outcomeVariants": []
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732834,
        "externalId": 258201351,
        "name": "Jersey Number of Away First Tryscorer",
        "statusCode": "A",
        "sort": 460,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Includes extra time. Bets void if any other number scores the first try.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732834",
        "selections": [
            {
                "id": 646195802,
                "name": "Backs (No's 1, 2, 3, 4, 5, 6, 7)",
                "resultType": "-",
                "externalId": 1196500052,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.28,
                    "winPriceNum": 280,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732834/Selections/646195802/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732834/Selections/646195802",
                "outcomeVariants": []
            },
            {
                "id": 646195803,
                "name": "Forwards (No's 8, 9, 10, 11, 12, 13)",
                "resultType": "-",
                "externalId": 1196500053,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.5,
                    "winPriceNum": 2500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732834/Selections/646195803/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732834/Selections/646195803",
                "outcomeVariants": []
            },
            {
                "id": 646195804,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1196500054,
                "sort": 40,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732834/Selections/646195804/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732834/Selections/646195804",
                "outcomeVariants": []
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732907,
        "externalId": 258201296,
        "name": "Most Tries - A vs B - Group 1",
        "statusCode": "A",
        "sort": 485,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732907",
        "selections": [
            {
                "id": 646196805,
                "name": "Dylan Walker",
                "resultType": "-",
                "externalId": 1196499399,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732907/Selections/646196805/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732907/Selections/646196805",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196807,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499401,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.83,
                    "winPriceNum": 830,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732907/Selections/646196807/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732907/Selections/646196807",
                "outcomeVariants": []
            },
            {
                "id": 646196806,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1196499400,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.3,
                    "winPriceNum": 1300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732907/Selections/646196806/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732907/Selections/646196806",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732821,
        "externalId": 258201297,
        "name": "Most Tries - A vs B - Group 2",
        "statusCode": "A",
        "sort": 490,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732821",
        "selections": [
            {
                "id": 646195699,
                "name": "Jason Saab",
                "resultType": "-",
                "externalId": 1196499402,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732821/Selections/646195699/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732821/Selections/646195699",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195701,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499404,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.3,
                    "winPriceNum": 1300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732821/Selections/646195701/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732821/Selections/646195701",
                "outcomeVariants": []
            },
            {
                "id": 646195700,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1196499403,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.91,
                    "winPriceNum": 910,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732821/Selections/646195700/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732821/Selections/646195700",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732838,
        "externalId": 258201298,
        "name": "Most Tries - A vs B - Group 3",
        "statusCode": "A",
        "sort": 495,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732838",
        "selections": [
            {
                "id": 646195891,
                "name": "Reuben Garrick",
                "resultType": "-",
                "externalId": 1196499405,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732838/Selections/646195891/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732838/Selections/646195891",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195893,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499407,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.4,
                    "winPriceNum": 1400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732838/Selections/646195893/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732838/Selections/646195893",
                "outcomeVariants": []
            },
            {
                "id": 646195892,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1196499406,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.91,
                    "winPriceNum": 910,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732838/Selections/646195892/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732838/Selections/646195892",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732871,
        "externalId": 258201299,
        "name": "Most Tries - A vs B - Group 4",
        "statusCode": "A",
        "sort": 500,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732871",
        "selections": [
            {
                "id": 646196230,
                "name": "Brad Parker",
                "resultType": "-",
                "externalId": 1196499408,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732871/Selections/646196230/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732871/Selections/646196230",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196232,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499410,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.57,
                    "winPriceNum": 570,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732871/Selections/646196232/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732871/Selections/646196232",
                "outcomeVariants": []
            },
            {
                "id": 646196231,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1196499409,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.88,
                    "winPriceNum": 1880,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732871/Selections/646196231/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732871/Selections/646196231",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732823,
        "externalId": 258201300,
        "name": "Most Tries - A vs B - Group 5",
        "statusCode": "A",
        "sort": 505,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732823",
        "selections": [
            {
                "id": 646195705,
                "name": "Moses Suli",
                "resultType": "-",
                "externalId": 1196499411,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732823/Selections/646195705/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732823/Selections/646195705",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195707,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499413,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.53,
                    "winPriceNum": 530,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732823/Selections/646195707/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732823/Selections/646195707",
                "outcomeVariants": []
            },
            {
                "id": 646195706,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1196499412,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 3,
                    "winPriceNum": 2000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732823/Selections/646195706/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732823/Selections/646195706",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732798,
        "externalId": 258201301,
        "name": "Most Tries - A vs B - Group 6",
        "statusCode": "A",
        "sort": 510,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732798",
        "selections": [
            {
                "id": 646195398,
                "name": "Kieran Foran",
                "resultType": "-",
                "externalId": 1196499414,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732798/Selections/646195398/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732798/Selections/646195398",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195400,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499416,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.36,
                    "winPriceNum": 360,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732798/Selections/646195400/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732798/Selections/646195400",
                "outcomeVariants": []
            },
            {
                "id": 646195399,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1196499415,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.5,
                    "winPriceNum": 2500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732798/Selections/646195399/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732798/Selections/646195399",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732885,
        "externalId": 258201302,
        "name": "Most Tries - A vs B - Group 7",
        "statusCode": "A",
        "sort": 515,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732885",
        "selections": [
            {
                "id": 646196393,
                "name": "Daly Cherry-Evans",
                "resultType": "-",
                "externalId": 1196499417,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732885/Selections/646196393/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732885/Selections/646196393",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196396,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499419,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.4,
                    "winPriceNum": 400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732885/Selections/646196396/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732885/Selections/646196396",
                "outcomeVariants": []
            },
            {
                "id": 646196394,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1196499418,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.6,
                    "winPriceNum": 2600,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732885/Selections/646196394/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732885/Selections/646196394",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732858,
        "externalId": 258201303,
        "name": "Most Tries - A vs B - Group 8",
        "statusCode": "A",
        "sort": 520,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732858",
        "selections": [
            {
                "id": 646196085,
                "name": "Taniela Paseka",
                "resultType": "-",
                "externalId": 1196499420,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732858/Selections/646196085/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732858/Selections/646196085",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196087,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499422,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.08,
                    "winPriceNum": 80,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732858/Selections/646196087/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732858/Selections/646196087",
                "outcomeVariants": []
            },
            {
                "id": 646196086,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1196499421,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732858/Selections/646196086/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732858/Selections/646196086",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732850,
        "externalId": 258201304,
        "name": "Most Tries - A vs B - Group 9",
        "statusCode": "A",
        "sort": 525,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732850",
        "selections": [
            {
                "id": 646196029,
                "name": "Martin Taupau",
                "resultType": "-",
                "externalId": 1196499423,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732850/Selections/646196029/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732850/Selections/646196029",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196031,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499425,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.12,
                    "winPriceNum": 120,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732850/Selections/646196031/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732850/Selections/646196031",
                "outcomeVariants": []
            },
            {
                "id": 646196030,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1196499424,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732850/Selections/646196030/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732850/Selections/646196030",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732870,
        "externalId": 258201305,
        "name": "Most Tries - A vs B - Group 10",
        "statusCode": "A",
        "sort": 530,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732870",
        "selections": [
            {
                "id": 646196227,
                "name": "Lachlan Croker",
                "resultType": "-",
                "externalId": 1196499426,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732870/Selections/646196227/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732870/Selections/646196227",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196229,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499428,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.2,
                    "winPriceNum": 200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732870/Selections/646196229/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732870/Selections/646196229",
                "outcomeVariants": []
            },
            {
                "id": 646196228,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1196499427,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732870/Selections/646196228/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732870/Selections/646196228",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732902,
        "externalId": 258201306,
        "name": "Most Tries - A vs B - Group 11",
        "statusCode": "A",
        "sort": 535,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732902",
        "selections": [
            {
                "id": 646196676,
                "name": "Jack Gosiewski",
                "resultType": "-",
                "externalId": 1196499429,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732902/Selections/646196676/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732902/Selections/646196676",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646196678,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499431,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.67,
                    "winPriceNum": 670,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732902/Selections/646196678/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732902/Selections/646196678",
                "outcomeVariants": []
            },
            {
                "id": 646196677,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1196499430,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.3,
                    "winPriceNum": 1300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732902/Selections/646196677/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732902/Selections/646196677",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732811,
        "externalId": 258201307,
        "name": "Most Tries - A vs B - Group 12",
        "statusCode": "A",
        "sort": 540,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732811",
        "selections": [
            {
                "id": 646195513,
                "name": "Joshua Schuster",
                "resultType": "-",
                "externalId": 1196499432,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732811/Selections/646195513/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732811/Selections/646195513",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195515,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499434,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.4,
                    "winPriceNum": 400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732811/Selections/646195515/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732811/Selections/646195515",
                "outcomeVariants": []
            },
            {
                "id": 646195514,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1196499433,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.3,
                    "winPriceNum": 2300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732811/Selections/646195514/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732811/Selections/646195514",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121732812,
        "externalId": 258201308,
        "name": "Most Tries - A vs B - Group 13",
        "statusCode": "A",
        "sort": 545,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732812",
        "selections": [
            {
                "id": 646195516,
                "name": "Jake Trbojevic",
                "resultType": "-",
                "externalId": 1196499435,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732812/Selections/646195516/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732812/Selections/646195516",
                "outcomeVariants": [],
                "multiplesKey": "manlyseaeaglrl"
            },
            {
                "id": 646195518,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1196499437,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.2,
                    "winPriceNum": 200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732812/Selections/646195518/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732812/Selections/646195518",
                "outcomeVariants": []
            },
            {
                "id": 646195517,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1196499436,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732812/Selections/646195517/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5745273/Markets/121732812/Selections/646195517",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    }
]
'''
# In the code below I am tranforming the JSON content in a python content.
# So I can work with it tranforming it in either dictonaries or lists
data = json.loads(markets_in_json)

# here we are just checking what kind of data we have received from the JSON content. It will be a lists
# print("----------------")
# print()
# print()
# print("JSON content data type and length: ")
# print(type(data))
# print(len(data))
# print("----------------")
# print()

# converting the first index of the list in a dictionary, where I can find the First Tryscorer data.
first_tryscorer_dict = dict(data[0])
print("First Tryscorer data type and length: ")
print(type(first_tryscorer_dict))
print(len(first_tryscorer_dict))
print("----------------")
print()
# converting the second index of the list in a dictionary, where I can find the Anytime Tryscorer data.
anytime_tryscorer_dict = dict(data[1])
print("Anytime Scorer data type and length: ")
print(type(anytime_tryscorer_dict))
print(len(anytime_tryscorer_dict))
print("----------------")
print()

# Here I am printing the data keys of the dictionary so I know how to access the data I want.
# In this case, I will want to access the data NAME that gives me the ANYTIME SCORER, however, it will be a list nested wich I will have to treat later
# print("Anytime Scorer keys: ")
# print(anytime_tryscorer_dict.keys())
# print("----------------")
# print()

# Accessing the NAME key where it will show what MARKET I am printing
print("NAME SELECTION: ")
print(anytime_tryscorer_dict.get("name"))

# print(anytime_tryscorer_dict.get("selections"))

# As said before, I need to get the list nested and transform in a dictionary. So I can access the data.Here I am checking what I have inside the "selections" key and after I am tranforming in a python dict
anytime_tryscrore = anytime_tryscorer_dict.get("selections")
# print(type(anytime_tryscrore))
# print(len(anytime_tryscrore))


# Here I am trying the first index of the dict, that will give me the first player. The idea is to check so I can later just
# do a loop to get those
dictionary_values_of_tryscorer = dict(anytime_tryscrore[0])
# print("Type of dictionary_values_of_tryscorer: ")
# print(type(dictionary_values_of_tryscorer))
# print(dictionary_values_of_tryscorer)
print(dictionary_values_of_tryscorer.get("name"))
# print(dictionary_values_of_tryscorer.get("price"))
new_dict = dict(dictionary_values_of_tryscorer.get("price"))
print(new_dict.get("winPrice"))
# print(dictionary_values_of_tryscorer.get("price"))
print()
print("----------------")
print()


print()
print("----------------")
print()
print("---------------------STOP HERE!!!!!!!--------------------------")
print()
print("----------------")
print()
dictionary_values_of_tryscorer = dict(anytime_tryscrore[1])
# print("Type of dictionary_values_of_tryscorer: ")
# print(type(dictionary_values_of_tryscorer))
# print(dictionary_values_of_tryscorer)
print(dictionary_values_of_tryscorer.get("name"))
# print(dictionary_values_of_tryscorer.get("price"))
new_dict = dict(dictionary_values_of_tryscorer.get("price"))
print(new_dict.get("winPrice"))
# print(dictionary_values_of_tryscorer.get("price"))
print()
print("----------------")
print()

dictionary_values_of_tryscorer = dict(anytime_tryscrore[2])
# print("Type of dictionary_values_of_tryscorer: ")
# print(type(dictionary_values_of_tryscorer))
# print(dictionary_values_of_tryscorer)
print(dictionary_values_of_tryscorer.get("name"))
# print(dictionary_values_of_tryscorer.get("price"))
new_dict = dict(dictionary_values_of_tryscorer.get("price"))
print(new_dict.get("winPrice"))
# print(dictionary_values_of_tryscorer.get("price"))
print()
print("----------------")
print()


dictionary_values_of_tryscorer = dict(anytime_tryscrore[3])
# print("Type of dictionary_values_of_tryscorer: ")
# print(type(dictionary_values_of_tryscorer))
# print(dictionary_values_of_tryscorer)
print(dictionary_values_of_tryscorer.get("name"))
# print(dictionary_values_of_tryscorer.get("price"))
new_dict = dict(dictionary_values_of_tryscorer.get("price"))
print(new_dict.get("winPrice"))
# print(dictionary_values_of_tryscorer.get("price"))
print()
print("----------------")
print()

# There is another nested dictionary in the dict, so we have to transforme the list returned to a dict and then get
# the data we want that will be in WinPrice
# new_dict = dict(dictionary_values_of_tryscorer.get("price"))
# print(new_dict.get("winPrice"))
# print(type(new_dict))
# # print(new_dict.get("price"))
# print()
# print("----------------")
# print()
