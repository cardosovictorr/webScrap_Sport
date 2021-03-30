import requests

x = requests.get(
    'https://www.sportsbet.com.au/apigw/sportsbook-sports/Sportsbook/Sports/Events/5730632/MarketGroupings/112/Markets')
print(x.status_code)
