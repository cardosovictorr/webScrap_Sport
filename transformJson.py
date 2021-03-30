import json

markets_in_json = '''
[
    {
        "id": 121256584,
        "externalId": 257231874,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584",
        "selections": [
            {
                "id": 644051795,
                "name": "Brian To'o",
                "resultType": "H",
                "externalId": 1192100057,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051795/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051795",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051794,
                "name": "Charlie Staines",
                "resultType": "H",
                "externalId": 1192100056,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051794/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051794",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051782,
                "name": "Stephen Crichton",
                "resultType": "H",
                "externalId": 1192100044,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051782/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051782",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051792,
                "name": "Tyrone May",
                "resultType": "H",
                "externalId": 1192100054,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051792/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051792",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051787,
                "name": "Viliame Kikau",
                "resultType": "H",
                "externalId": 1192100049,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051787/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051787",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051793,
                "name": "Paul Momirovski",
                "resultType": "H",
                "externalId": 1192100055,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051793/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051793",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051783,
                "name": "Dylan Edwards",
                "resultType": "H",
                "externalId": 1192100045,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051783/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051783",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051790,
                "name": "Jarome Luai",
                "resultType": "H",
                "externalId": 1192100052,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051790/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051790",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051780,
                "name": "Kurt Capewell",
                "resultType": "H",
                "externalId": 1192100042,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051780/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051780",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051791,
                "name": "Liam Martin",
                "resultType": "H",
                "externalId": 1192100053,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051791/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051791",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351866,
                "name": "Matt Burton",
                "resultType": "H",
                "externalId": 1192632140,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644351866/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644351866",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051796,
                "name": "Isaah Yeo",
                "resultType": "H",
                "externalId": 1192100058,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051796/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051796",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051784,
                "name": "Matt Eisenhuth",
                "resultType": "H",
                "externalId": 1192100046,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051784/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051784",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051786,
                "name": "Mitch Kenny",
                "resultType": "H",
                "externalId": 1192100048,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051786/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051786",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051785,
                "name": "James Fisher-Harris",
                "resultType": "H",
                "externalId": 1192100047,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051785/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051785",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051789,
                "name": "Moses Leota",
                "resultType": "H",
                "externalId": 1192100051,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051789/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051789",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051788,
                "name": "Spencer Leniu",
                "resultType": "H",
                "externalId": 1192100050,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051788/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051788",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051797,
                "name": "Josh Addo-Carr",
                "resultType": "A",
                "externalId": 1192100059,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051797/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051797",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051804,
                "name": "George Jennings",
                "resultType": "A",
                "externalId": 1192100066,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051804/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051804",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051807,
                "name": "Justin Olam",
                "resultType": "A",
                "externalId": 1192100069,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051807/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051807",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051803,
                "name": "Nicho Hynes",
                "resultType": "A",
                "externalId": 1192100065,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051803/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051803",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051811,
                "name": "Reimis Smith",
                "resultType": "A",
                "externalId": 1192100073,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051811/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051811",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051806,
                "name": "Cameron Munster",
                "resultType": "A",
                "externalId": 1192100068,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051806/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051806",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051802,
                "name": "Jahrome Hughes",
                "resultType": "A",
                "externalId": 1192100064,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051802/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051802",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360289,
                "name": "Tyson Smoothy",
                "resultType": "A",
                "externalId": 1192644948,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644360289/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644360289",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051810,
                "name": "Brandon Smith",
                "resultType": "A",
                "externalId": 1192100072,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051810/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051810",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051805,
                "name": "Tui Kamikamica",
                "resultType": "A",
                "externalId": 1192100067,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051805/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051805",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360285,
                "name": "Chris Lewis",
                "resultType": "A",
                "externalId": 1192644947,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644360285/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644360285",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051800,
                "name": "Kenny Bromwich",
                "resultType": "A",
                "externalId": 1192100062,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051800/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051800",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051801,
                "name": "Thomas Eisenhuth",
                "resultType": "A",
                "externalId": 1192100063,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051801/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051801",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051798,
                "name": "Nelson Asofa-Solomona",
                "resultType": "A",
                "externalId": 1192100060,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051798/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051798",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051809,
                "name": "Aaron Pene",
                "resultType": "A",
                "externalId": 1192100071,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051809/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051809",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051799,
                "name": "Jesse Bromwich",
                "resultType": "A",
                "externalId": 1192100061,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051799/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051799",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051812,
                "name": "Christian Welch",
                "resultType": "A",
                "externalId": 1192100074,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051812/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256584/Selections/644051812",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256579,
        "externalId": 257231877,
        "name": "Anytime Tryscorer",
        "statusCode": "A",
        "sort": 18,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Quote Others. Includes extra time. Refund if not in final 17.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": true,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579",
        "selections": [
            {
                "id": 644051644,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100159,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.1,
                    "winPriceNum": 1100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051644/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051644",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051643,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100158,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.25,
                    "winPriceNum": 1250,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051643/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051643",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051631,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100146,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.7,
                    "winPriceNum": 1700,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051631/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051631",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051641,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100156,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.88,
                    "winPriceNum": 1880,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051641/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051641",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051636,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100151,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.88,
                    "winPriceNum": 1880,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051636/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051636",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051632,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100147,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.2,
                    "winPriceNum": 3200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051632/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051632",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051642,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100157,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4,
                    "winPriceNum": 3000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051642/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051642",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051639,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100154,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051639/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051639",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051629,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100144,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051629/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051629",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051640,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100155,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051640/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051640",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351858,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632143,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644351858/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644351858",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051645,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100160,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051645/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051645",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051633,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100148,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051633/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051633",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051635,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100150,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051635/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051635",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051634,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100149,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051634/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051634",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051638,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100153,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051638/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051638",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051637,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100152,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051637/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051637",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051653,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100168,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.4,
                    "winPriceNum": 1400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051653/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051653",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051646,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100161,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2,
                    "winPriceNum": 1000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051646/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051646",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051656,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100171,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.88,
                    "winPriceNum": 1880,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051656/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051656",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051652,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100167,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.3,
                    "winPriceNum": 2300,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051652/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051652",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051655,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100170,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4,
                    "winPriceNum": 3000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051655/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051655",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051660,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100175,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4,
                    "winPriceNum": 3000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051660/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051660",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051659,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100174,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051659/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051659",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051651,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100166,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051651/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051651",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051654,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100169,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051654/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051654",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360286,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644954,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644360286/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644360286",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051649,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100164,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051649/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051649",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360277,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644953,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644360277/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644360277",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051650,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100165,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051650/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051650",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051647,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100162,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051647/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051647",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051658,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100173,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051658/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051658",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051648,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100163,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051648/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051648",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051661,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100176,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051661/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256579/Selections/644051661",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256583,
        "externalId": 257231880,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583",
        "selections": [
            {
                "id": 644051762,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100258,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051762/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051762",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051761,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100257,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051761/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051761",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051749,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100245,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051749/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051749",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051759,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100255,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051759/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051759",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051754,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100250,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051754/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051754",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051760,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100256,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051760/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051760",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051750,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100246,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051750/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051750",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051757,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100253,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051757/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051757",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051758,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100254,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051758/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051758",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051747,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100243,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051747/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051747",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351863,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632146,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644351863/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644351863",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051763,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100259,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051763/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051763",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051751,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100247,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051751/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051751",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051753,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100249,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051753/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051753",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051752,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100248,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051752/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051752",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051756,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100252,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051756/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051756",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051755,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100251,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051755/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051755",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051764,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100260,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051764/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051764",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051771,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100267,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051771/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051771",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051774,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100270,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051774/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051774",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051770,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100266,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051770/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051770",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051778,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100274,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051778/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051778",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051773,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100269,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051773/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051773",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051777,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100273,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051777/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051777",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051769,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100265,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051769/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051769",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051772,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100268,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051772/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051772",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360294,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644960,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644360294/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644360294",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051767,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100263,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051767/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051767",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360293,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644959,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644360293/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644360293",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051768,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100264,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051768/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051768",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051765,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100261,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051765/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051765",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051776,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100272,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051776/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051776",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051779,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100275,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051779/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051779",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051766,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100262,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051766/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256583/Selections/644051766",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256587,
        "externalId": 257231881,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587",
        "selections": [
            {
                "id": 644051880,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100291,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051880/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051880",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051879,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100290,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051879/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051879",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051867,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100278,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051867/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051867",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051877,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100288,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051877/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051877",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051872,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100283,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051872/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051872",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051868,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100279,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051868/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051868",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051878,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100289,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051878/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051878",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051881,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100292,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051881/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051881",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051870,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100281,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051870/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051870",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051875,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100286,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051875/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051875",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051865,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100276,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051865/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051865",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051876,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100287,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051876/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051876",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351859,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632147,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644351859/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644351859",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051869,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100280,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051869/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051869",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051871,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100282,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051871/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051871",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051874,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100285,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051874/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051874",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051873,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100284,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051873/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051873",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051882,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100293,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051882/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051882",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051889,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100300,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051889/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051889",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051892,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100303,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051892/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051892",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051888,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100299,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051888/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051888",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051891,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100302,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051891/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051891",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051896,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100307,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051896/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051896",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051894,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100305,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051894/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051894",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051895,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100306,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051895/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051895",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360278,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644961,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644360278/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644360278",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051897,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100308,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051897/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051897",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051887,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100298,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051887/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051887",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051884,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100295,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051884/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051884",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051885,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100296,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051885/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051885",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051883,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100294,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051883/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051883",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051886,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100297,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051886/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051886",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051890,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100301,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051890/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644051890",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360282,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644962,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644360282/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256587/Selections/644360282",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256676,
        "externalId": 257231966,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676",
        "selections": [
            {
                "id": 644053075,
                "name": "Brian To'o to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101436,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3,
                    "winPriceNum": 2000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053075/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053075",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053074,
                "name": "Charlie Staines to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101435,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.1,
                    "winPriceNum": 2100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053074/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053074",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053084,
                "name": "George Jennings to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101445,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.5,
                    "winPriceNum": 2500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053084/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053084",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053077,
                "name": "Josh Addo-Carr to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101438,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3,
                    "winPriceNum": 2000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053077/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053077",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053062,
                "name": "Stephen Crichton to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101423,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.6,
                    "winPriceNum": 2600,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053062/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053062",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053072,
                "name": "Tyrone May to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101433,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053072/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053072",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053067,
                "name": "Viliame Kikau to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101428,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053067/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053067",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053108,
                "name": "Brian To'o to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101469,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053108/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053108",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053044,
                "name": "Josh Addo-Carr to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101405,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.33,
                    "winPriceNum": 3330,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053044/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053044",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053087,
                "name": "Justin Olam to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101448,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4,
                    "winPriceNum": 3000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053087/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053087",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053083,
                "name": "Nicho Hynes to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101444,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053083/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053083",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053086,
                "name": "Cameron Munster to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101447,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053086/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053086",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053107,
                "name": "Charlie Staines to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101468,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053107/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053107",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053063,
                "name": "Dylan Edwards to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101424,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053063/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053063",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053051,
                "name": "George Jennings to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101412,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053051/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053051",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053054,
                "name": "Justin Olam to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101415,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053054/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053054",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053073,
                "name": "Paul Momirovski to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101434,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053073/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053073",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053091,
                "name": "Reimis Smith to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101452,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053091/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053091",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053090,
                "name": "Brandon Smith to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101451,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053090/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053090",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053082,
                "name": "Jahrome Hughes to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101443,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053082/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053082",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053070,
                "name": "Jarome Luai to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101431,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053070/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053070",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053060,
                "name": "Kurt Capewell to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101421,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053060/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053060",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053071,
                "name": "Liam Martin to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101432,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053071/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053071",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351868,
                "name": "Matt Burton to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192632153,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644351868/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644351868",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053050,
                "name": "Nicho Hynes to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101411,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053050/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053050",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053095,
                "name": "Stephen Crichton to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101456,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053095/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053095",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053085,
                "name": "Tui Kamikamica to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101446,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053085/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053085",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053105,
                "name": "Tyrone May to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101466,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053105/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053105",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644360310,
                "name": "Tyson Smoothy to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192645005,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644360310/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644360310",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053100,
                "name": "Viliame Kikau to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101461,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053100/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053100",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053053,
                "name": "Cameron Munster to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101414,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053053/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053053",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053080,
                "name": "Kenny Bromwich to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101441,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053080/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053080",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360308,
                "name": "Chris Lewis to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192645004,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644360308/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644360308",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053076,
                "name": "Isaah Yeo to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101437,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053076/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053076",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053064,
                "name": "Matt Eisenhuth to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101425,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053064/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053064",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053058,
                "name": "Reimis Smith to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101419,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053058/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053058",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053081,
                "name": "Thomas Eisenhuth to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101442,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053081/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053081",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053096,
                "name": "Dylan Edwards to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101457,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053096/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053096",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053066,
                "name": "Mitch Kenny to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101427,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053066/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053066",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053106,
                "name": "Paul Momirovski to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101467,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053106/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053106",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053103,
                "name": "Jarome Luai to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101464,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053103/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053103",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053104,
                "name": "Liam Martin to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101465,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053104/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053104",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053078,
                "name": "Nelson Asofa-Solomona to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101439,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053078/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053078",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053057,
                "name": "Brandon Smith to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101418,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053057/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053057",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053049,
                "name": "Jahrome Hughes to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101410,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053049/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053049",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053093,
                "name": "Kurt Capewell to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101454,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053093/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053093",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053052,
                "name": "Tui Kamikamica to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101413,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053052/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053052",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360306,
                "name": "Tyson Smoothy to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192645003,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644360306/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644360306",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053089,
                "name": "Aaron Pene to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101450,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053089/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053089",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053079,
                "name": "Jesse Bromwich to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101440,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053079/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053079",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053047,
                "name": "Kenny Bromwich to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101408,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053047/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053047",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644351870,
                "name": "Matt Burton to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192632154,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644351870/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644351870",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644360302,
                "name": "Chris Lewis to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192645002,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644360302/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644360302",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053065,
                "name": "James Fisher-Harris to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101426,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053065/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053065",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053069,
                "name": "Moses Leota to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101430,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053069/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053069",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053068,
                "name": "Spencer Leniu to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101429,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053068/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053068",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053048,
                "name": "Thomas Eisenhuth to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101409,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053048/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053048",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053092,
                "name": "Christian Welch to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101453,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053092/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053092",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053109,
                "name": "Isaah Yeo to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101470,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053109/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053109",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053097,
                "name": "Matt Eisenhuth to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101458,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053097/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053097",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053099,
                "name": "Mitch Kenny to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101460,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053099/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053099",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053045,
                "name": "Nelson Asofa-Solomona to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101406,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053045/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053045",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053056,
                "name": "Aaron Pene to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101417,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053056/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053056",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053046,
                "name": "Jesse Bromwich to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101407,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053046/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053046",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053059,
                "name": "Christian Welch to score a try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101420,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053059/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053059",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644053098,
                "name": "James Fisher-Harris to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101459,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053098/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053098",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053102,
                "name": "Moses Leota to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101463,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053102/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053102",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053101,
                "name": "Spencer Leniu to score a try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101462,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053101/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256676/Selections/644053101",
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
        "id": 121256610,
        "externalId": 257231967,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610",
        "selections": [
            {
                "id": 644052229,
                "name": "Brian To'o to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101502,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052229/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052229",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052231,
                "name": "Josh Addo-Carr to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101504,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052231/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052231",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052228,
                "name": "Charlie Staines to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101501,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052228/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052228",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052238,
                "name": "George Jennings to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101511,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052238/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052238",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052216,
                "name": "Stephen Crichton to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101489,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052216/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052216",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052226,
                "name": "Tyrone May to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101499,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052226/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052226",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052221,
                "name": "Viliame Kikau to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101494,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052221/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052221",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052241,
                "name": "Justin Olam to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101514,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052241/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052241",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052237,
                "name": "Nicho Hynes to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101510,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052237/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052237",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052262,
                "name": "Brian To'o to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101535,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052262/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052262",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052198,
                "name": "Josh Addo-Carr to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101471,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052198/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052198",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052227,
                "name": "Paul Momirovski to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101500,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052227/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052227",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052245,
                "name": "Reimis Smith to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101518,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052245/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052245",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052240,
                "name": "Cameron Munster to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101513,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052240/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052240",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052261,
                "name": "Charlie Staines to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101534,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052261/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052261",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052217,
                "name": "Dylan Edwards to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101490,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052217/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052217",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052205,
                "name": "George Jennings to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101478,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052205/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052205",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052236,
                "name": "Jahrome Hughes to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101509,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052236/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052236",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052224,
                "name": "Jarome Luai to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101497,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052224/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052224",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052225,
                "name": "Liam Martin to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101498,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052225/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052225",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052249,
                "name": "Stephen Crichton to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101522,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052249/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052249",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052259,
                "name": "Tyrone May to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101532,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052259/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052259",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644360305,
                "name": "Tyson Smoothy to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192645009,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644360305/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644360305",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052254,
                "name": "Viliame Kikau to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101527,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052254/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052254",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052208,
                "name": "Justin Olam to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101481,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052208/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052208",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644351871,
                "name": "Matt Burton to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192632155,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644351871/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644351871",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052244,
                "name": "Brandon Smith to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101517,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052244/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052244",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052214,
                "name": "Kurt Capewell to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101487,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052214/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052214",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052204,
                "name": "Nicho Hynes to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101477,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052204/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052204",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052239,
                "name": "Tui Kamikamica to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101512,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052239/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052239",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052207,
                "name": "Cameron Munster to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101480,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052207/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052207",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052234,
                "name": "Kenny Bromwich to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101507,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052234/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052234",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052212,
                "name": "Reimis Smith to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101485,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052212/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052212",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360301,
                "name": "Chris Lewis to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192645008,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644360301/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644360301",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052230,
                "name": "Isaah Yeo to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101503,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052230/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052230",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052218,
                "name": "Matt Eisenhuth to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101491,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052218/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052218",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052235,
                "name": "Thomas Eisenhuth to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101508,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052235/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052235",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052260,
                "name": "Paul Momirovski to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101533,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052260/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052260",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052220,
                "name": "Mitch Kenny to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101493,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052220/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052220",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052250,
                "name": "Dylan Edwards to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101523,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052250/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052250",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052203,
                "name": "Jahrome Hughes to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101476,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052203/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052203",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052257,
                "name": "Jarome Luai to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101530,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052257/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052257",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052258,
                "name": "Liam Martin to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101531,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052258/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052258",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052232,
                "name": "Nelson Asofa-Solomona to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101505,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052232/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052232",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360299,
                "name": "Tyson Smoothy to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192645007,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644360299/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644360299",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052243,
                "name": "Aaron Pene to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101516,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052243/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052243",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052233,
                "name": "Jesse Bromwich to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101506,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052233/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052233",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052211,
                "name": "Brandon Smith to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101484,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052211/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052211",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360295,
                "name": "Chris Lewis to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192645006,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644360295/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644360295",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052247,
                "name": "Kurt Capewell to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101520,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052247/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052247",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052202,
                "name": "Thomas Eisenhuth to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101475,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052202/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052202",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052206,
                "name": "Tui Kamikamica to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101479,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052206/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052206",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052263,
                "name": "Isaah Yeo to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101536,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052263/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052263",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052219,
                "name": "James Fisher-Harris to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101492,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052219/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052219",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351872,
                "name": "Matt Burton to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192632156,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644351872/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644351872",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052251,
                "name": "Matt Eisenhuth to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101524,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052251/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052251",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052201,
                "name": "Kenny Bromwich to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101474,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052201/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052201",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052253,
                "name": "Mitch Kenny to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101526,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052253/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052253",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052246,
                "name": "Christian Welch to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101519,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052246/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052246",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052223,
                "name": "Moses Leota to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101496,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052223/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052223",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052222,
                "name": "Spencer Leniu to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101495,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052222/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052222",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052199,
                "name": "Nelson Asofa-Solomona to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101472,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052199/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052199",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052210,
                "name": "Aaron Pene to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101483,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052210/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052210",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052200,
                "name": "Jesse Bromwich to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101473,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052200/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052200",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052256,
                "name": "Moses Leota to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101529,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052256/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052256",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052255,
                "name": "Spencer Leniu to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101528,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052255/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052255",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052213,
                "name": "Christian Welch to score the first try and Penrith Panthers to win",
                "resultType": "-",
                "externalId": 1192101486,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052213/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052213",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052252,
                "name": "James Fisher-Harris to score the first try and Melbourne Storm to win",
                "resultType": "-",
                "externalId": 1192101525,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052252/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256610/Selections/644052252",
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
        "id": 121256581,
        "externalId": 257231878,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581",
        "selections": [
            {
                "id": 644051711,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100192,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.5,
                    "winPriceNum": 2500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051711/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051711",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051710,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100191,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051710/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051710",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051698,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100179,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051698/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051698",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051708,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100189,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051708/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051708",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051703,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100184,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051703/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051703",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051699,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100180,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051699/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051699",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051709,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100190,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051709/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051709",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051706,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100187,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051706/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051706",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051707,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100188,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051707/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051707",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051696,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100177,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051696/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051696",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351861,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632144,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644351861/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644351861",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051712,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100193,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051712/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051712",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051700,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100181,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051700/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051700",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051702,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100183,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051702/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051702",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051701,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100182,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051701/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051701",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051705,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100186,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051705/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051705",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051704,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100185,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051704/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051704",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051713,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100194,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.4,
                    "winPriceNum": 2400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051713/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051713",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051720,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100201,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4,
                    "winPriceNum": 3000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051720/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051720",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051723,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100204,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051723/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051723",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051719,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100200,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051719/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051719",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051722,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100203,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051722/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051722",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051727,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100208,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051727/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051727",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051726,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100207,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051726/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051726",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051718,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100199,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051718/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051718",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051721,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100202,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051721/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051721",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360280,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644956,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644360280/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644360280",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051716,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100197,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051716/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051716",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360273,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644955,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644360273/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644360273",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051717,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100198,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051717/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051717",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051714,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100195,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051714/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051714",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051725,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100206,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051725/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051725",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051715,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100196,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051715/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051715",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051728,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100209,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051728/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256581/Selections/644051728",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": true,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256580,
        "externalId": 257231885,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580",
        "selections": [
            {
                "id": 644051677,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100393,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051677/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051677",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051676,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100392,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051676/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051676",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051664,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100380,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051664/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051664",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051674,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100390,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051674/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051674",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051669,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100385,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051669/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051669",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051665,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100381,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051665/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051665",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051675,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100391,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051675/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051675",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051672,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100388,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051672/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051672",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051662,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100378,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051662/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051662",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051673,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100389,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051673/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051673",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351860,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632150,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644351860/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644351860",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051678,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100394,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051678/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051678",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051666,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100382,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051666/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051666",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051668,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100384,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051668/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051668",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051667,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100383,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051667/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051667",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051671,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100387,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051671/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051671",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051670,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100386,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051670/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051670",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051695,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192100411,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051695/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051695",
                "outcomeVariants": []
            },
            {
                "id": 644051679,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100395,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051679/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051679",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051686,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100402,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051686/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051686",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051689,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100405,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051689/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051689",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051685,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100401,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051685/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051685",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051693,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100409,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051693/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051693",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051688,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100404,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051688/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051688",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051692,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100408,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051692/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051692",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051684,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100400,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051684/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051684",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051687,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100403,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051687/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051687",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360288,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644968,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644360288/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644360288",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051682,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100398,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051682/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051682",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360283,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644967,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644360283/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644360283",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051680,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100396,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051680/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051680",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051683,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100399,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051683/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051683",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051691,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100407,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051691/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051691",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051694,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100410,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051694/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051694",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051681,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100397,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051681/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256580/Selections/644051681",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256668,
        "externalId": 257231944,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668",
        "selections": [
            {
                "id": 644052847,
                "name": "1st: Brian To'o, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101213,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052847/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052847",
                "outcomeVariants": []
            },
            {
                "id": 644052852,
                "name": "1st: Brian To'o, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101218,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052852/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052852",
                "outcomeVariants": []
            },
            {
                "id": 644052766,
                "name": "1st: Josh Addo-Carr, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192101132,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052766/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052766",
                "outcomeVariants": []
            },
            {
                "id": 644052856,
                "name": "1st: Brian To'o, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192101222,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052856/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052856",
                "outcomeVariants": []
            },
            {
                "id": 644052855,
                "name": "1st: Brian To'o, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192101221,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052855/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052855",
                "outcomeVariants": []
            },
            {
                "id": 644052848,
                "name": "1st: Brian To'o, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192101214,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052848/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052848",
                "outcomeVariants": []
            },
            {
                "id": 644052846,
                "name": "1st: Charlie Staines, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192101212,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052846/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052846",
                "outcomeVariants": []
            },
            {
                "id": 644052845,
                "name": "1st: Charlie Staines, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192101211,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052845/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052845",
                "outcomeVariants": []
            },
            {
                "id": 644052837,
                "name": "1st: Charlie Staines, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101203,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052837/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052837",
                "outcomeVariants": []
            },
            {
                "id": 644052765,
                "name": "1st: Josh Addo-Carr, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192101131,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052765/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052765",
                "outcomeVariants": []
            },
            {
                "id": 644052758,
                "name": "1st: Josh Addo-Carr, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192101124,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052758/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052758",
                "outcomeVariants": []
            },
            {
                "id": 644052757,
                "name": "1st: Josh Addo-Carr, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101123,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052757/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052757",
                "outcomeVariants": []
            },
            {
                "id": 644052849,
                "name": "1st: Brian To'o, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192101215,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052849/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052849",
                "outcomeVariants": []
            },
            {
                "id": 644052775,
                "name": "1st: George Jennings, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192101141,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052775/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052775",
                "outcomeVariants": []
            },
            {
                "id": 644052838,
                "name": "1st: Charlie Staines, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192101204,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052838/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052838",
                "outcomeVariants": []
            },
            {
                "id": 644052839,
                "name": "1st: Charlie Staines, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192101205,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052839/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052839",
                "outcomeVariants": []
            },
            {
                "id": 644052776,
                "name": "1st: George Jennings, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192101142,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052776/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052776",
                "outcomeVariants": []
            },
            {
                "id": 644052767,
                "name": "1st: George Jennings, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101133,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052767/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052767",
                "outcomeVariants": []
            },
            {
                "id": 644052769,
                "name": "1st: George Jennings, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192101135,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052769/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052769",
                "outcomeVariants": []
            },
            {
                "id": 644360337,
                "name": "1st: George Jennings, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644984,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360337/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360337",
                "outcomeVariants": []
            },
            {
                "id": 644052759,
                "name": "1st: Josh Addo-Carr, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192101125,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052759/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052759",
                "outcomeVariants": []
            },
            {
                "id": 644360317,
                "name": "1st: Josh Addo-Carr, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644973,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360317/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360317",
                "outcomeVariants": []
            },
            {
                "id": 644052762,
                "name": "1st: Josh Addo-Carr, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101128,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052762/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052762",
                "outcomeVariants": []
            },
            {
                "id": 644052785,
                "name": "1st: Justin Olam, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192101151,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052785/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052785",
                "outcomeVariants": []
            },
            {
                "id": 644052777,
                "name": "1st: Justin Olam, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101143,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052777/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052777",
                "outcomeVariants": []
            },
            {
                "id": 644052815,
                "name": "1st: Stephen Crichton, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192101181,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052815/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052815",
                "outcomeVariants": []
            },
            {
                "id": 644052807,
                "name": "1st: Stephen Crichton, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101173,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052807/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052807",
                "outcomeVariants": []
            },
            {
                "id": 644360347,
                "name": "1st: Brian To'o, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644991,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360347/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360347",
                "outcomeVariants": []
            },
            {
                "id": 644052842,
                "name": "1st: Charlie Staines, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101208,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052842/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052842",
                "outcomeVariants": []
            },
            {
                "id": 644052768,
                "name": "1st: George Jennings, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192101134,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052768/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052768",
                "outcomeVariants": []
            },
            {
                "id": 644052772,
                "name": "1st: George Jennings, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101138,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052772/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052772",
                "outcomeVariants": []
            },
            {
                "id": 644052786,
                "name": "1st: Justin Olam, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192101152,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052786/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052786",
                "outcomeVariants": []
            },
            {
                "id": 644360335,
                "name": "1st: Nicho Hynes, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192644983,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360335/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360335",
                "outcomeVariants": []
            },
            {
                "id": 644360333,
                "name": "1st: Nicho Hynes, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192644982,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360333/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360333",
                "outcomeVariants": []
            },
            {
                "id": 644360318,
                "name": "1st: Nicho Hynes, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192644974,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360318/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360318",
                "outcomeVariants": []
            },
            {
                "id": 644052836,
                "name": "1st: Paul Momirovski, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192101202,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052836/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052836",
                "outcomeVariants": []
            },
            {
                "id": 644052816,
                "name": "1st: Stephen Crichton, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192101182,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052816/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052816",
                "outcomeVariants": []
            },
            {
                "id": 644052808,
                "name": "1st: Stephen Crichton, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192101174,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052808/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052808",
                "outcomeVariants": []
            },
            {
                "id": 644052809,
                "name": "1st: Stephen Crichton, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192101175,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052809/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052809",
                "outcomeVariants": []
            },
            {
                "id": 644052812,
                "name": "1st: Stephen Crichton, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101178,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052812/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052812",
                "outcomeVariants": []
            },
            {
                "id": 644052853,
                "name": "1st: Brian To'o, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101219,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052853/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052853",
                "outcomeVariants": []
            },
            {
                "id": 644052854,
                "name": "1st: Brian To'o, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101220,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052854/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052854",
                "outcomeVariants": []
            },
            {
                "id": 644052843,
                "name": "1st: Charlie Staines, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101209,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052843/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052843",
                "outcomeVariants": []
            },
            {
                "id": 644360346,
                "name": "1st: Charlie Staines, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644990,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360346/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360346",
                "outcomeVariants": []
            },
            {
                "id": 644052778,
                "name": "1st: Justin Olam, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192101144,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052778/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052778",
                "outcomeVariants": []
            },
            {
                "id": 644052782,
                "name": "1st: Justin Olam, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101148,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052782/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052782",
                "outcomeVariants": []
            },
            {
                "id": 644360321,
                "name": "1st: Nicho Hynes, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192644976,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360321/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360321",
                "outcomeVariants": []
            },
            {
                "id": 644052827,
                "name": "1st: Paul Momirovski, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101193,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052827/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052827",
                "outcomeVariants": []
            },
            {
                "id": 644052797,
                "name": "1st: Reimis Smith, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101163,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 151,
                    "winPriceNum": 150000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052797/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052797",
                "outcomeVariants": []
            },
            {
                "id": 644052826,
                "name": "1st: Dylan Edwards, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192101192,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052826/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052826",
                "outcomeVariants": []
            },
            {
                "id": 644052825,
                "name": "1st: Dylan Edwards, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192101191,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052825/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052825",
                "outcomeVariants": []
            },
            {
                "id": 644052764,
                "name": "1st: Josh Addo-Carr, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101130,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052764/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052764",
                "outcomeVariants": []
            },
            {
                "id": 644052761,
                "name": "1st: Josh Addo-Carr, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192101127,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052761/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052761",
                "outcomeVariants": []
            },
            {
                "id": 644052828,
                "name": "1st: Paul Momirovski, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192101194,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052828/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052828",
                "outcomeVariants": []
            },
            {
                "id": 644052806,
                "name": "1st: Reimis Smith, 2nd: Brian To'o",
                "resultType": "-",
                "externalId": 1192101172,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052806/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052806",
                "outcomeVariants": []
            },
            {
                "id": 644052805,
                "name": "1st: Reimis Smith, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192101171,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052805/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052805",
                "outcomeVariants": []
            },
            {
                "id": 644052798,
                "name": "1st: Reimis Smith, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192101164,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052798/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052798",
                "outcomeVariants": []
            },
            {
                "id": 644360343,
                "name": "1st: Stephen Crichton, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644987,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360343/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360343",
                "outcomeVariants": []
            },
            {
                "id": 644052851,
                "name": "1st: Brian To'o, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192101217,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052851/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052851",
                "outcomeVariants": []
            },
            {
                "id": 644052844,
                "name": "1st: Charlie Staines, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101210,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052844/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052844",
                "outcomeVariants": []
            },
            {
                "id": 644052763,
                "name": "1st: Josh Addo-Carr, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101129,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052763/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052763",
                "outcomeVariants": []
            },
            {
                "id": 644360326,
                "name": "1st: Nicho Hynes, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192644979,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360326/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360326",
                "outcomeVariants": []
            },
            {
                "id": 644052835,
                "name": "1st: Paul Momirovski, 2nd: Charlie Staines",
                "resultType": "-",
                "externalId": 1192101201,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052835/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052835",
                "outcomeVariants": []
            },
            {
                "id": 644052802,
                "name": "1st: Reimis Smith, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101168,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052802/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052802",
                "outcomeVariants": []
            },
            {
                "id": 644052813,
                "name": "1st: Stephen Crichton, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101179,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052813/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052813",
                "outcomeVariants": []
            },
            {
                "id": 644052811,
                "name": "1st: Stephen Crichton, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192101177,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052811/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052811",
                "outcomeVariants": []
            },
            {
                "id": 644052841,
                "name": "1st: Charlie Staines, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192101207,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052841/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052841",
                "outcomeVariants": []
            },
            {
                "id": 644052817,
                "name": "1st: Dylan Edwards, 2nd: Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101183,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052817/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052817",
                "outcomeVariants": []
            },
            {
                "id": 644052822,
                "name": "1st: Dylan Edwards, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101188,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052822/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052822",
                "outcomeVariants": []
            },
            {
                "id": 644052771,
                "name": "1st: George Jennings, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192101137,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052771/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052771",
                "outcomeVariants": []
            },
            {
                "id": 644052779,
                "name": "1st: Justin Olam, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192101145,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052779/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052779",
                "outcomeVariants": []
            },
            {
                "id": 644360340,
                "name": "1st: Justin Olam, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644985,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360340/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360340",
                "outcomeVariants": []
            },
            {
                "id": 644052781,
                "name": "1st: Justin Olam, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192101147,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052781/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052781",
                "outcomeVariants": []
            },
            {
                "id": 644052834,
                "name": "1st: Paul Momirovski, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101200,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052834/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052834",
                "outcomeVariants": []
            },
            {
                "id": 644052799,
                "name": "1st: Reimis Smith, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192101165,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052799/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052799",
                "outcomeVariants": []
            },
            {
                "id": 644052773,
                "name": "1st: George Jennings, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101139,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052773/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052773",
                "outcomeVariants": []
            },
            {
                "id": 644052784,
                "name": "1st: Justin Olam, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101150,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052784/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052784",
                "outcomeVariants": []
            },
            {
                "id": 644360328,
                "name": "1st: Nicho Hynes, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192644980,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 251,
                    "winPriceNum": 250000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360328/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360328",
                "outcomeVariants": []
            },
            {
                "id": 644052818,
                "name": "1st: Dylan Edwards, 2nd: George Jennings",
                "resultType": "-",
                "externalId": 1192101184,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052818/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052818",
                "outcomeVariants": []
            },
            {
                "id": 644052819,
                "name": "1st: Dylan Edwards, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192101185,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052819/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052819",
                "outcomeVariants": []
            },
            {
                "id": 644360344,
                "name": "1st: Dylan Edwards, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644988,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360344/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360344",
                "outcomeVariants": []
            },
            {
                "id": 644052774,
                "name": "1st: George Jennings, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101140,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052774/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052774",
                "outcomeVariants": []
            },
            {
                "id": 644052829,
                "name": "1st: Paul Momirovski, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192101195,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 276,
                    "winPriceNum": 275000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052829/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052829",
                "outcomeVariants": []
            },
            {
                "id": 644360320,
                "name": "1st: Nicho Hynes, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644975,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360320/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360320",
                "outcomeVariants": []
            },
            {
                "id": 644360322,
                "name": "1st: Nicho Hynes, 2nd: Justin Olam",
                "resultType": "-",
                "externalId": 1192644977,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360322/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360322",
                "outcomeVariants": []
            },
            {
                "id": 644360324,
                "name": "1st: Nicho Hynes, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192644978,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360324/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360324",
                "outcomeVariants": []
            },
            {
                "id": 644052833,
                "name": "1st: Paul Momirovski, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101199,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052833/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052833",
                "outcomeVariants": []
            },
            {
                "id": 644052832,
                "name": "1st: Paul Momirovski, 2nd: Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101198,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052832/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052832",
                "outcomeVariants": []
            },
            {
                "id": 644052803,
                "name": "1st: Reimis Smith, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101169,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052803/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052803",
                "outcomeVariants": []
            },
            {
                "id": 644360342,
                "name": "1st: Reimis Smith, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644986,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360342/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360342",
                "outcomeVariants": []
            },
            {
                "id": 644052814,
                "name": "1st: Stephen Crichton, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101180,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 326,
                    "winPriceNum": 325000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052814/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052814",
                "outcomeVariants": []
            },
            {
                "id": 644360332,
                "name": "1st: Nicho Hynes, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192644981,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360332/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360332",
                "outcomeVariants": []
            },
            {
                "id": 644360345,
                "name": "1st: Paul Momirovski, 2nd: Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644989,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360345/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644360345",
                "outcomeVariants": []
            },
            {
                "id": 644052804,
                "name": "1st: Reimis Smith, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101170,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 376,
                    "winPriceNum": 375000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052804/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052804",
                "outcomeVariants": []
            },
            {
                "id": 644052783,
                "name": "1st: Justin Olam, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101149,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052783/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052783",
                "outcomeVariants": []
            },
            {
                "id": 644052801,
                "name": "1st: Reimis Smith, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192101167,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052801/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052801",
                "outcomeVariants": []
            },
            {
                "id": 644052823,
                "name": "1st: Dylan Edwards, 2nd: Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101189,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052823/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052823",
                "outcomeVariants": []
            },
            {
                "id": 644052824,
                "name": "1st: Dylan Edwards, 2nd: Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101190,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052824/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052824",
                "outcomeVariants": []
            },
            {
                "id": 644052821,
                "name": "1st: Dylan Edwards, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192101187,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052821/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052821",
                "outcomeVariants": []
            },
            {
                "id": 644052831,
                "name": "1st: Paul Momirovski, 2nd: Reimis Smith",
                "resultType": "-",
                "externalId": 1192101197,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052831/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256668/Selections/644052831",
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
        "id": 121256596,
        "externalId": 257231945,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596",
        "selections": [
            {
                "id": 644052020,
                "name": "Josh Addo-Carr / Brian To'o",
                "resultType": "-",
                "externalId": 1192101232,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052020/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052020",
                "outcomeVariants": []
            },
            {
                "id": 644052064,
                "name": "Charlie Staines / Brian To'o",
                "resultType": "-",
                "externalId": 1192101276,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052064/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052064",
                "outcomeVariants": []
            },
            {
                "id": 644052019,
                "name": "Josh Addo-Carr / Charlie Staines",
                "resultType": "-",
                "externalId": 1192101231,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052019/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052019",
                "outcomeVariants": []
            },
            {
                "id": 644052029,
                "name": "George Jennings / Brian To'o",
                "resultType": "-",
                "externalId": 1192101241,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052029/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052029",
                "outcomeVariants": []
            },
            {
                "id": 644052028,
                "name": "George Jennings / Charlie Staines",
                "resultType": "-",
                "externalId": 1192101240,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052028/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052028",
                "outcomeVariants": []
            },
            {
                "id": 644052012,
                "name": "Josh Addo-Carr / George Jennings",
                "resultType": "-",
                "externalId": 1192101224,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052012/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052012",
                "outcomeVariants": []
            },
            {
                "id": 644052055,
                "name": "Stephen Crichton / Brian To'o",
                "resultType": "-",
                "externalId": 1192101267,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052055/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052055",
                "outcomeVariants": []
            },
            {
                "id": 644052013,
                "name": "Josh Addo-Carr / Justin Olam",
                "resultType": "-",
                "externalId": 1192101225,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052013/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052013",
                "outcomeVariants": []
            },
            {
                "id": 644052016,
                "name": "Josh Addo-Carr / Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101228,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052016/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052016",
                "outcomeVariants": []
            },
            {
                "id": 644052037,
                "name": "Justin Olam / Brian To'o",
                "resultType": "-",
                "externalId": 1192101249,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052037/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052037",
                "outcomeVariants": []
            },
            {
                "id": 644360298,
                "name": "Josh Addo-Carr / Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644992,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360298/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360298",
                "outcomeVariants": []
            },
            {
                "id": 644052036,
                "name": "Justin Olam / Charlie Staines",
                "resultType": "-",
                "externalId": 1192101248,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052036/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052036",
                "outcomeVariants": []
            },
            {
                "id": 644052054,
                "name": "Stephen Crichton / Charlie Staines",
                "resultType": "-",
                "externalId": 1192101266,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052054/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052054",
                "outcomeVariants": []
            },
            {
                "id": 644052022,
                "name": "George Jennings / Justin Olam",
                "resultType": "-",
                "externalId": 1192101234,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052022/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052022",
                "outcomeVariants": []
            },
            {
                "id": 644052025,
                "name": "George Jennings / Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101237,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052025/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052025",
                "outcomeVariants": []
            },
            {
                "id": 644360307,
                "name": "Nicho Hynes / George Jennings",
                "resultType": "-",
                "externalId": 1192644994,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360307/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360307",
                "outcomeVariants": []
            },
            {
                "id": 644360316,
                "name": "Nicho Hynes / Brian To'o",
                "resultType": "-",
                "externalId": 1192645001,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360316/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360316",
                "outcomeVariants": []
            },
            {
                "id": 644052033,
                "name": "Justin Olam / Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101245,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052033/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052033",
                "outcomeVariants": []
            },
            {
                "id": 644360315,
                "name": "Nicho Hynes / Charlie Staines",
                "resultType": "-",
                "externalId": 1192645000,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360315/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360315",
                "outcomeVariants": []
            },
            {
                "id": 644052062,
                "name": "Paul Momirovski / Brian To'o",
                "resultType": "-",
                "externalId": 1192101274,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 76,
                    "winPriceNum": 75000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052062/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052062",
                "outcomeVariants": []
            },
            {
                "id": 644052065,
                "name": "Brian To'o / Brian To'o",
                "resultType": "-",
                "externalId": 1192101277,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052065/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052065",
                "outcomeVariants": []
            },
            {
                "id": 644052063,
                "name": "Charlie Staines / Charlie Staines",
                "resultType": "-",
                "externalId": 1192101275,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052063/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052063",
                "outcomeVariants": []
            },
            {
                "id": 644052059,
                "name": "Dylan Edwards / Brian To'o",
                "resultType": "-",
                "externalId": 1192101271,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052059/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052059",
                "outcomeVariants": []
            },
            {
                "id": 644052058,
                "name": "Dylan Edwards / Charlie Staines",
                "resultType": "-",
                "externalId": 1192101270,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052058/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052058",
                "outcomeVariants": []
            },
            {
                "id": 644052011,
                "name": "Josh Addo-Carr / Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101223,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052011/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052011",
                "outcomeVariants": []
            },
            {
                "id": 644052018,
                "name": "Josh Addo-Carr / Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101230,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052018/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052018",
                "outcomeVariants": []
            },
            {
                "id": 644052015,
                "name": "Josh Addo-Carr / Reimis Smith",
                "resultType": "-",
                "externalId": 1192101227,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 81,
                    "winPriceNum": 80000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052015/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052015",
                "outcomeVariants": []
            },
            {
                "id": 644052050,
                "name": "Reimis Smith / Brian To'o",
                "resultType": "-",
                "externalId": 1192101262,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 91,
                    "winPriceNum": 90000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052050/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052050",
                "outcomeVariants": []
            },
            {
                "id": 644052027,
                "name": "George Jennings / Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101239,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052027/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052027",
                "outcomeVariants": []
            },
            {
                "id": 644052024,
                "name": "George Jennings / Reimis Smith",
                "resultType": "-",
                "externalId": 1192101236,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052024/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052024",
                "outcomeVariants": []
            },
            {
                "id": 644052017,
                "name": "Josh Addo-Carr / Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101229,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052017/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052017",
                "outcomeVariants": []
            },
            {
                "id": 644052032,
                "name": "Justin Olam / Reimis Smith",
                "resultType": "-",
                "externalId": 1192101244,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052032/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052032",
                "outcomeVariants": []
            },
            {
                "id": 644360312,
                "name": "Nicho Hynes / Stephen Crichton",
                "resultType": "-",
                "externalId": 1192644997,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360312/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360312",
                "outcomeVariants": []
            },
            {
                "id": 644052061,
                "name": "Paul Momirovski / Charlie Staines",
                "resultType": "-",
                "externalId": 1192101273,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052061/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052061",
                "outcomeVariants": []
            },
            {
                "id": 644052049,
                "name": "Reimis Smith / Charlie Staines",
                "resultType": "-",
                "externalId": 1192101261,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052049/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052049",
                "outcomeVariants": []
            },
            {
                "id": 644052046,
                "name": "Reimis Smith / Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101258,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052046/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052046",
                "outcomeVariants": []
            },
            {
                "id": 644052052,
                "name": "Stephen Crichton / Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101264,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052052/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052052",
                "outcomeVariants": []
            },
            {
                "id": 644052026,
                "name": "George Jennings / Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101238,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052026/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052026",
                "outcomeVariants": []
            },
            {
                "id": 644052021,
                "name": "George Jennings / George Jennings",
                "resultType": "-",
                "externalId": 1192101233,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052021/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052021",
                "outcomeVariants": []
            },
            {
                "id": 644052035,
                "name": "Justin Olam / Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101247,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052035/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052035",
                "outcomeVariants": []
            },
            {
                "id": 644360313,
                "name": "Nicho Hynes / Dylan Edwards",
                "resultType": "-",
                "externalId": 1192644998,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360313/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360313",
                "outcomeVariants": []
            },
            {
                "id": 644360309,
                "name": "Nicho Hynes / Justin Olam",
                "resultType": "-",
                "externalId": 1192644995,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360309/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360309",
                "outcomeVariants": []
            },
            {
                "id": 644052051,
                "name": "Stephen Crichton / Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101263,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 126,
                    "winPriceNum": 125000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052051/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052051",
                "outcomeVariants": []
            },
            {
                "id": 644052034,
                "name": "Justin Olam / Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101246,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052034/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052034",
                "outcomeVariants": []
            },
            {
                "id": 644360311,
                "name": "Nicho Hynes / Reimis Smith",
                "resultType": "-",
                "externalId": 1192644996,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360311/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360311",
                "outcomeVariants": []
            },
            {
                "id": 644052053,
                "name": "Stephen Crichton / Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101265,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 176,
                    "winPriceNum": 175000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052053/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052053",
                "outcomeVariants": []
            },
            {
                "id": 644052057,
                "name": "Dylan Edwards / Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101269,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052057/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052057",
                "outcomeVariants": []
            },
            {
                "id": 644360314,
                "name": "Nicho Hynes / Paul Momirovski",
                "resultType": "-",
                "externalId": 1192644999,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360314/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360314",
                "outcomeVariants": []
            },
            {
                "id": 644052047,
                "name": "Reimis Smith / Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101259,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052047/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052047",
                "outcomeVariants": []
            },
            {
                "id": 644052030,
                "name": "Justin Olam / Justin Olam",
                "resultType": "-",
                "externalId": 1192101242,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052030/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052030",
                "outcomeVariants": []
            },
            {
                "id": 644052060,
                "name": "Paul Momirovski / Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101272,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052060/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052060",
                "outcomeVariants": []
            },
            {
                "id": 644052048,
                "name": "Reimis Smith / Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101260,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 226,
                    "winPriceNum": 225000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052048/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052048",
                "outcomeVariants": []
            },
            {
                "id": 644360304,
                "name": "Nicho Hynes / Nicho Hynes",
                "resultType": "-",
                "externalId": 1192644993,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 301,
                    "winPriceNum": 300000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360304/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644360304",
                "outcomeVariants": []
            },
            {
                "id": 644052045,
                "name": "Reimis Smith / Reimis Smith",
                "resultType": "-",
                "externalId": 1192101257,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 426,
                    "winPriceNum": 425000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052045/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052045",
                "outcomeVariants": []
            },
            {
                "id": 644052056,
                "name": "Dylan Edwards / Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101268,
                "sort": 0,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052056/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256596/Selections/644052056",
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
        "id": 121256585,
        "externalId": 257231875,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585",
        "selections": [
            {
                "id": 644051829,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100091,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051829/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051829",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051828,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100090,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051828/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051828",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051816,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100078,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051816/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051816",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051826,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100088,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051826/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051826",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051821,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100083,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051821/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051821",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051817,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100079,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051817/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051817",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051827,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100089,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051827/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051827",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051824,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100086,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051824/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051824",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051825,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100087,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051825/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051825",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051814,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100076,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051814/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051814",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351862,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632141,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644351862/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644351862",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051830,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100092,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051830/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051830",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051818,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100080,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051818/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051818",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051820,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100082,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051820/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051820",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051819,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100081,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051819/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051819",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051823,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100085,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051823/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051823",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051822,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100084,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051822/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051822",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051847,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192100109,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051847/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051847",
                "outcomeVariants": []
            },
            {
                "id": 644051831,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100093,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051831/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051831",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051838,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100100,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051838/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051838",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051841,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100103,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051841/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051841",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051837,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100099,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051837/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051837",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051840,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100102,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051840/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051840",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051845,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100107,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051845/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051845",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051844,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100106,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051844/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051844",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051836,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100098,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051836/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051836",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051839,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100101,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051839/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051839",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360290,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644950,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644360290/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644360290",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051834,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100096,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051834/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051834",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360284,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644949,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644360284/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644360284",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051835,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100097,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051835/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051835",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051832,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100094,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051832/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051832",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051843,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100105,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051843/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051843",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051833,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100095,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051833/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051833",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051846,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100108,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051846/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256585/Selections/644051846",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256589,
        "externalId": 257231876,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589",
        "selections": [
            {
                "id": 644051946,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100125,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051946/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051946",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051945,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100124,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051945/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051945",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051933,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100112,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051933/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051933",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051943,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100122,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051943/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051943",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051938,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100117,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051938/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051938",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051944,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100123,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051944/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051944",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051934,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100113,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051934/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051934",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051941,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100120,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051941/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051941",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051942,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100121,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051942/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051942",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051931,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100110,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051931/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051931",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351873,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632142,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644351873/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644351873",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051947,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100126,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051947/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051947",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051935,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100114,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051935/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051935",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051937,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100116,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051937/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051937",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051940,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100119,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051940/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051940",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051939,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100118,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051939/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051939",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051936,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100115,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051936/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051936",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051964,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192100143,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051964/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051964",
                "outcomeVariants": []
            },
            {
                "id": 644051948,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100127,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051948/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051948",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051955,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100134,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051955/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051955",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051958,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100137,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051958/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051958",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051954,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100133,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051954/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051954",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051962,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100141,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051962/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051962",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051957,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100136,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051957/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051957",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051961,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100140,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051961/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051961",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051956,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100135,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051956/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051956",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051953,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100132,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051953/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051953",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360303,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644952,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644360303/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644360303",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051951,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100130,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051951/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051951",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360297,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644951,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644360297/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644360297",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051952,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100131,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051952/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051952",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051949,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100128,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 41,
                    "winPriceNum": 40000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051949/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051949",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051963,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100142,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051963/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051963",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051960,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100139,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051960/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051960",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051950,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100129,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 56,
                    "winPriceNum": 55000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051950/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256589/Selections/644051950",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256582,
        "externalId": 257231883,
        "name": "First Tryscorer - Penrith Panthers",
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582",
        "selections": [
            {
                "id": 644051744,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100358,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051744/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051744",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051743,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100357,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051743/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051743",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051731,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100345,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051731/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051731",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051741,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100355,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051741/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051741",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051736,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100350,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051736/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051736",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051732,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100346,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051732/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051732",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051742,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100356,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051742/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051742",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051739,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100353,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051739/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051739",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051740,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100354,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051740/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051740",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051729,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100343,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051729/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051729",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351857,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632149,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644351857/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644351857",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051745,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100359,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051745/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051745",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051733,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100347,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051733/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051733",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051735,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100349,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051735/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051735",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051746,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192100360,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051746/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051746",
                "outcomeVariants": []
            },
            {
                "id": 644051734,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100348,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051734/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051734",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051738,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100352,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051738/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051738",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051737,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100351,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051737/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256582/Selections/644051737",
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
        "id": 121256586,
        "externalId": 257231884,
        "name": "First Tryscorer - Melbourne Storm",
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586",
        "selections": [
            {
                "id": 644051848,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100361,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051848/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051848",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051855,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100368,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051855/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051855",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051858,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100371,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051858/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051858",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051854,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100367,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051854/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051854",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051857,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100370,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051857/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051857",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051862,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100375,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051862/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051862",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051861,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100374,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051861/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051861",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051856,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100369,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051856/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051856",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051853,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100366,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051853/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051853",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360275,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644966,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644360275/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644360275",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051851,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100364,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051851/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051851",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360274,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644965,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644360274/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644360274",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051852,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100365,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051852/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051852",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051849,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100362,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051849/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051849",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051864,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192100377,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051864/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051864",
                "outcomeVariants": []
            },
            {
                "id": 644051860,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100373,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051860/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051860",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051850,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100363,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051850/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051850",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051863,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100376,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051863/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256586/Selections/644051863",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256636,
        "externalId": 257231914,
        "name": "Last Tryscorer - Penrith Panthers",
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636",
        "selections": [
            {
                "id": 644052516,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100521,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052516/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052516",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052515,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100520,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052515/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052515",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052503,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100508,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052503/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052503",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052513,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100518,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052513/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052513",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052508,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100513,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7.5,
                    "winPriceNum": 6500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052508/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052508",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052514,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100519,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052514/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052514",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052504,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100509,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052504/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052504",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052511,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100516,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052511/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052511",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052512,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100517,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052512/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052512",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052501,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100506,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052501/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052501",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351856,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632152,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644351856/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644351856",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052517,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100522,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052517/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052517",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052505,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100510,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052505/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052505",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052507,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100512,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052507/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052507",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052518,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192100523,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052518/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052518",
                "outcomeVariants": []
            },
            {
                "id": 644052510,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100515,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052510/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052510",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052509,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100514,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052509/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052509",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052506,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100511,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052506/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256636/Selections/644052506",
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
        "id": 121256665,
        "externalId": 257231915,
        "name": "Last Tryscorer - Melbourne Storm",
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665",
        "selections": [
            {
                "id": 644052735,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100524,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052735/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052735",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052742,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100531,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052742/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052742",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052745,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100534,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052745/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052745",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052741,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100530,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052741/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052741",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052749,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100538,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052749/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052749",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052744,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100533,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052744/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052744",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052740,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100529,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052740/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052740",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360279,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644972,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644360279/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644360279",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052748,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100537,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052748/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052748",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052738,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100527,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052738/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052738",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052743,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100532,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052743/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052743",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360276,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644971,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644360276/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644360276",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052739,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100528,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052739/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052739",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052751,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192100540,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052751/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052751",
                "outcomeVariants": []
            },
            {
                "id": 644052736,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100525,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052736/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052736",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052747,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100536,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052747/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052747",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052737,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100526,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052737/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052737",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644052750,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100539,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052750/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256665/Selections/644052750",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256578,
        "externalId": 257231882,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578",
        "selections": [
            {
                "id": 644051609,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100323,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051609/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051609",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051610,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100324,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051610/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051610",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051597,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100311,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051597/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051597",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051607,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100321,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051607/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051607",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051602,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100316,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051602/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051602",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051608,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100322,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051608/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051608",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051598,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100312,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051598/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051598",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051605,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100319,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051605/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051605",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051595,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100309,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051595/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051595",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051606,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100320,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051606/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051606",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351865,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632148,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644351865/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644351865",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051611,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100325,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051611/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051611",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051599,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100313,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051599/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051599",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051601,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100315,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 36,
                    "winPriceNum": 35000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051601/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051601",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051604,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100318,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051604/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051604",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051603,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100317,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 61,
                    "winPriceNum": 60000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051603/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051603",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051600,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100314,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 71,
                    "winPriceNum": 70000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051600/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051600",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051628,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192100342,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 101,
                    "winPriceNum": 100000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051628/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051628",
                "outcomeVariants": []
            },
            {
                "id": 644051612,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100326,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051612/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051612",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051619,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100333,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051619/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051619",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051622,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100336,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051622/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051622",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051618,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100332,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051618/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051618",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051621,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100335,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051621/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051621",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051626,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100340,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 19,
                    "winPriceNum": 18000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051626/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051626",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051625,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100339,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051625/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051625",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051617,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100331,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051617/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051617",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051620,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100334,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051620/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051620",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360300,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644964,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644360300/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644360300",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360296,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644963,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644360296/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644360296",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051615,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100329,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051615/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051615",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051616,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100330,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 31,
                    "winPriceNum": 30000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051616/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051616",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051613,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100327,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 46,
                    "winPriceNum": 45000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051613/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051613",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051624,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100338,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051624/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051624",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051614,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100328,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 51,
                    "winPriceNum": 50000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051614/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051614",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051627,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100341,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 67,
                    "winPriceNum": 66000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051627/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256578/Selections/644051627",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": true,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256590,
        "externalId": 257231886,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590",
        "selections": [
            {
                "id": 644051980,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192100427,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051980/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051980",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051979,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192100426,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 5,
                    "winPriceNum": 4000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051979/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051979",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051967,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192100414,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051967/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051967",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051977,
                "name": "Tyrone May",
                "resultType": "-",
                "externalId": 1192100424,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051977/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051977",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051972,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192100419,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051972/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051972",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051978,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192100425,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051978/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051978",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051968,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192100415,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 11,
                    "winPriceNum": 10000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051968/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051968",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051975,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192100422,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051975/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051975",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051965,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192100412,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051965/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051965",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051976,
                "name": "Liam Martin",
                "resultType": "-",
                "externalId": 1192100423,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051976/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051976",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644351867,
                "name": "Matt Burton",
                "resultType": "-",
                "externalId": 1192632151,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644351867/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644351867",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051981,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192100428,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051981/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051981",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051969,
                "name": "Matt Eisenhuth",
                "resultType": "-",
                "externalId": 1192100416,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 18,
                    "winPriceNum": 17000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051969/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051969",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051971,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192100418,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 20,
                    "winPriceNum": 19000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051971/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051971",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051970,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192100417,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051970/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051970",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051974,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192100421,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051974/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051974",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051973,
                "name": "Spencer Leniu",
                "resultType": "-",
                "externalId": 1192100420,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051973/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051973",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644051998,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192100445,
                "sort": 500,
                "statusCode": "A",
                "price": {
                    "winPrice": 201,
                    "winPriceNum": 200000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051998/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051998",
                "outcomeVariants": []
            },
            {
                "id": 644051982,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192100429,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051982/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051982",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051989,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192100436,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051989/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051989",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051992,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192100439,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051992/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051992",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051988,
                "name": "Nicho Hynes",
                "resultType": "-",
                "externalId": 1192100435,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 8.5,
                    "winPriceNum": 7500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051988/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051988",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051991,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192100438,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051991/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051991",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051996,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192100443,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051996/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051996",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051987,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192100434,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051987/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051987",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360292,
                "name": "Tyson Smoothy",
                "resultType": "-",
                "externalId": 1192644970,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644360292/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644360292",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051995,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192100442,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051995/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051995",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051990,
                "name": "Tui Kamikamica",
                "resultType": "-",
                "externalId": 1192100437,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 14,
                    "winPriceNum": 13000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051990/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051990",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051985,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192100432,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 15,
                    "winPriceNum": 14000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051985/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051985",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644360291,
                "name": "Chris Lewis",
                "resultType": "-",
                "externalId": 1192644969,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644360291/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644360291",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051986,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192100433,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 17,
                    "winPriceNum": 16000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051986/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051986",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051983,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192100430,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 23,
                    "winPriceNum": 22000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051983/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051983",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051994,
                "name": "Aaron Pene",
                "resultType": "-",
                "externalId": 1192100441,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051994/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051994",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051984,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192100431,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 26,
                    "winPriceNum": 25000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051984/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051984",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            },
            {
                "id": 644051997,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192100444,
                "sort": 1010,
                "statusCode": "A",
                "price": {
                    "winPrice": 34,
                    "winPriceNum": 33000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051997/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256590/Selections/644051997",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256633,
        "externalId": 257231980,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256633",
        "selections": [
            {
                "id": 644052494,
                "name": "Backs (No's 1, 2, 3, 4, 5, 6, 7)",
                "resultType": "-",
                "externalId": 1192101714,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.36,
                    "winPriceNum": 360,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256633/Selections/644052494/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256633/Selections/644052494",
                "outcomeVariants": []
            },
            {
                "id": 644052495,
                "name": "Forwards (No's 8, 9, 10, 11, 12, 13)",
                "resultType": "-",
                "externalId": 1192101715,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256633/Selections/644052495/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256633/Selections/644052495",
                "outcomeVariants": []
            },
            {
                "id": 644052496,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192101716,
                "sort": 40,
                "statusCode": "A",
                "price": {
                    "winPrice": 501,
                    "winPriceNum": 500000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256633/Selections/644052496/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256633/Selections/644052496",
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
        "id": 121256663,
        "externalId": 257231982,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256663",
        "selections": [
            {
                "id": 644052730,
                "name": "Backs (No's 1, 2, 3, 4, 5, 6, 7)",
                "resultType": "-",
                "externalId": 1192101720,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.4,
                    "winPriceNum": 400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256663/Selections/644052730/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256663/Selections/644052730",
                "outcomeVariants": []
            },
            {
                "id": 644052731,
                "name": "Forwards (No's 8, 9, 10, 11, 12, 13)",
                "resultType": "-",
                "externalId": 1192101721,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256663/Selections/644052731/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256663/Selections/644052731",
                "outcomeVariants": []
            },
            {
                "id": 644052732,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192101722,
                "sort": 40,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256663/Selections/644052732/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256663/Selections/644052732",
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
        "id": 121256644,
        "externalId": 257231983,
        "name": "Jersey Number of Storm First Tryscorer",
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256644",
        "selections": [
            {
                "id": 644052631,
                "name": "Backs (No's 1, 2, 3, 4, 5, 6, 7)",
                "resultType": "-",
                "externalId": 1192101723,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.4,
                    "winPriceNum": 400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256644/Selections/644052631/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256644/Selections/644052631",
                "outcomeVariants": []
            },
            {
                "id": 644052632,
                "name": "Forwards (No's 8, 9, 10, 11, 12, 13)",
                "resultType": "-",
                "externalId": 1192101724,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 4,
                    "winPriceNum": 3000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256644/Selections/644052632/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256644/Selections/644052632",
                "outcomeVariants": []
            },
            {
                "id": 644052633,
                "name": "No Try Scored",
                "resultType": "-",
                "externalId": 1192101725,
                "sort": 40,
                "statusCode": "A",
                "price": {
                    "winPrice": 21,
                    "winPriceNum": 20000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256644/Selections/644052633/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256644/Selections/644052633",
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
        "id": 121256657,
        "externalId": 257231928,
        "name": "Most Tries - A vs B - Group 1",
        "statusCode": "S",
        "sort": 485,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256657",
        "selections": [
            {
                "id": 644052715,
                "name": "Dylan Edwards",
                "resultType": "-",
                "externalId": 1192101078,
                "sort": 10,
                "statusCode": "S",
                "price": {
                    "winPrice": 1.001,
                    "winPriceNum": 1,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256657/Selections/644052715/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256657/Selections/644052715",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052717,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101080,
                "sort": 20,
                "statusCode": "S",
                "price": {
                    "winPrice": 1.001,
                    "winPriceNum": 1,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256657/Selections/644052717/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256657/Selections/644052717",
                "outcomeVariants": []
            },
            {
                "id": 644052716,
                "name": "Ryan Papenhuyzen",
                "resultType": "-",
                "externalId": 1192101079,
                "sort": 30,
                "statusCode": "S",
                "price": {
                    "winPrice": 1.001,
                    "winPriceNum": 1,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256657/Selections/644052716/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256657/Selections/644052716",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256624,
        "externalId": 257231929,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256624",
        "selections": [
            {
                "id": 644052370,
                "name": "Charlie Staines",
                "resultType": "-",
                "externalId": 1192101081,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.1,
                    "winPriceNum": 2100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256624/Selections/644052370/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256624/Selections/644052370",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052372,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101083,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 2,
                    "winPriceNum": 1000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256624/Selections/644052372/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256624/Selections/644052372",
                "outcomeVariants": []
            },
            {
                "id": 644052371,
                "name": "George Jennings",
                "resultType": "-",
                "externalId": 1192101082,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.4,
                    "winPriceNum": 2400,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256624/Selections/644052371/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256624/Selections/644052371",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256662,
        "externalId": 257231930,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256662",
        "selections": [
            {
                "id": 644052727,
                "name": "Brian To'o",
                "resultType": "-",
                "externalId": 1192101084,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.1,
                    "winPriceNum": 2100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256662/Selections/644052727/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256662/Selections/644052727",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052729,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101086,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 2.2,
                    "winPriceNum": 1200,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256662/Selections/644052729/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256662/Selections/644052729",
                "outcomeVariants": []
            },
            {
                "id": 644052728,
                "name": "Josh Addo-Carr",
                "resultType": "-",
                "externalId": 1192101085,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 3,
                    "winPriceNum": 2000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256662/Selections/644052728/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256662/Selections/644052728",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256601,
        "externalId": 257231931,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256601",
        "selections": [
            {
                "id": 644052117,
                "name": "Paul Momirovski",
                "resultType": "-",
                "externalId": 1192101087,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256601/Selections/644052117/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256601/Selections/644052117",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052119,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101089,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.45,
                    "winPriceNum": 450,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256601/Selections/644052119/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256601/Selections/644052119",
                "outcomeVariants": []
            },
            {
                "id": 644052118,
                "name": "Reimis Smith",
                "resultType": "-",
                "externalId": 1192101088,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256601/Selections/644052118/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256601/Selections/644052118",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256654,
        "externalId": 257231932,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256654",
        "selections": [
            {
                "id": 644052708,
                "name": "Stephen Crichton",
                "resultType": "-",
                "externalId": 1192101090,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.5,
                    "winPriceNum": 2500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256654/Selections/644052708/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256654/Selections/644052708",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052710,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101092,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.72,
                    "winPriceNum": 720,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256654/Selections/644052710/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256654/Selections/644052710",
                "outcomeVariants": []
            },
            {
                "id": 644052709,
                "name": "Justin Olam",
                "resultType": "-",
                "externalId": 1192101091,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.75,
                    "winPriceNum": 2750,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256654/Selections/644052709/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256654/Selections/644052709",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256653,
        "externalId": 257231933,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256653",
        "selections": [
            {
                "id": 644052705,
                "name": "Jarome Luai",
                "resultType": "-",
                "externalId": 1192101093,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256653/Selections/644052705/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256653/Selections/644052705",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052707,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101095,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.36,
                    "winPriceNum": 360,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256653/Selections/644052707/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256653/Selections/644052707",
                "outcomeVariants": []
            },
            {
                "id": 644052706,
                "name": "Cameron Munster",
                "resultType": "-",
                "externalId": 1192101094,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 4.5,
                    "winPriceNum": 3500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256653/Selections/644052706/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256653/Selections/644052706",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256602,
        "externalId": 257231934,
        "name": "Most Tries - A vs B - Group 7",
        "statusCode": "S",
        "sort": 515,
        "marketType": "-",
        "marketSort": "--",
        "BIR": false,
        "blurb": "Both players must start for bets to stand. Includes extra time.",
        "powerPlay": true,
        "mbsAvailable": false,
        "cashoutAvailable": false,
        "eachwayAvailable": false,
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256602",
        "selections": [
            {
                "id": 644052120,
                "name": "Nathan Cleary",
                "resultType": "-",
                "externalId": 1192101096,
                "sort": 10,
                "statusCode": "S",
                "price": {
                    "winPrice": 1.001,
                    "winPriceNum": 1,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256602/Selections/644052120/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256602/Selections/644052120",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052122,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101098,
                "sort": 20,
                "statusCode": "S",
                "price": {
                    "winPrice": 1.001,
                    "winPriceNum": 1,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256602/Selections/644052122/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256602/Selections/644052122",
                "outcomeVariants": []
            },
            {
                "id": 644052121,
                "name": "Jahrome Hughes",
                "resultType": "-",
                "externalId": 1192101097,
                "sort": 30,
                "statusCode": "S",
                "price": {
                    "winPrice": 1.001,
                    "winPriceNum": 1,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256602/Selections/644052121/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256602/Selections/644052121",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256622,
        "externalId": 257231935,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256622",
        "selections": [
            {
                "id": 644052365,
                "name": "Moses Leota",
                "resultType": "-",
                "externalId": 1192101099,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256622/Selections/644052365/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256622/Selections/644052365",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052367,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101101,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.08,
                    "winPriceNum": 80,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256622/Selections/644052367/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256622/Selections/644052367",
                "outcomeVariants": []
            },
            {
                "id": 644052366,
                "name": "Jesse Bromwich",
                "resultType": "-",
                "externalId": 1192101100,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 10,
                    "winPriceNum": 9000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256622/Selections/644052366/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256622/Selections/644052366",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256649,
        "externalId": 257231936,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256649",
        "selections": [
            {
                "id": 644052669,
                "name": "James Fisher-Harris",
                "resultType": "-",
                "externalId": 1192101102,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 12,
                    "winPriceNum": 11000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256649/Selections/644052669/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256649/Selections/644052669",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052671,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101104,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.07,
                    "winPriceNum": 70,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256649/Selections/644052671/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256649/Selections/644052671",
                "outcomeVariants": []
            },
            {
                "id": 644052670,
                "name": "Christian Welch",
                "resultType": "-",
                "externalId": 1192101103,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 13,
                    "winPriceNum": 12000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256649/Selections/644052670/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256649/Selections/644052670",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256612,
        "externalId": 257231937,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256612",
        "selections": [
            {
                "id": 644052300,
                "name": "Mitch Kenny",
                "resultType": "-",
                "externalId": 1192101105,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 8,
                    "winPriceNum": 7000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256612/Selections/644052300/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256612/Selections/644052300",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052302,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101107,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.22,
                    "winPriceNum": 220,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256612/Selections/644052302/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256612/Selections/644052302",
                "outcomeVariants": []
            },
            {
                "id": 644052301,
                "name": "Brandon Smith",
                "resultType": "-",
                "externalId": 1192101106,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 5.5,
                    "winPriceNum": 4500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256612/Selections/644052301/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256612/Selections/644052301",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256673,
        "externalId": 257231938,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256673",
        "selections": [
            {
                "id": 644053035,
                "name": "Viliame Kikau",
                "resultType": "-",
                "externalId": 1192101108,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 3.1,
                    "winPriceNum": 2100,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256673/Selections/644053035/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256673/Selections/644053035",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644053037,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101110,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.45,
                    "winPriceNum": 450,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256673/Selections/644053037/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256673/Selections/644053037",
                "outcomeVariants": []
            },
            {
                "id": 644053036,
                "name": "Thomas Eisenhuth",
                "resultType": "-",
                "externalId": 1192101109,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 9,
                    "winPriceNum": 8000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256673/Selections/644053036/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256673/Selections/644053036",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256659,
        "externalId": 257231939,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256659",
        "selections": [
            {
                "id": 644052720,
                "name": "Kurt Capewell",
                "resultType": "-",
                "externalId": 1192101111,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 6,
                    "winPriceNum": 5000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256659/Selections/644052720/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256659/Selections/644052720",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052722,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101113,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.25,
                    "winPriceNum": 250,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256659/Selections/644052722/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256659/Selections/644052722",
                "outcomeVariants": []
            },
            {
                "id": 644052721,
                "name": "Kenny Bromwich",
                "resultType": "-",
                "externalId": 1192101112,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 6.5,
                    "winPriceNum": 5500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256659/Selections/644052721/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256659/Selections/644052721",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
            }
        ],
        "sameGameMultiEnabled": false,
        "sameGameMultiExpanded": false,
        "sameMarketMultiEnabled": false,
        "accMax": 20,
        "accRestriction": "-"
    },
    {
        "id": 121256606,
        "externalId": 257231940,
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
        "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256606",
        "selections": [
            {
                "id": 644052157,
                "name": "Isaah Yeo",
                "resultType": "-",
                "externalId": 1192101114,
                "sort": 10,
                "statusCode": "A",
                "price": {
                    "winPrice": 7,
                    "winPriceNum": 6000,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256606/Selections/644052157/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256606/Selections/644052157",
                "outcomeVariants": [],
                "multiplesKey": "penrithpanthrl"
            },
            {
                "id": 644052159,
                "name": "Tie (Includes 0-0 Tries)",
                "resultType": "-",
                "externalId": 1192101116,
                "sort": 20,
                "statusCode": "A",
                "price": {
                    "winPrice": 1.14,
                    "winPriceNum": 140,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256606/Selections/644052159/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256606/Selections/644052159",
                "outcomeVariants": []
            },
            {
                "id": 644052158,
                "name": "Nelson Asofa-Solomona",
                "resultType": "-",
                "externalId": 1192101115,
                "sort": 30,
                "statusCode": "A",
                "price": {
                    "winPrice": 9.5,
                    "winPriceNum": 8500,
                    "winPriceDen": 1000,
                    "priceCode": "L",
                    "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256606/Selections/644052158/Prices/L"
                },
                "topicLink": "Sportsbet/Sportsbook/Sports/23/Competitions/3436/Events/5730632/Markets/121256606/Selections/644052158",
                "outcomeVariants": [],
                "multiplesKey": "melbournestorl"
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
# In the code below I am tranforming the JSON content in a python content. SO I can work with it tranforming it in dictonaries and lists
data = json.loads(markets_in_json)

# here we are just checking what kind of data we have received from the JSON content. It will be a lists
print("----------------")
print()
print()
print("JSON content data type and lenght: ")
print(type(data))
print(len(data))
print("----------------")
print()

# converting the second index of the list in a dictionary, where I can find the Anytime Scorer data.
anytime_tryscorer_dict = dict(data[1])
print("Anytime Scorer data type and lenght: ")
print(type(anytime_tryscorer_dict))
print(len(anytime_tryscorer_dict))
print("----------------")
print()

# Here I am printing the data keys of the dictionary so I know how to access the data I want.
# In this case, I will want to access the data NAME that gives me the ANYTIME SCORER, however, it will be a list nested wich I will have to treat later
print("Anytime Scorer keys: ")
print(anytime_tryscorer_dict.keys())
print("----------------")
print()

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
