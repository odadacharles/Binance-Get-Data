from binance.client import Client
import config
from datetime import datetime


def main():
    client = Client(config.API_KEY,config.API_SECRET, testnet=False)
    info = client.get_account()
    unx_time = info['updateTime']
    current_date = datetime.utcfromtimestamp(unx_time/1000).strftime('%Y-%m-%d %H:%M:%S')
    print(current_date)
    for asset in info['balances']:
        asset_val = float(asset['free'])
        if asset_val>0:
            print(asset['asset']+": "+ asset['free'])

if __name__ == "__main__":
    main()