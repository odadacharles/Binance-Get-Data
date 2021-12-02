#This script retrieves currently active trading pairs within binance

from binance.client import Client
import config
import pandas as pd

client = Client(config.API_KEY, config.API_SECRET)
exchange_info = client.get_exchange_info()
trading_pairs = []
for s in exchange_info['symbols']:
    trading_pairs.append(s['symbol'])

# Symbol_DF = pd.DataFrame(columns=["Symbols"], data=trading_pairs)
# Symbol_DF.to_csv('binance_trading_pairs.csv', index=False)

print(exchange_info)