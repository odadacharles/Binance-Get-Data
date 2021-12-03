#This script retrieves currently active trading pairs within binance and saves it in a pandas data frame which can be saved to an csv file

#Import the relevant libraries
from binance.client import Client
import config
import pandas as pd

client = Client(config.API_KEY, config.API_SECRET)              #Create an instance of the client method that retrieves the api key and secret from the config file
exchange_info = client.get_exchange_info()                      #Create a variable to store all information from the 'get_exchange_info' method
trading_pairs = []                                              #Create an empty list called trading_pairs
for s in exchange_info['symbols']:
    if 'ETH' in s['symbol']:                              #Loop through the symbols in the exchange info and append all symbols to the trading_pairs list
        trading_pairs.append(s['symbol'])

Symbol_DF = pd.DataFrame(columns=["Symbols"], data=trading_pairs)  #Create a pandas dataframe and save the trading_pairs in it
Symbol_DF.to_csv('binance_ETH_trading_pairs.csv', index=False)      #Convert the dataframe to a csv file, 'index = False' will prevent creation of a second index when the csv file is created
