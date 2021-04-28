import json

# MARKETS for Camberra
# Date released: 28/04/2021
# SportsBet website

# Data in Json
markets_in_json = '''[
    {
        "id": 123747597,
        "externalId": 261773082,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597",
        "selections": [
            {
                "id": 656182403,
                "name": "Jordan Rapana",
                "resultType": "H",
                "externalId": 1214910417,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182403/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182403",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182405,
                "name": "Bailey Simonsson",
                "resultType": "H",
                "externalId": 1214910419,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182405/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182405",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182410,
                "name": "Jack Wighton",
                "resultType": "H",
                "externalId": 1214910424,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182410/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182410",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182404,
                "name": "Curtis Scott",
                "resultType": "H",
                "externalId": 1214910418,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182404/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182404",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182413,
                "name": "Sebastian Kris",
                "resultType": "H",
                "externalId": 1214910427,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182413/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182413",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182397,
                "name": "Caleb Aekins",
                "resultType": "H",
                "externalId": 1214910411,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182397/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182397",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182411,
                "name": "George Williams",
                "resultType": "H",
                "externalId": 1214910425,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182411/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182411",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182399,
                "name": "Corey Harawira-Naera",
                "resultType": "H",
                "externalId": 1214910413,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182399/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182399",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182409,
                "name": "Elliott Whitehead",
                "resultType": "H",
                "externalId": 1214910423,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182409/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182409",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182412,
                "name": "Hudson Young",
                "resultType": "H",
                "externalId": 1214910426,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182412/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182412",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182408,
                "name": "Joseph Tapine",
                "resultType": "H",
                "externalId": 1214910422,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182408/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182408",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182400,
                "name": "Siliva Havili",
                "resultType": "H",
                "externalId": 1214910414,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182400/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182400",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182406,
                "name": "Tom Starling",
                "resultType": "H",
                "externalId": 1214910420,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182406/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182406",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182402,
                "name": "Ryan James",
                "resultType": "H",
                "externalId": 1214910416,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182402/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182402",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182401,
                "name": "Corey Horsburgh",
                "resultType": "H",
                "externalId": 1214910415,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182401/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182401",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182407,
                "name": "Ryan Sutton",
                "resultType": "H",
                "externalId": 1214910421,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182407/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182407",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182398,
                "name": "Emre Guler",
                "resultType": "H",
                "externalId": 1214910412,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182398/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182398",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182420,
                "name": "Alex Johnston",
                "resultType": "A",
                "externalId": 1214910434,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182420/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182420",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182426,
                "name": "Jaxson Paulo",
                "resultType": "A",
                "externalId": 1214910440,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182426/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182426",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182430,
                "name": "Cody Walker",
                "resultType": "A",
                "externalId": 1214910444,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182430/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182430",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182417,
                "name": "Dane Gagai",
                "resultType": "A",
                "externalId": 1214910431,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182417/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182417",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182418,
                "name": "Campbell Graham",
                "resultType": "A",
                "externalId": 1214910432,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182418/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182418",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182423,
                "name": "Benji Marshall",
                "resultType": "A",
                "externalId": 1214910437,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182423/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182423",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182416,
                "name": "Damien Cook",
                "resultType": "A",
                "externalId": 1214910430,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182416/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182416",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182427,
                "name": "Adam Reynolds",
                "resultType": "A",
                "externalId": 1214910441,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182427/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182427",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182424,
                "name": "Cameron Murray",
                "resultType": "A",
                "externalId": 1214910438,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182424/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182424",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182414,
                "name": "Jai Arrow",
                "resultType": "A",
                "externalId": 1214910428,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182414/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182414",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182422,
                "name": "Keaon Koloamatangi",
                "resultType": "A",
                "externalId": 1214910436,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182422/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182422",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182419,
                "name": "Jacob Host",
                "resultType": "A",
                "externalId": 1214910433,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182419/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182419",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182428,
                "name": "Jaydn Su'A",
                "resultType": "A",
                "externalId": 1214910442,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182428/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182428",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182421,
                "name": "Liam Knight",
                "resultType": "A",
                "externalId": 1214910435,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182421/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182421",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182425,
                "name": "Mark Nicholls",
                "resultType": "A",
                "externalId": 1214910439,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182425/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182425",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182429,
                "name": "Tevita Tatola",
                "resultType": "A",
                "externalId": 1214910443,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182429/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182429",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182415,
                "name": "Thomas Burgess",
                "resultType": "A",
                "externalId": 1214910429,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182415/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747597/Selections/656182415",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747605,
        "externalId": 261773085,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605",
        "selections": [
            {
                "id": 656182682,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910524,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.4,
                    "winPriceNum": 1400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182682/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182682",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182680,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910522,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 2,
                    "winPriceNum": 1000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182680/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182680",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182687,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910529,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3,
                    "winPriceNum": 2000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182687/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182687",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182674,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910516,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182674/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182674",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182681,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910523,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182681/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182681",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182688,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910530,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182688/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182688",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182690,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910532,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4,
                    "winPriceNum": 3000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182690/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182690",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182676,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910518,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182676/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182676",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182686,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910528,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182686/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182686",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182689,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910531,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182689/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182689",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182685,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910527,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182685/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182685",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182677,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910519,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182677/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182677",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182683,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910525,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182683/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182683",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182678,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910520,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182678/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182678",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182675,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910517,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182675/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182675",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182679,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910521,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182679/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182679",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182684,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910526,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182684/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182684",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182697,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910539,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.67,
                    "winPriceNum": 670,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182697/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182697",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182707,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910549,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.2,
                    "winPriceNum": 1200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182707/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182707",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182694,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910536,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.88,
                    "winPriceNum": 1880,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182694/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182694",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182703,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910545,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2,
                    "winPriceNum": 1000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182703/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182703",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182695,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910537,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.25,
                    "winPriceNum": 2250,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182695/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182695",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182704,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910546,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182704/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182704",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182700,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910542,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.2,
                    "winPriceNum": 3200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182700/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182700",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182701,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910543,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182701/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182701",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182693,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910535,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.33,
                    "winPriceNum": 3330,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182693/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182693",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182691,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910533,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182691/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182691",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182699,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910541,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182699/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182699",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182696,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910538,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182696/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182696",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182705,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910547,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182705/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182705",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182698,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910540,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182698/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182698",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182692,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910534,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182692/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182692",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182702,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910544,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182702/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182702",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182706,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910548,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182706/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747605/Selections/656182706",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747607,
        "externalId": 261773088,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607",
        "selections": [
            {
                "id": 656182732,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910624,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182732/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182732",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182734,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910626,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182734/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182734",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182739,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910631,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182739/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182739",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182744,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910634,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182744/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182744",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182733,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910625,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182733/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182733",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182726,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910618,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182726/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182726",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182738,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910630,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182738/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182738",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182737,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910629,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182737/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182737",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182741,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910632,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182741/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182741",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182728,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910620,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182728/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182728",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182743,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910633,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182743/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182743",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182729,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910621,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182729/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182729",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182735,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910627,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182735/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182735",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182730,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910622,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182730/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182730",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182727,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910619,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182727/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182727",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182736,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910628,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182736/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182736",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182731,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910623,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182731/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182731",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182751,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910641,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.2,
                    "winPriceNum": 3200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182751/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182751",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182759,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910647,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182759/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182759",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182764,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910651,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182764/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182764",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182748,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910638,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182748/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182748",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182749,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910639,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182749/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182749",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182755,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910644,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182755/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182755",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182747,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910637,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182747/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182747",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182760,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910648,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182760/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182760",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182745,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910635,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182745/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182745",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182753,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910643,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182753/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182753",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182757,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910645,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182757/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182757",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182750,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910640,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182750/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182750",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182761,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910649,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182761/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182761",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182752,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910642,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182752/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182752",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182746,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910636,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182746/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182746",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182758,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910646,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182758/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182758",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182763,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910650,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182763/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747607/Selections/656182763",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747599,
        "externalId": 261773089,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599",
        "selections": [
            {
                "id": 656182472,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910658,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182472/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182472",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182474,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910660,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182474/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182474",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182479,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910665,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182479/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182479",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182482,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910668,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182482/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182482",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182473,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910659,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182473/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182473",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182480,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910666,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182480/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182480",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182466,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910652,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182466/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182466",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182468,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910654,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182468/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182468",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182470,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910656,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182470/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182470",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182478,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910664,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182478/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182478",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182467,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910653,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182467/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182467",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182481,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910667,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182481/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182481",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182477,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910663,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182477/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182477",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182471,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910657,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182471/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182471",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182476,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910662,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182476/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182476",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182469,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910655,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182469/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182469",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182475,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910661,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182475/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182475",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182489,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910675,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182489/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182489",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182495,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910681,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182495/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182495",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182499,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910685,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182499/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182499",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182486,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910672,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182486/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182486",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182487,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910673,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182487/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182487",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182492,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910678,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182492/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182492",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182485,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910671,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182485/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182485",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182496,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910682,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182496/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182496",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182493,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910679,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182493/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182493",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182483,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910669,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182483/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182483",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182488,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910674,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182488/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182488",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182497,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910683,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182497/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182497",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182491,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910677,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182491/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182491",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182490,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910676,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182490/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182490",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182494,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910680,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182494/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182494",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182498,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910684,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182498/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182498",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182484,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910670,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182484/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747599/Selections/656182484",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747671,
        "externalId": 261773320,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671",
        "selections": [
            {
                "id": 656183633,
                "name": "Alex Johnston to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912424,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2,
                    "winPriceNum": 1000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183633/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183633",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183643,
                "name": "Cody Walker to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912434,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.7,
                    "winPriceNum": 1700,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183643/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183643",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183639,
                "name": "Jaxson Paulo to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912430,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.4,
                    "winPriceNum": 1400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183639/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183639",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183631,
                "name": "Campbell Graham to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912422,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183631/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183631",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183630,
                "name": "Dane Gagai to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912421,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.4,
                    "winPriceNum": 2400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183630/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183630",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183616,
                "name": "Jordan Rapana to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912407,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.6,
                    "winPriceNum": 2600,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183616/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183616",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183650,
                "name": "Jordan Rapana to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912441,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.4,
                    "winPriceNum": 2400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183650/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183650",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183618,
                "name": "Bailey Simonsson to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912409,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.33,
                    "winPriceNum": 3330,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183618/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183618",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183652,
                "name": "Bailey Simonsson to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912443,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4,
                    "winPriceNum": 3000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183652/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183652",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183636,
                "name": "Benji Marshall to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912427,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183636/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183636",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183629,
                "name": "Damien Cook to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912420,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183629/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183629",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183657,
                "name": "Jack Wighton to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912448,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183657/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183657",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183640,
                "name": "Adam Reynolds to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912431,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183640/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183640",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183599,
                "name": "Alex Johnston to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912390,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183599/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183599",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183637,
                "name": "Cameron Murray to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912428,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183637/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183637",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183623,
                "name": "Jack Wighton to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912414,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183623/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183623",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183627,
                "name": "Jai Arrow to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912418,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183627/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183627",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183635,
                "name": "Keaon Koloamatangi to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912426,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183635/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183635",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183609,
                "name": "Cody Walker to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912400,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183609/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183609",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183617,
                "name": "Curtis Scott to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912408,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183617/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183617",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183651,
                "name": "Curtis Scott to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912442,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183651/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183651",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183632,
                "name": "Jacob Host to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912423,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183632/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183632",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183605,
                "name": "Jaxson Paulo to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912396,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183605/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183605",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183641,
                "name": "Jaydn Su'A to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912432,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183641/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183641",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183626,
                "name": "Sebastian Kris to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912417,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183626/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183626",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183660,
                "name": "Sebastian Kris to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912451,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183660/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183660",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183610,
                "name": "Caleb Aekins to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912401,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183610/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183610",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183644,
                "name": "Caleb Aekins to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912435,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183644/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183644",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183612,
                "name": "Corey Harawira-Naera to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912403,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183612/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183612",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183646,
                "name": "Corey Harawira-Naera to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912437,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183646/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183646",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183622,
                "name": "Elliott Whitehead to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912413,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183622/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183622",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183656,
                "name": "Elliott Whitehead to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912447,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183656/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183656",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183624,
                "name": "George Williams to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912415,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183624/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183624",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183658,
                "name": "George Williams to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912449,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183658/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183658",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183625,
                "name": "Hudson Young to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912416,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183625/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183625",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183659,
                "name": "Hudson Young to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912450,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183659/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183659",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183621,
                "name": "Joseph Tapine to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912412,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183621/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183621",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183655,
                "name": "Joseph Tapine to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912446,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183655/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183655",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183596,
                "name": "Dane Gagai to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912387,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183596/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183596",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183634,
                "name": "Liam Knight to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912425,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183634/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183634",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183613,
                "name": "Siliva Havili to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912404,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183613/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183613",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183647,
                "name": "Siliva Havili to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912438,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183647/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183647",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183628,
                "name": "Thomas Burgess to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912419,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183628/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183628",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183619,
                "name": "Tom Starling to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912410,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183619/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183619",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183653,
                "name": "Tom Starling to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912444,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183653/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183653",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183597,
                "name": "Campbell Graham to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912388,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183597/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183597",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183638,
                "name": "Mark Nicholls to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912429,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183638/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183638",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183642,
                "name": "Tevita Tatola to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912433,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183642/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183642",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183602,
                "name": "Benji Marshall to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912393,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183602/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183602",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183614,
                "name": "Corey Horsburgh to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912405,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183614/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183614",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183595,
                "name": "Damien Cook to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912386,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183595/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183595",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183620,
                "name": "Ryan Sutton to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912411,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183620/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183620",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183606,
                "name": "Adam Reynolds to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912397,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183606/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183606",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183603,
                "name": "Cameron Murray to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912394,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183603/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183603",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183648,
                "name": "Corey Horsburgh to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912439,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183648/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183648",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183611,
                "name": "Emre Guler to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912402,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183611/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183611",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183593,
                "name": "Jai Arrow to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912384,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183593/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183593",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183615,
                "name": "Ryan James to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912406,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183615/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183615",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183649,
                "name": "Ryan James to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912440,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183649/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183649",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183654,
                "name": "Ryan Sutton to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912445,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183654/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183654",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183645,
                "name": "Emre Guler to score a try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912436,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183645/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183645",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183601,
                "name": "Keaon Koloamatangi to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912392,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183601/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183601",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183598,
                "name": "Jacob Host to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912389,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183598/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183598",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183607,
                "name": "Jaydn Su'A to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912398,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183607/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183607",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183600,
                "name": "Liam Knight to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912391,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183600/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183600",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183594,
                "name": "Thomas Burgess to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912385,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183594/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183594",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183604,
                "name": "Mark Nicholls to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912395,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183604/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183604",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183608,
                "name": "Tevita Tatola to score a try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912399,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183608/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747671/Selections/656183608",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747643,
        "externalId": 261773321,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643",
        "selections": [
            {
                "id": 656183316,
                "name": "Alex Johnston to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912492,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183316/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183316",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183322,
                "name": "Jaxson Paulo to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912498,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183322/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183322",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183326,
                "name": "Cody Walker to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912502,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183326/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183326",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183299,
                "name": "Jordan Rapana to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912475,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183299/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183299",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183313,
                "name": "Dane Gagai to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912489,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183313/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183313",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183333,
                "name": "Jordan Rapana to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912509,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183333/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183333",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183314,
                "name": "Campbell Graham to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912490,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183314/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183314",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183301,
                "name": "Bailey Simonsson to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912477,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183301/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183301",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183335,
                "name": "Bailey Simonsson to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912511,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183335/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183335",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183323,
                "name": "Adam Reynolds to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912499,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183323/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183323",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183282,
                "name": "Alex Johnston to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912458,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183282/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183282",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183319,
                "name": "Benji Marshall to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912495,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183319/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183319",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183312,
                "name": "Damien Cook to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912488,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183312/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183312",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183306,
                "name": "Jack Wighton to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912482,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183306/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183306",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183340,
                "name": "Jack Wighton to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912516,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183340/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183340",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183310,
                "name": "Jai Arrow to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912486,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183310/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183310",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183318,
                "name": "Keaon Koloamatangi to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912494,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183318/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183318",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183320,
                "name": "Cameron Murray to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912496,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183320/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183320",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183300,
                "name": "Curtis Scott to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912476,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183300/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183300",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183309,
                "name": "Sebastian Kris to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912485,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183309/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183309",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183293,
                "name": "Caleb Aekins to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912469,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183293/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183293",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183292,
                "name": "Cody Walker to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912468,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183292/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183292",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183307,
                "name": "George Williams to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912483,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183307/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183307",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183315,
                "name": "Jacob Host to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912491,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183315/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183315",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183288,
                "name": "Jaxson Paulo to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912464,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183288/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183288",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183324,
                "name": "Jaydn Su'A to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912500,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183324/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183324",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183327,
                "name": "Caleb Aekins to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912503,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183327/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183327",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183334,
                "name": "Curtis Scott to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912510,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183334/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183334",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183341,
                "name": "George Williams to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912517,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183341/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183341",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183343,
                "name": "Sebastian Kris to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912519,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183343/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183343",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183295,
                "name": "Corey Harawira-Naera to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912471,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183295/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183295",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183329,
                "name": "Corey Harawira-Naera to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912505,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183329/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183329",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183305,
                "name": "Elliott Whitehead to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912481,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183305/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183305",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183308,
                "name": "Hudson Young to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912484,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183308/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183308",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183342,
                "name": "Hudson Young to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912518,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183342/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183342",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183304,
                "name": "Joseph Tapine to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912480,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183304/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183304",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183279,
                "name": "Dane Gagai to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912455,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183279/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183279",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183339,
                "name": "Elliott Whitehead to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912515,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183339/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183339",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183338,
                "name": "Joseph Tapine to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912514,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183338/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183338",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183296,
                "name": "Siliva Havili to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912472,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183296/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183296",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183302,
                "name": "Tom Starling to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912478,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183302/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183302",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183317,
                "name": "Liam Knight to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912493,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183317/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183317",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183311,
                "name": "Thomas Burgess to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912487,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183311/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183311",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183321,
                "name": "Mark Nicholls to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912497,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183321/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183321",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183325,
                "name": "Tevita Tatola to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912501,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183325/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183325",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183280,
                "name": "Campbell Graham to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912456,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183280/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183280",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183286,
                "name": "Cameron Murray to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912462,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183286/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183286",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183297,
                "name": "Corey Horsburgh to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912473,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183297/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183297",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183298,
                "name": "Ryan James to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912474,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183298/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183298",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183303,
                "name": "Ryan Sutton to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912479,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183303/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183303",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183330,
                "name": "Siliva Havili to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912506,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183330/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183330",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183336,
                "name": "Tom Starling to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912512,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183336/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183336",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183285,
                "name": "Benji Marshall to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912461,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183285/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183285",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183332,
                "name": "Ryan James to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912508,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183332/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183332",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183289,
                "name": "Adam Reynolds to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912465,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183289/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183289",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183278,
                "name": "Damien Cook to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912454,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183278/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183278",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183294,
                "name": "Emre Guler to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912470,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183294/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183294",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183276,
                "name": "Jai Arrow to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912452,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183276/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183276",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183331,
                "name": "Corey Horsburgh to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912507,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183331/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183331",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183328,
                "name": "Emre Guler to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912504,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183328/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183328",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183281,
                "name": "Jacob Host to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912457,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183281/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183281",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183290,
                "name": "Jaydn Su'A to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912466,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183290/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183290",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183284,
                "name": "Keaon Koloamatangi to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912460,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183284/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183284",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183337,
                "name": "Ryan Sutton to score the first try and South Sydney Rabbitohs to win",
                "resultType": "-",
                "externalId": 1214912513,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183337/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183337",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183283,
                "name": "Liam Knight to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912459,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183283/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183283",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183287,
                "name": "Mark Nicholls to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912463,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183287/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183287",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183291,
                "name": "Tevita Tatola to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912467,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183291/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183291",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183277,
                "name": "Thomas Burgess to score the first try and Canberra Raiders to win",
                "resultType": "-",
                "externalId": 1214912453,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183277/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747643/Selections/656183277",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747603,
        "externalId": 261773086,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603",
        "selections": [
            {
                "id": 656182611,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910556,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.4,
                    "winPriceNum": 2400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182611/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182611",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182613,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910558,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.33,
                    "winPriceNum": 3330,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182613/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182613",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182618,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910563,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182618/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182618",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182605,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910550,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182605/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182605",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182612,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910557,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182612/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182612",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182621,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910566,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182621/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182621",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182607,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910552,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182607/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182607",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182619,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910564,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182619/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182619",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182620,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910565,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182620/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182620",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182617,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910562,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182617/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182617",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182616,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910561,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182616/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182616",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182608,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910553,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182608/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182608",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182614,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910559,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182614/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182614",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182609,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910554,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182609/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182609",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182615,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910560,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182615/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182615",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182606,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910551,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182606/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182606",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182610,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910555,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182610/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182610",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182628,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910573,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.7,
                    "winPriceNum": 1700,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182628/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182628",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182638,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910583,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182638/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182638",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182634,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910579,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.3,
                    "winPriceNum": 2300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182634/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182634",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182626,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910571,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182626/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182626",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182625,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910570,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182625/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182625",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182631,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910576,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182631/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182631",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182624,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910569,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182624/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182624",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182635,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910580,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182635/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182635",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182632,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910577,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182632/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182632",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182622,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910567,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182622/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182622",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182630,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910575,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182630/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182630",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182627,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910572,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182627/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182627",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182636,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910581,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182636/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182636",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182629,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910574,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182629/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182629",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182623,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910568,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182623/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182623",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182633,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910578,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182633/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182633",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182637,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910582,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182637/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747603/Selections/656182637",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747604,
        "externalId": 261773093,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604",
        "selections": [
            {
                "id": 656182645,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910763,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182645/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182645",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182647,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910765,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182647/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182647",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182652,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910770,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182652/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182652",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182655,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910773,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182655/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182655",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182639,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910757,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182639/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182639",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182641,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910759,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182641/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182641",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182646,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910764,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182646/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182646",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182651,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910769,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182651/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182651",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182653,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910771,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182653/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182653",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182654,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910772,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182654/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182654",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182650,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910768,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182650/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182650",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182642,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910760,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182642/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182642",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182648,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910766,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182648/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182648",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182643,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910761,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182643/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182643",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182649,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910767,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182649/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182649",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182640,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910758,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182640/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182640",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182644,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910762,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182644/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182644",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182673,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214910791,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182673/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182673",
                "outcomeVariants": []
            },
            {
                "id": 656182662,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910780,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182662/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182662",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182668,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910786,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182668/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182668",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182672,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910790,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182672/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182672",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182659,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910777,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182659/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182659",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182660,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910778,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182660/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182660",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182665,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910783,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182665/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182665",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182669,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910787,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182669/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182669",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182666,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910784,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182666/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182666",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182658,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910776,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182658/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182658",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182656,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910774,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182656/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182656",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182661,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910779,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182661/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182661",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182670,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910788,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182670/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182670",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182664,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910782,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182664/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182664",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182663,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910781,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182663/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182663",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182657,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910775,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182657/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182657",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182667,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910785,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182667/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182667",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182671,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910789,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182671/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747604/Selections/656182671",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747703,
        "externalId": 261773298,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703",
        "selections": [
            {
                "id": 656183858,
                "name": "1st: Alex Johnston, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912110,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183858/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183858",
                "outcomeVariants": []
            },
            {
                "id": 656183868,
                "name": "1st: Jaxson Paulo, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912120,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183868/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183868",
                "outcomeVariants": []
            },
            {
                "id": 656183859,
                "name": "1st: Alex Johnston, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912111,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183859/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183859",
                "outcomeVariants": []
            },
            {
                "id": 656183898,
                "name": "1st: Jordan Rapana, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912154,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183898/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183898",
                "outcomeVariants": []
            },
            {
                "id": 656183862,
                "name": "1st: Alex Johnston, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912114,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183862/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183862",
                "outcomeVariants": []
            },
            {
                "id": 656183879,
                "name": "1st: Cody Walker, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912131,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183879/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183879",
                "outcomeVariants": []
            },
            {
                "id": 656183878,
                "name": "1st: Cody Walker, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912130,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183878/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183878",
                "outcomeVariants": []
            },
            {
                "id": 656183838,
                "name": "1st: Dane Gagai, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912090,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183838/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183838",
                "outcomeVariants": []
            },
            {
                "id": 656183869,
                "name": "1st: Jaxson Paulo, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912121,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183869/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183869",
                "outcomeVariants": []
            },
            {
                "id": 656183872,
                "name": "1st: Jaxson Paulo, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912124,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183872/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183872",
                "outcomeVariants": []
            },
            {
                "id": 656183864,
                "name": "1st: Alex Johnston, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912116,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183864/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183864",
                "outcomeVariants": []
            },
            {
                "id": 656183860,
                "name": "1st: Alex Johnston, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912112,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183860/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183860",
                "outcomeVariants": []
            },
            {
                "id": 656183918,
                "name": "1st: Bailey Simonsson, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912180,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183918/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183918",
                "outcomeVariants": []
            },
            {
                "id": 656183882,
                "name": "1st: Cody Walker, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912134,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183882/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183882",
                "outcomeVariants": []
            },
            {
                "id": 656183870,
                "name": "1st: Jaxson Paulo, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912122,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183870/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183870",
                "outcomeVariants": []
            },
            {
                "id": 656183899,
                "name": "1st: Jordan Rapana, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912157,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183899/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183899",
                "outcomeVariants": []
            },
            {
                "id": 656183902,
                "name": "1st: Jordan Rapana, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912162,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183902/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183902",
                "outcomeVariants": []
            },
            {
                "id": 656183856,
                "name": "1st: Alex Johnston, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912108,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183856/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183856",
                "outcomeVariants": []
            },
            {
                "id": 656183919,
                "name": "1st: Bailey Simonsson, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912181,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183919/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183919",
                "outcomeVariants": []
            },
            {
                "id": 656183848,
                "name": "1st: Campbell Graham, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912100,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183848/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183848",
                "outcomeVariants": []
            },
            {
                "id": 656183880,
                "name": "1st: Cody Walker, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912132,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183880/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183880",
                "outcomeVariants": []
            },
            {
                "id": 656183874,
                "name": "1st: Jaxson Paulo, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912126,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183874/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183874",
                "outcomeVariants": []
            },
            {
                "id": 656183904,
                "name": "1st: Jordan Rapana, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912164,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183904/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183904",
                "outcomeVariants": []
            },
            {
                "id": 656183900,
                "name": "1st: Jordan Rapana, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912158,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183900/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183900",
                "outcomeVariants": []
            },
            {
                "id": 656183857,
                "name": "1st: Alex Johnston, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912109,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183857/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183857",
                "outcomeVariants": []
            },
            {
                "id": 656183924,
                "name": "1st: Bailey Simonsson, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912190,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183924/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183924",
                "outcomeVariants": []
            },
            {
                "id": 656183922,
                "name": "1st: Bailey Simonsson, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912188,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183922/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183922",
                "outcomeVariants": []
            },
            {
                "id": 656183850,
                "name": "1st: Campbell Graham, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912102,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183850/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183850",
                "outcomeVariants": []
            },
            {
                "id": 656183908,
                "name": "1st: Curtis Scott, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912168,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183908/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183908",
                "outcomeVariants": []
            },
            {
                "id": 656183844,
                "name": "1st: Dane Gagai, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912096,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183844/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183844",
                "outcomeVariants": []
            },
            {
                "id": 656183839,
                "name": "1st: Dane Gagai, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912091,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183839/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183839",
                "outcomeVariants": []
            },
            {
                "id": 656183866,
                "name": "1st: Jaxson Paulo, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912118,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183866/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183866",
                "outcomeVariants": []
            },
            {
                "id": 656183896,
                "name": "1st: Jordan Rapana, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912150,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183896/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183896",
                "outcomeVariants": []
            },
            {
                "id": 656183865,
                "name": "1st: Alex Johnston, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912117,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183865/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183865",
                "outcomeVariants": []
            },
            {
                "id": 656183849,
                "name": "1st: Campbell Graham, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912101,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183849/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183849",
                "outcomeVariants": []
            },
            {
                "id": 656183876,
                "name": "1st: Cody Walker, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912128,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183876/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183876",
                "outcomeVariants": []
            },
            {
                "id": 656183842,
                "name": "1st: Dane Gagai, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912094,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183842/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183842",
                "outcomeVariants": []
            },
            {
                "id": 656183867,
                "name": "1st: Jaxson Paulo, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912119,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183867/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183867",
                "outcomeVariants": []
            },
            {
                "id": 656183897,
                "name": "1st: Jordan Rapana, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912153,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183897/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183897",
                "outcomeVariants": []
            },
            {
                "id": 656183928,
                "name": "1st: Sebastian Kris, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912194,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183928/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183928",
                "outcomeVariants": []
            },
            {
                "id": 656183863,
                "name": "1st: Alex Johnston, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912115,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183863/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183863",
                "outcomeVariants": []
            },
            {
                "id": 656183917,
                "name": "1st: Bailey Simonsson, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912179,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183917/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183917",
                "outcomeVariants": []
            },
            {
                "id": 656183920,
                "name": "1st: Bailey Simonsson, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912184,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183920/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183920",
                "outcomeVariants": []
            },
            {
                "id": 656183888,
                "name": "1st: Caleb Aekins, 2nd: Alex Johnston",
                "resultType": "-",
                "externalId": 1214912140,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183888/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183888",
                "outcomeVariants": []
            },
            {
                "id": 656183892,
                "name": "1st: Caleb Aekins, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912146,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183892/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183892",
                "outcomeVariants": []
            },
            {
                "id": 656183852,
                "name": "1st: Campbell Graham, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912104,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183852/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183852",
                "outcomeVariants": []
            },
            {
                "id": 656183884,
                "name": "1st: Cody Walker, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912136,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183884/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183884",
                "outcomeVariants": []
            },
            {
                "id": 656183877,
                "name": "1st: Cody Walker, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912129,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183877/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183877",
                "outcomeVariants": []
            },
            {
                "id": 656183840,
                "name": "1st: Dane Gagai, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912092,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183840/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183840",
                "outcomeVariants": []
            },
            {
                "id": 656183903,
                "name": "1st: Jordan Rapana, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912163,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183903/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183903",
                "outcomeVariants": []
            },
            {
                "id": 656183932,
                "name": "1st: Sebastian Kris, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912198,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183932/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183932",
                "outcomeVariants": []
            },
            {
                "id": 656183861,
                "name": "1st: Alex Johnston, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912113,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183861/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183861",
                "outcomeVariants": []
            },
            {
                "id": 656183916,
                "name": "1st: Bailey Simonsson, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912176,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183916/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183916",
                "outcomeVariants": []
            },
            {
                "id": 656183914,
                "name": "1st: Curtis Scott, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912174,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183914/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183914",
                "outcomeVariants": []
            },
            {
                "id": 656183875,
                "name": "1st: Jaxson Paulo, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912127,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183875/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183875",
                "outcomeVariants": []
            },
            {
                "id": 656183901,
                "name": "1st: Jordan Rapana, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912161,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183901/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183901",
                "outcomeVariants": []
            },
            {
                "id": 656183929,
                "name": "1st: Sebastian Kris, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912195,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183929/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183929",
                "outcomeVariants": []
            },
            {
                "id": 656183925,
                "name": "1st: Bailey Simonsson, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912191,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183925/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183925",
                "outcomeVariants": []
            },
            {
                "id": 656183889,
                "name": "1st: Caleb Aekins, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912141,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183889/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183889",
                "outcomeVariants": []
            },
            {
                "id": 656183873,
                "name": "1st: Jaxson Paulo, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912125,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183873/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183873",
                "outcomeVariants": []
            },
            {
                "id": 656183905,
                "name": "1st: Jordan Rapana, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912165,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183905/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183905",
                "outcomeVariants": []
            },
            {
                "id": 656183930,
                "name": "1st: Sebastian Kris, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912196,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183930/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183930",
                "outcomeVariants": []
            },
            {
                "id": 656183894,
                "name": "1st: Caleb Aekins, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912148,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183894/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183894",
                "outcomeVariants": []
            },
            {
                "id": 656183854,
                "name": "1st: Campbell Graham, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912106,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183854/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183854",
                "outcomeVariants": []
            },
            {
                "id": 656183910,
                "name": "1st: Curtis Scott, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912170,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183910/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183910",
                "outcomeVariants": []
            },
            {
                "id": 656183909,
                "name": "1st: Curtis Scott, 2nd: Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912169,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183909/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183909",
                "outcomeVariants": []
            },
            {
                "id": 656183912,
                "name": "1st: Curtis Scott, 2nd: Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912172,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183912/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183912",
                "outcomeVariants": []
            },
            {
                "id": 656183837,
                "name": "1st: Dane Gagai, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912089,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183837/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183837",
                "outcomeVariants": []
            },
            {
                "id": 656183871,
                "name": "1st: Jaxson Paulo, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912123,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183871/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183871",
                "outcomeVariants": []
            },
            {
                "id": 656183934,
                "name": "1st: Sebastian Kris, 2nd: Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912200,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183934/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183934",
                "outcomeVariants": []
            },
            {
                "id": 656183923,
                "name": "1st: Bailey Simonsson, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912189,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183923/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183923",
                "outcomeVariants": []
            },
            {
                "id": 656183890,
                "name": "1st: Caleb Aekins, 2nd: Cody Walker",
                "resultType": "-",
                "externalId": 1214912142,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183890/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183890",
                "outcomeVariants": []
            },
            {
                "id": 656183846,
                "name": "1st: Campbell Graham, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912098,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183846/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183846",
                "outcomeVariants": []
            },
            {
                "id": 656183906,
                "name": "1st: Curtis Scott, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912166,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183906/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183906",
                "outcomeVariants": []
            },
            {
                "id": 656183847,
                "name": "1st: Campbell Graham, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912099,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183847/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183847",
                "outcomeVariants": []
            },
            {
                "id": 656183855,
                "name": "1st: Campbell Graham, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912107,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183855/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183855",
                "outcomeVariants": []
            },
            {
                "id": 656183841,
                "name": "1st: Dane Gagai, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912093,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183841/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183841",
                "outcomeVariants": []
            },
            {
                "id": 656183836,
                "name": "1st: Dane Gagai, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912088,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183836/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183836",
                "outcomeVariants": []
            },
            {
                "id": 656183845,
                "name": "1st: Dane Gagai, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912097,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183845/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183845",
                "outcomeVariants": []
            },
            {
                "id": 656183891,
                "name": "1st: Caleb Aekins, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912145,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183891/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183891",
                "outcomeVariants": []
            },
            {
                "id": 656183881,
                "name": "1st: Cody Walker, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912133,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183881/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183881",
                "outcomeVariants": []
            },
            {
                "id": 656183883,
                "name": "1st: Cody Walker, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912135,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183883/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183883",
                "outcomeVariants": []
            },
            {
                "id": 656183885,
                "name": "1st: Cody Walker, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912137,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183885/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183885",
                "outcomeVariants": []
            },
            {
                "id": 656183933,
                "name": "1st: Sebastian Kris, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912199,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183933/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183933",
                "outcomeVariants": []
            },
            {
                "id": 656183893,
                "name": "1st: Caleb Aekins, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912147,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183893/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183893",
                "outcomeVariants": []
            },
            {
                "id": 656183921,
                "name": "1st: Bailey Simonsson, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912187,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 401,
                    "winPriceNum": 400000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183921/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183921",
                "outcomeVariants": []
            },
            {
                "id": 656183915,
                "name": "1st: Curtis Scott, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912175,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183915/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183915",
                "outcomeVariants": []
            },
            {
                "id": 656183843,
                "name": "1st: Dane Gagai, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912095,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183843/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183843",
                "outcomeVariants": []
            },
            {
                "id": 656183931,
                "name": "1st: Sebastian Kris, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912197,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183931/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183931",
                "outcomeVariants": []
            },
            {
                "id": 656183927,
                "name": "1st: Sebastian Kris, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912193,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183927/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183927",
                "outcomeVariants": []
            },
            {
                "id": 656183887,
                "name": "1st: Caleb Aekins, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912139,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183887/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183887",
                "outcomeVariants": []
            },
            {
                "id": 656183886,
                "name": "1st: Caleb Aekins, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912138,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183886/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183886",
                "outcomeVariants": []
            },
            {
                "id": 656183895,
                "name": "1st: Caleb Aekins, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912149,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183895/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183895",
                "outcomeVariants": []
            },
            {
                "id": 656183851,
                "name": "1st: Campbell Graham, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912103,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183851/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183851",
                "outcomeVariants": []
            },
            {
                "id": 656183853,
                "name": "1st: Campbell Graham, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912105,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183853/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183853",
                "outcomeVariants": []
            },
            {
                "id": 656183911,
                "name": "1st: Curtis Scott, 2nd: Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912171,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183911/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183911",
                "outcomeVariants": []
            },
            {
                "id": 656183907,
                "name": "1st: Curtis Scott, 2nd: Campbell Graham",
                "resultType": "-",
                "externalId": 1214912167,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183907/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183907",
                "outcomeVariants": []
            },
            {
                "id": 656183913,
                "name": "1st: Curtis Scott, 2nd: Curtis Scott",
                "resultType": "-",
                "externalId": 1214912173,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183913/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183913",
                "outcomeVariants": []
            },
            {
                "id": 656183926,
                "name": "1st: Sebastian Kris, 2nd: Dane Gagai",
                "resultType": "-",
                "externalId": 1214912192,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183926/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183926",
                "outcomeVariants": []
            },
            {
                "id": 656183935,
                "name": "1st: Sebastian Kris, 2nd: Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912201,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183935/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747703/Selections/656183935",
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
        "id": 123747640,
        "externalId": 261773299,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640",
        "selections": [
            {
                "id": 656183238,
                "name": "Alex Johnston / Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912222,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183238/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183238",
                "outcomeVariants": []
            },
            {
                "id": 656183241,
                "name": "Alex Johnston / Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912225,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183241/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183241",
                "outcomeVariants": []
            },
            {
                "id": 656183239,
                "name": "Alex Johnston / Cody Walker",
                "resultType": "-",
                "externalId": 1214912223,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183239/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183239",
                "outcomeVariants": []
            },
            {
                "id": 656183246,
                "name": "Jaxson Paulo / Cody Walker",
                "resultType": "-",
                "externalId": 1214912230,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183246/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183246",
                "outcomeVariants": []
            },
            {
                "id": 656183248,
                "name": "Jaxson Paulo / Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912232,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183248/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183248",
                "outcomeVariants": []
            },
            {
                "id": 656183237,
                "name": "Alex Johnston / Alex Johnston",
                "resultType": "-",
                "externalId": 1214912221,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183237/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183237",
                "outcomeVariants": []
            },
            {
                "id": 656183243,
                "name": "Alex Johnston / Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912227,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183243/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183243",
                "outcomeVariants": []
            },
            {
                "id": 656183219,
                "name": "Dane Gagai / Alex Johnston",
                "resultType": "-",
                "externalId": 1214912204,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183219/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183219",
                "outcomeVariants": []
            },
            {
                "id": 656183254,
                "name": "Cody Walker / Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912238,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183254/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183254",
                "outcomeVariants": []
            },
            {
                "id": 656183229,
                "name": "Campbell Graham / Alex Johnston",
                "resultType": "-",
                "externalId": 1214912213,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183229/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183229",
                "outcomeVariants": []
            },
            {
                "id": 656183250,
                "name": "Jaxson Paulo / Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912234,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183250/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183250",
                "outcomeVariants": []
            },
            {
                "id": 656183265,
                "name": "Jordan Rapana / Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912249,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183265/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183265",
                "outcomeVariants": []
            },
            {
                "id": 656183221,
                "name": "Dane Gagai / Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912205,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183221/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183221",
                "outcomeVariants": []
            },
            {
                "id": 656183230,
                "name": "Campbell Graham / Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912214,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183230/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183230",
                "outcomeVariants": []
            },
            {
                "id": 656183224,
                "name": "Dane Gagai / Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912208,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183224/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183224",
                "outcomeVariants": []
            },
            {
                "id": 656183242,
                "name": "Alex Johnston / Curtis Scott",
                "resultType": "-",
                "externalId": 1214912226,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183242/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183242",
                "outcomeVariants": []
            },
            {
                "id": 656183244,
                "name": "Alex Johnston / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912228,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183244/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183244",
                "outcomeVariants": []
            },
            {
                "id": 656183231,
                "name": "Campbell Graham / Cody Walker",
                "resultType": "-",
                "externalId": 1214912215,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183231/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183231",
                "outcomeVariants": []
            },
            {
                "id": 656183233,
                "name": "Campbell Graham / Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912217,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183233/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183233",
                "outcomeVariants": []
            },
            {
                "id": 656183226,
                "name": "Dane Gagai / Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912210,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183226/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183226",
                "outcomeVariants": []
            },
            {
                "id": 656183222,
                "name": "Dane Gagai / Cody Walker",
                "resultType": "-",
                "externalId": 1214912206,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183222/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183222",
                "outcomeVariants": []
            },
            {
                "id": 656183245,
                "name": "Jaxson Paulo / Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912229,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183245/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183245",
                "outcomeVariants": []
            },
            {
                "id": 656183259,
                "name": "Caleb Aekins / Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912243,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183259/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183259",
                "outcomeVariants": []
            },
            {
                "id": 656183256,
                "name": "Cody Walker / Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912240,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183256/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183256",
                "outcomeVariants": []
            },
            {
                "id": 656183263,
                "name": "Jordan Rapana / Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912247,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183263/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183263",
                "outcomeVariants": []
            },
            {
                "id": 656183240,
                "name": "Alex Johnston / Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912224,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183240/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183240",
                "outcomeVariants": []
            },
            {
                "id": 656183235,
                "name": "Campbell Graham / Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912219,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183235/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183235",
                "outcomeVariants": []
            },
            {
                "id": 656183252,
                "name": "Cody Walker / Cody Walker",
                "resultType": "-",
                "externalId": 1214912236,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183252/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183252",
                "outcomeVariants": []
            },
            {
                "id": 656183251,
                "name": "Jaxson Paulo / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912235,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183251/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183251",
                "outcomeVariants": []
            },
            {
                "id": 656183264,
                "name": "Jordan Rapana / Curtis Scott",
                "resultType": "-",
                "externalId": 1214912248,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183264/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183264",
                "outcomeVariants": []
            },
            {
                "id": 656183266,
                "name": "Jordan Rapana / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912250,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183266/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183266",
                "outcomeVariants": []
            },
            {
                "id": 656183270,
                "name": "Bailey Simonsson / Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912254,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183270/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183270",
                "outcomeVariants": []
            },
            {
                "id": 656183271,
                "name": "Bailey Simonsson / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912255,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183271/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183271",
                "outcomeVariants": []
            },
            {
                "id": 656183257,
                "name": "Cody Walker / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912241,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183257/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183257",
                "outcomeVariants": []
            },
            {
                "id": 656183268,
                "name": "Curtis Scott / Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912252,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183268/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183268",
                "outcomeVariants": []
            },
            {
                "id": 656183217,
                "name": "Dane Gagai / Campbell Graham",
                "resultType": "-",
                "externalId": 1214912203,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183217/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183217",
                "outcomeVariants": []
            },
            {
                "id": 656183247,
                "name": "Jaxson Paulo / Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912231,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183247/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183247",
                "outcomeVariants": []
            },
            {
                "id": 656183249,
                "name": "Jaxson Paulo / Curtis Scott",
                "resultType": "-",
                "externalId": 1214912233,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183249/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183249",
                "outcomeVariants": []
            },
            {
                "id": 656183261,
                "name": "Caleb Aekins / Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912245,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183261/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183261",
                "outcomeVariants": []
            },
            {
                "id": 656183253,
                "name": "Cody Walker / Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912237,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183253/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183253",
                "outcomeVariants": []
            },
            {
                "id": 656183255,
                "name": "Cody Walker / Curtis Scott",
                "resultType": "-",
                "externalId": 1214912239,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183255/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183255",
                "outcomeVariants": []
            },
            {
                "id": 656183236,
                "name": "Campbell Graham / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912220,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183236/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183236",
                "outcomeVariants": []
            },
            {
                "id": 656183225,
                "name": "Dane Gagai / Curtis Scott",
                "resultType": "-",
                "externalId": 1214912209,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183225/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183225",
                "outcomeVariants": []
            },
            {
                "id": 656183269,
                "name": "Curtis Scott / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912253,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183269/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183269",
                "outcomeVariants": []
            },
            {
                "id": 656183223,
                "name": "Dane Gagai / Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912207,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183223/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183223",
                "outcomeVariants": []
            },
            {
                "id": 656183227,
                "name": "Dane Gagai / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912211,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183227/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183227",
                "outcomeVariants": []
            },
            {
                "id": 656183260,
                "name": "Caleb Aekins / Curtis Scott",
                "resultType": "-",
                "externalId": 1214912244,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183260/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183260",
                "outcomeVariants": []
            },
            {
                "id": 656183262,
                "name": "Caleb Aekins / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912246,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183262/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183262",
                "outcomeVariants": []
            },
            {
                "id": 656183234,
                "name": "Campbell Graham / Curtis Scott",
                "resultType": "-",
                "externalId": 1214912218,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183234/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183234",
                "outcomeVariants": []
            },
            {
                "id": 656183232,
                "name": "Campbell Graham / Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912216,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183232/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183232",
                "outcomeVariants": []
            },
            {
                "id": 656183228,
                "name": "Campbell Graham / Campbell Graham",
                "resultType": "-",
                "externalId": 1214912212,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183228/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183228",
                "outcomeVariants": []
            },
            {
                "id": 656183216,
                "name": "Dane Gagai / Dane Gagai",
                "resultType": "-",
                "externalId": 1214912202,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183216/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183216",
                "outcomeVariants": []
            },
            {
                "id": 656183258,
                "name": "Caleb Aekins / Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912242,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183258/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183258",
                "outcomeVariants": []
            },
            {
                "id": 656183267,
                "name": "Curtis Scott / Curtis Scott",
                "resultType": "-",
                "externalId": 1214912251,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183267/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183267",
                "outcomeVariants": []
            },
            {
                "id": 656183272,
                "name": "Sebastian Kris / Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912256,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183272/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747640/Selections/656183272",
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
        "id": 123747602,
        "externalId": 261773083,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602",
        "selections": [
            {
                "id": 656182576,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910452,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182576/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182576",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182578,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910454,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182578/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182578",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182583,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910459,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182583/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182583",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182570,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910446,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182570/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182570",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182577,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910453,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182577/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182577",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182586,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910462,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182586/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182586",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182572,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910448,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182572/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182572",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182582,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910458,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182582/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182582",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182584,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910460,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182584/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182584",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182585,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910461,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182585/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182585",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182581,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910457,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182581/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182581",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182573,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910449,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182573/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182573",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182579,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910455,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182579/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182579",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182574,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910450,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182574/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182574",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182580,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910456,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182580/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182580",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182571,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910447,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182571/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182571",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182575,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910451,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182575/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182575",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182604,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214910480,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182604/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182604",
                "outcomeVariants": []
            },
            {
                "id": 656182593,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910469,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182593/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182593",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182599,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910475,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182599/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182599",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182603,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910479,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182603/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182603",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182590,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910466,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182590/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182590",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182591,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910467,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182591/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182591",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182589,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910465,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182589/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182589",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182596,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910472,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182596/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182596",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182600,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910476,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182600/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182600",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182597,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910473,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182597/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182597",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182587,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910463,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182587/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182587",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182595,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910471,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182595/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182595",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182592,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910468,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182592/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182592",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182601,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910477,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182601/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182601",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182594,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910470,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182594/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182594",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182588,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910464,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182588/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182588",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182598,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910474,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182598/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182598",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182602,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910478,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182602/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747602/Selections/656182602",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747615,
        "externalId": 261773084,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615",
        "selections": [
            {
                "id": 656182798,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910487,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182798/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182798",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182800,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910489,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182800/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182800",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182805,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910494,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182805/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182805",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182790,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910481,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182790/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182790",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182808,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910497,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182808/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182808",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182799,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910488,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182799/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182799",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182792,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910483,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182792/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182792",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182804,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910493,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182804/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182804",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182806,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910495,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182806/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182806",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182807,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910496,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182807/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182807",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182803,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910492,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182803/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182803",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182793,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910484,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182793/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182793",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182801,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910490,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182801/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182801",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182795,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910485,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182795/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182795",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182797,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910486,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182797/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182797",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182802,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910491,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182802/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182802",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182791,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910482,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182791/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182791",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182828,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214910515,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182828/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182828",
                "outcomeVariants": []
            },
            {
                "id": 656182816,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910504,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182816/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182816",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182823,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910510,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182823/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182823",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182827,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910514,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182827/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182827",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182812,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910501,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182812/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182812",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182813,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910502,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182813/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182813",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182811,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910500,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182811/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182811",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182824,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910511,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182824/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182824",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182820,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910507,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182820/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182820",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182821,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910508,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182821/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182821",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182809,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910498,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182809/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182809",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182819,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910506,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182819/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182819",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182814,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910503,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182814/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182814",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182825,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910512,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182825/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182825",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182817,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910505,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182817/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182817",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182810,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910499,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182810/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182810",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182822,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910509,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182822/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182822",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182826,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910513,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182826/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747615/Selections/656182826",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747611,
        "externalId": 261773091,
        "name": "First Tryscorer - Canberra Raiders",
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611",
        "selections": [
            {
                "id": 656182774,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910727,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182774/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182774",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182778,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910729,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182778/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182778",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182783,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910734,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182783/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182783",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182788,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910737,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182788/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182788",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182766,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910721,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182766/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182766",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182776,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910728,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182776/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182776",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182785,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910735,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182785/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182785",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182782,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910733,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182782/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182782",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182781,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910732,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182781/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182781",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182768,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910723,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182768/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182768",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182786,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910736,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182786/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182786",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182770,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910724,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182770/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182770",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182779,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910730,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182779/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182779",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182789,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214910738,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182789/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182789",
                "outcomeVariants": []
            },
            {
                "id": 656182772,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910725,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182772/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182772",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182773,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910726,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182773/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182773",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182780,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910731,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182780/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182780",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182767,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910722,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182767/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747611/Selections/656182767",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747606,
        "externalId": 261773092,
        "name": "First Tryscorer - Rabbitohs",
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606",
        "selections": [
            {
                "id": 656182714,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910745,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182714/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182714",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182720,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910751,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182720/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182720",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182724,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910755,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182724/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182724",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182711,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910742,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182711/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182711",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182712,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910743,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182712/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182712",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182717,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910748,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182717/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182717",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182710,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910741,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182710/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182710",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182721,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910752,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182721/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182721",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182718,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910749,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182718/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182718",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182708,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910739,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182708/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182708",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182716,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910747,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182716/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182716",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182713,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910744,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182713/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182713",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182722,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910753,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182722/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182722",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182715,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910746,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182715/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182715",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182709,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910740,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182709/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182709",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182719,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910750,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182719/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182719",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182723,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910754,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182723/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182723",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182725,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214910756,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182725/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747606/Selections/656182725",
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
        "id": 123747627,
        "externalId": 261773268,
        "name": "Last Tryscorer - Canberra Raiders",
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627",
        "selections": [
            {
                "id": 656182948,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214911476,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182948/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182948",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182950,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214911478,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182950/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182950",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182955,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214911483,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182955/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182955",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182958,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214911486,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182958/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182958",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182949,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214911477,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182949/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182949",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182956,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214911484,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182956/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182956",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182942,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214911470,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182942/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182942",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182954,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214911482,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182954/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182954",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182953,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214911481,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182953/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182953",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182944,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214911472,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182944/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182944",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182957,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214911485,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182957/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182957",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182945,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214911473,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182945/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182945",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182951,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214911479,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182951/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182951",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182959,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214911487,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182959/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182959",
                "outcomeVariants": []
            },
            {
                "id": 656182946,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214911474,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182946/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182946",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182943,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214911471,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182943/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182943",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182947,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214911475,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182947/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182947",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182952,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214911480,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182952/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747627/Selections/656182952",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747705,
        "externalId": 261773269,
        "name": "Last Tryscorer - Rabbitohs",
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705",
        "selections": [
            {
                "id": 656183944,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214911494,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.33,
                    "winPriceNum": 3333,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183944/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183944",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183950,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214911500,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183950/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183950",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183954,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214911504,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183954/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183954",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183942,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214911492,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183942/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183942",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183941,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214911491,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183941/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183941",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183947,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214911497,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183947/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183947",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183940,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214911490,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183940/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183940",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183946,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214911496,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183946/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183946",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183951,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214911501,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183951/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183951",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183948,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214911498,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183948/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183948",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183938,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214911488,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183938/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183938",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183943,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214911493,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183943/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183943",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183952,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214911502,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183952/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183952",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183945,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214911495,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183945/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183945",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183939,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214911489,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183939/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183939",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183949,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214911499,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183949/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183949",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183953,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214911503,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183953/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183953",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656183955,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214911505,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183955/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747705/Selections/656183955",
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
        "id": 123747601,
        "externalId": 261773090,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601",
        "selections": [
            {
                "id": 656182541,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910692,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182541/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182541",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182543,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910694,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182543/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182543",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182548,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910699,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182548/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182548",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182551,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910702,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182551/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182551",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182542,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910693,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182542/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182542",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182535,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910686,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182535/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182535",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182537,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910688,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182537/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182537",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182547,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910698,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182547/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182547",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182549,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910700,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182549/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182549",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182550,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910701,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182550/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182550",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182546,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910697,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182546/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182546",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182538,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910689,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182538/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182538",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182544,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910695,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182544/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182544",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182539,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910690,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182539/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182539",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182545,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910696,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182545/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182545",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182536,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910687,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182536/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182536",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182540,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910691,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182540/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182540",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182569,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214910720,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182569/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182569",
                "outcomeVariants": []
            },
            {
                "id": 656182558,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910709,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182558/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182558",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182564,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910715,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182564/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182564",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182568,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910719,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182568/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182568",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182555,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910706,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182555/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182555",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182556,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910707,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182556/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182556",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182561,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910712,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182561/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182561",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182554,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910705,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182554/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182554",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182565,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910716,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182565/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182565",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182562,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910713,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182562/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182562",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182557,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910708,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182557/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182557",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182552,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910703,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182552/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182552",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182566,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910717,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182566/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182566",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182560,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910711,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182560/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182560",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182559,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910710,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182559/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182559",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182553,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910704,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182553/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182553",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182563,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910714,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182563/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182563",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182567,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910718,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182567/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747601/Selections/656182567",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747600,
        "externalId": 261773094,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600",
        "selections": [
            {
                "id": 656182506,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214910800,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182506/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182506",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182508,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214910802,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182508/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182508",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182513,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214910807,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182513/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182513",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182516,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214910810,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182516/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182516",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182500,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214910792,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182500/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182500",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182507,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214910801,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182507/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182507",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182514,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214910808,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182514/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182514",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182512,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214910806,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182512/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182512",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182511,
                "name": "Joseph Tapine",
                "resultType": "-",
                "externalId": 1214910805,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182511/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182511",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182502,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214910794,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182502/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182502",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182515,
                "name": "Hudson Young",
                "resultType": "-",
                "externalId": 1214910809,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182515/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182515",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182503,
                "name": "Siliva Havili",
                "resultType": "-",
                "externalId": 1214910795,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182503/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182503",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182509,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214910803,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182509/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182509",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182504,
                "name": "Corey Horsburgh",
                "resultType": "-",
                "externalId": 1214910796,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182504/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182504",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182505,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214910799,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182505/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182505",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182510,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214910804,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182510/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182510",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182501,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214910793,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182501/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182501",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182534,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214910828,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182534/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182534",
                "outcomeVariants": []
            },
            {
                "id": 656182523,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214910817,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.2,
                    "winPriceNum": 3200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182523/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182523",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182529,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214910823,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182529/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182529",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182533,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214910827,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182533/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182533",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182520,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214910814,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182520/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182520",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182521,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214910815,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182521/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182521",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182526,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214910820,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182526/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182526",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182519,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214910813,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182519/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182519",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182530,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214910824,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182530/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182530",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182527,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214910821,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182527/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182527",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182517,
                "name": "Jai Arrow",
                "resultType": "-",
                "externalId": 1214910811,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182517/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182517",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182525,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214910819,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182525/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182525",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182522,
                "name": "Jacob Host",
                "resultType": "-",
                "externalId": 1214910816,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182522/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182522",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182531,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214910825,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182531/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182531",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182524,
                "name": "Liam Knight",
                "resultType": "-",
                "externalId": 1214910818,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182524/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182524",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182518,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214910812,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182518/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182518",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182528,
                "name": "Mark Nicholls",
                "resultType": "-",
                "externalId": 1214910822,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182528/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182528",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            },
            {
                "id": 656182532,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214910826,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182532/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747600/Selections/656182532",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747682,
        "externalId": 261773334,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747682",
        "selections": [
            {
                "id": 656183687,
                "name": "Backs (No's 1, 2, 3, 4, 5, 6, 7)",
                "resultType": "-",
                "externalId": 1214912703,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.22,
                    "winPriceNum": 220,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747682/Selections/656183687/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747682/Selections/656183687",
                "outcomeVariants": []
            },
            {
                "id": 656183688,
                "name": "Forwards (No's 8, 9, 10, 11, 12, 13)",
                "resultType": "-",
                "externalId": 1214912704,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.5,
                    "winPriceNum": 2500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747682/Selections/656183688/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747682/Selections/656183688",
                "outcomeVariants": []
            },
            {
                "id": 656183689,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214912705,
                "sort": 40,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747682/Selections/656183689/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747682/Selections/656183689",
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
        "id": 123747624,
        "externalId": 261773336,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747624",
        "selections": [
            {
                "id": 656182903,
                "name": "Backs (No's 1, 2, 3, 4, 5, 6, 7)",
                "resultType": "-",
                "externalId": 1214912709,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.3,
                    "winPriceNum": 300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747624/Selections/656182903/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747624/Selections/656182903",
                "outcomeVariants": []
            },
            {
                "id": 656182904,
                "name": "Forwards (No's 8, 9, 10, 11, 12, 13)",
                "resultType": "-",
                "externalId": 1214912710,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.5,
                    "winPriceNum": 2500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747624/Selections/656182904/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747624/Selections/656182904",
                "outcomeVariants": []
            },
            {
                "id": 656182905,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214912711,
                "sort": 40,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747624/Selections/656182905/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747624/Selections/656182905",
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
        "id": 123747649,
        "externalId": 261773337,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747649",
        "selections": [
            {
                "id": 656183363,
                "name": "Backs (No's 1, 2, 3, 4, 5, 6, 7)",
                "resultType": "-",
                "externalId": 1214912712,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.25,
                    "winPriceNum": 250,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747649/Selections/656183363/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747649/Selections/656183363",
                "outcomeVariants": []
            },
            {
                "id": 656183364,
                "name": "Forwards (No's 8, 9, 10, 11, 12, 13)",
                "resultType": "-",
                "externalId": 1214912713,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.6,
                    "winPriceNum": 2600,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747649/Selections/656183364/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747649/Selections/656183364",
                "outcomeVariants": []
            },
            {
                "id": 656183365,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1214912714,
                "sort": 40,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747649/Selections/656183365/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747649/Selections/656183365",
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
        "id": 123747701,
        "externalId": 261773282,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747701",
        "selections": [
            {
                "id": 656183795,
                "name": "Caleb Aekins",
                "resultType": "-",
                "externalId": 1214912043,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747701/Selections/656183795/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747701/Selections/656183795",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183797,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912045,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.72,
                    "winPriceNum": 720,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747701/Selections/656183797/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747701/Selections/656183797",
                "outcomeVariants": []
            },
            {
                "id": 656183796,
                "name": "Cody Walker",
                "resultType": "-",
                "externalId": 1214912044,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.5,
                    "winPriceNum": 1500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747701/Selections/656183796/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747701/Selections/656183796",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747688,
        "externalId": 261773283,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747688",
        "selections": [
            {
                "id": 656183763,
                "name": "Bailey Simonsson",
                "resultType": "-",
                "externalId": 1214912046,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.33,
                    "winPriceNum": 3330,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747688/Selections/656183763/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747688/Selections/656183763",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183765,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912048,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.4,
                    "winPriceNum": 1400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747688/Selections/656183765/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747688/Selections/656183765",
                "outcomeVariants": []
            },
            {
                "id": 656183764,
                "name": "Alex Johnston",
                "resultType": "-",
                "externalId": 1214912047,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.1,
                    "winPriceNum": 1100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747688/Selections/656183764/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747688/Selections/656183764",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747658,
        "externalId": 261773284,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747658",
        "selections": [
            {
                "id": 656183419,
                "name": "Jordan Rapana",
                "resultType": "-",
                "externalId": 1214912049,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3,
                    "winPriceNum": 2000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747658/Selections/656183419/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747658/Selections/656183419",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183421,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912051,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.3,
                    "winPriceNum": 1300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747658/Selections/656183421/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747658/Selections/656183421",
                "outcomeVariants": []
            },
            {
                "id": 656183420,
                "name": "Jaxson Paulo",
                "resultType": "-",
                "externalId": 1214912050,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.88,
                    "winPriceNum": 1880,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747658/Selections/656183420/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747658/Selections/656183420",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747655,
        "externalId": 261773285,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747655",
        "selections": [
            {
                "id": 656183377,
                "name": "Sebastian Kris",
                "resultType": "-",
                "externalId": 1214912052,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747655/Selections/656183377/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747655/Selections/656183377",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183379,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912054,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.57,
                    "winPriceNum": 570,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747655/Selections/656183379/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747655/Selections/656183379",
                "outcomeVariants": []
            },
            {
                "id": 656183378,
                "name": "Dane Gagai",
                "resultType": "-",
                "externalId": 1214912053,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.4,
                    "winPriceNum": 2400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747655/Selections/656183378/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747655/Selections/656183378",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747685,
        "externalId": 261773286,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747685",
        "selections": [
            {
                "id": 656183730,
                "name": "Curtis Scott",
                "resultType": "-",
                "externalId": 1214912055,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747685/Selections/656183730/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747685/Selections/656183730",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183732,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912057,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.5,
                    "winPriceNum": 500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747685/Selections/656183732/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747685/Selections/656183732",
                "outcomeVariants": []
            },
            {
                "id": 656183731,
                "name": "Campbell Graham",
                "resultType": "-",
                "externalId": 1214912056,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747685/Selections/656183731/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747685/Selections/656183731",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747699,
        "externalId": 261773287,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747699",
        "selections": [
            {
                "id": 656183788,
                "name": "Jack Wighton",
                "resultType": "-",
                "externalId": 1214912058,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.5,
                    "winPriceNum": 2500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747699/Selections/656183788/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747699/Selections/656183788",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183790,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912060,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.53,
                    "winPriceNum": 530,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747699/Selections/656183790/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747699/Selections/656183790",
                "outcomeVariants": []
            },
            {
                "id": 656183789,
                "name": "Benji Marshall",
                "resultType": "-",
                "externalId": 1214912059,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747699/Selections/656183789/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747699/Selections/656183789",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747637,
        "externalId": 261773288,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747637",
        "selections": [
            {
                "id": 656183209,
                "name": "George Williams",
                "resultType": "-",
                "externalId": 1214912061,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747637/Selections/656183209/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747637/Selections/656183209",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183213,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912063,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.33,
                    "winPriceNum": 330,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747637/Selections/656183213/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747637/Selections/656183213",
                "outcomeVariants": []
            },
            {
                "id": 656183211,
                "name": "Adam Reynolds",
                "resultType": "-",
                "externalId": 1214912062,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747637/Selections/656183211/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747637/Selections/656183211",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747669,
        "externalId": 261773289,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747669",
        "selections": [
            {
                "id": 656183588,
                "name": "Ryan James",
                "resultType": "-",
                "externalId": 1214912064,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747669/Selections/656183588/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747669/Selections/656183588",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183590,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912066,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.12,
                    "winPriceNum": 120,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747669/Selections/656183590/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747669/Selections/656183590",
                "outcomeVariants": []
            },
            {
                "id": 656183589,
                "name": "Thomas Burgess",
                "resultType": "-",
                "externalId": 1214912065,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747669/Selections/656183589/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747669/Selections/656183589",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747692,
        "externalId": 261773290,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747692",
        "selections": [
            {
                "id": 656183772,
                "name": "Emre Guler",
                "resultType": "-",
                "externalId": 1214912067,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747692/Selections/656183772/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747692/Selections/656183772",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183774,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912069,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.11,
                    "winPriceNum": 110,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747692/Selections/656183774/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747692/Selections/656183774",
                "outcomeVariants": []
            },
            {
                "id": 656183773,
                "name": "Tevita Tatola",
                "resultType": "-",
                "externalId": 1214912068,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747692/Selections/656183773/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747692/Selections/656183773",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747672,
        "externalId": 261773291,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747672",
        "selections": [
            {
                "id": 656183661,
                "name": "Tom Starling",
                "resultType": "-",
                "externalId": 1214912070,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747672/Selections/656183661/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747672/Selections/656183661",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183663,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912072,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.33,
                    "winPriceNum": 330,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747672/Selections/656183663/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747672/Selections/656183663",
                "outcomeVariants": []
            },
            {
                "id": 656183662,
                "name": "Damien Cook",
                "resultType": "-",
                "externalId": 1214912071,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747672/Selections/656183662/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747672/Selections/656183662",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747623,
        "externalId": 261773292,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747623",
        "selections": [
            {
                "id": 656182900,
                "name": "Corey Harawira-Naera",
                "resultType": "-",
                "externalId": 1214912073,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747623/Selections/656182900/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747623/Selections/656182900",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656182902,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912075,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.33,
                    "winPriceNum": 330,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747623/Selections/656182902/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747623/Selections/656182902",
                "outcomeVariants": []
            },
            {
                "id": 656182901,
                "name": "Keaon Koloamatangi",
                "resultType": "-",
                "externalId": 1214912074,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747623/Selections/656182901/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747623/Selections/656182901",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747706,
        "externalId": 261773293,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747706",
        "selections": [
            {
                "id": 656183956,
                "name": "Elliott Whitehead",
                "resultType": "-",
                "externalId": 1214912076,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747706/Selections/656183956/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747706/Selections/656183956",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183958,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912078,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.3,
                    "winPriceNum": 300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747706/Selections/656183958/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747706/Selections/656183958",
                "outcomeVariants": []
            },
            {
                "id": 656183957,
                "name": "Jaydn Su'A",
                "resultType": "-",
                "externalId": 1214912077,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747706/Selections/656183957/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747706/Selections/656183957",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 123747680,
        "externalId": 261773294,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747680",
        "selections": [
            {
                "id": 656183682,
                "name": "Ryan Sutton",
                "resultType": "-",
                "externalId": 1214912079,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747680/Selections/656183682/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747680/Selections/656183682",
                "outcomeVariants": [],
                "multiplesKey": "canberraraidrl"
            },
            {
                "id": 656183684,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1214912081,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.25,
                    "winPriceNum": 250,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747680/Selections/656183684/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747680/Selections/656183684",
                "outcomeVariants": []
            },
            {
                "id": 656183683,
                "name": "Cameron Murray",
                "resultType": "-",
                "externalId": 1214912080,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747680/Selections/656183683/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5804190/Markets/123747680/Selections/656183683",
                "outcomeVariants": [],
                "multiplesKey": "southsydneyrrl"
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

# converting the first index of the list in a dictionary, where I can find the First Tryscorer data.
first_tryscorer_dict = dict(data[0])
anytime_tryscorer_dict = dict(data[1])

# Accessing the NAME key where it will show what MARKET I am printing
print("NAME SELECTION: ")
print(first_tryscorer_dict.get("name"))

# As said before, I need to get the list nested and transform in a dictionary.
# So I can access the data.Here I am checking what I have inside the "selections" key and after I am tranforming in a python dict
first_tryscorer = first_tryscorer_dict.get("selections")
dictionary_values_of_first_tryscorer = dict(first_tryscorer[0])
print()

for x in range(len(first_tryscorer)):
    player_first_try_scorer_dict = dict(first_tryscorer[x])
    print(player_first_try_scorer_dict.get("name"))
    player_market_dict = dict(player_first_try_scorer_dict.get("price"))
    print(player_market_dict.get("winPrice"))
    print()
    print("----------------")
    print()

# Accessing the NAME key where it will show what MARKET I am printing
print("NAME SELECTION: ")
print(anytime_tryscorer_dict.get("name"))

# As said before, I need to get the list nested and transform in a dictionary. So I can access the data.Here I am checking what I have inside the "selections" key and after I am tranforming in a python dict
anytime_tryscrore = anytime_tryscorer_dict.get("selections")
dictionary_values_of_tryscorer = dict(anytime_tryscrore[0])
print()

for x in range(len(anytime_tryscrore)):
    player_dict = dict(anytime_tryscrore[x])
    print(player_dict.get("name"))
    player_market_dict = dict(player_dict.get("price"))
    print(player_market_dict.get("winPrice"))
    print()
    print("----------------")
    print()
