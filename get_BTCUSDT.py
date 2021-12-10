#In the code below, a checkpoint is used to denote a point where information is printed to confirm a section of the data works as expected before proceeding to the next step.
#Import all relevant libraries
import pandas as pd
import csv
from datetime import datetime, date
from binance.client import Client
import config

def main():
    client = Client(config.API_KEY,config.API_SECRET) #create a client instance that retrieves the api key and secret from the config script
    #print(trading_pairs)                  
    daily_klinedf = pd.DataFrame(columns=["Index","Trading_Pair","Opening Time","Opening Price","Closing Price","Volume","Closing Time","No. of Trades"])  #Create a pandas dataframe and save the trading_pairs in it
    klines = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC") #create a variable to store the candlestick data for the defined period
        #Create a loop to extract and print the necessary data from the historical candlestick information
    counter = 0
    #Create a CSV file and write in the names of the relevant columns
    with open('C:/Users/Charlie.O/Documents/Python Projects/Binance Get Data/Data/'+str(date.today())+'/daily_BTCUSDT_kline.csv', 'a', newline='', encoding= 'utf-8') as f: 
                    writer = csv.writer(f)
                    writer.writerow(["Index","Trading_Pair","Opening Time","Opening Price","Closing Price","Volume","Closing Time","No. of Trades"])

    #Loop through the klines data and extract the hourly opening and closing prices for the BTCUSDT pair and other information
    for hourly_data in klines:
        opening_time = hourly_data[0]
        opening_price = hourly_data[1]
        closing_price = hourly_data[4]
        volume = hourly_data[5]
        closing_time = hourly_data[6]
        no_of_trades = hourly_data[8]

        #Create a dataframe to hold the data above. The dataframe will be concatenated with the main dataframe
        kline_info = [counter, 'BTCUSDT',opening_time,opening_price,closing_price,volume,closing_time,no_of_trades]
        pair_df=pd.DataFrame(columns=["Index","Trading_Pair","Opening Time","Opening Price","Closing Price","Volume","Closing Time","No. of Trades"], data=[kline_info])

        #Concatenate the dataframe created above with the main dataframe
        daily_klinedf=pd.concat([daily_klinedf,pair_df],ignore_index=True)
        #Save the data above to the csv file
        with open('C:/Users/Charlie.O/Documents/Python Projects/Binance Get Data/Data/'+str(date.today())+'/daily_BTCUSDT_kline.csv', 'a', newline='', encoding= 'utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(kline_info)
        counter+=1
    #Pickle the dataframe to save it locally
    daily_klinedf.to_pickle('daily_BTCUSDT_kline_df')
    
        

            #Checkpoint
            # print('Opening Time: {}'.format(opening_time))
            # print('Opening Price: {}'.format(opening_price))
            # print('Closing Price: {}'.format(closing_price))
            # print('Closing Time: {}'.format(closing_time))
            # print('Volume: {}'.format(volume))
            # print('No. of Trades: {}'.format(no_of_trades))
            # print(" ")



#Run the function above if the condition below is met
if __name__ == "__main__":
    main()