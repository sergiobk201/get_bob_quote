import requests

url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
headers = {
    'Content-Type': 'application/json'
}
data = {
    'asset': 'USDT',
    'fiat': 'BOB',
    'tradeType': 'BUY',
    'page': 1,
    'rows': 1
}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    ads = response.json().get('data', [])
    if ads:
        first_ad = ads[0]
        price = first_ad['adv']['price']
        print(f"Exchange Rate: {price} BOB/USDT")
    else:
        print("No advertisements found.")
else:
    print(f"Error: {response.status_code}")