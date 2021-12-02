from binance.client import Client
import config

def main():
    client = Client(config.API_KEY,config.API_SECRET)

    klines = client.get_historical_klines("BUSDTRY", Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
    for hourly_data in klines:
        opening_time = hourly_data[0]
        opening_price = hourly_data[1]
        closing_price = hourly_data[4]
        volume = hourly_data[5]
        closing_time = hourly_data[6]
        no_of_trades = hourly_data[8]

        print('Opening Time: {}'.format(opening_time))
        print('Opening Price: {}'.format(opening_price))
        print('Closing Price: {}'.format(closing_price))
        print('Closing Time: {}'.format(closing_time))
        print('Volume: {}'.format(volume))
        print('No. of Trades: {}'.format(no_of_trades))
        print(" ")




if __name__ == "__main__":
    main()