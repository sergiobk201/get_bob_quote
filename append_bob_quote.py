import requests
import pandas as pd
from datetime import datetime

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


file_path = 'bob_usdt_history.csv'

try:
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
except:
    df = pd.DataFrame(columns=['Timestamp', 'Price'])

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
new_row = pd.DataFrame([[today, price]], columns=["Timestamp", "Price"])

df = pd.concat([df, new_row], ignore_index=True) 
df.to_csv(file_path, index=False)