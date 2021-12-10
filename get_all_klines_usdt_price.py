#In the code below, a checkpoint is used to denote a point where information is printed to confirm a section of the data works as expected before proceeding to the next step.
#Import all relevant libraries
import pandas as pd
import csv
from datetime import datetime, date
from binance.client import Client
import config

def main():
    client = Client(config.API_KEY,config.API_SECRET) #create a client instance that retrieves the api key and secret from the config script
    trading_pairs_path = 'C:/Users/Charlie.O/Documents/Python Projects/Binance Get Data/Data/'+str(date.today())+'/trading_pairs '+str(date.today())+'.csv' #This path is defined to get data from a different folder each day
    csv_file = open(trading_pairs_path) #Open the csv file
    csvreader = csv.reader(csv_file)             #read the contents of the csv file and save to a new variable
    trading_pairs = []                           #create a list called 'trading_pairs'
    header = next(csvreader)                     #Assign the first item in trading pairs the header variable

    #Loop through the data in the csvreader variable and append each trading pair to the trading_pairs list
    for pair in csvreader:
        trading_pairs.append(pair)
    
    #print(trading_pairs)                        #Print the trading_pairs list (Checkpoint)
    col_list = ["Index","Trading_Pair","Opening Time","Opening Price","Closing Price","Volume","Closing Time","No. of Trades"] #create a list of the column names in the BTCUSDT csv file
    usd_pricesdf=pd.read_csv('C:/Users/Charlie.O/Documents/Python Projects/Binance Get Data/Data/'+str(date.today())+'/daily_BTCUSDT_kline.csv', usecols=col_list) #Read the values in the csv file into a dataframe

    daily_klinedf = pd.DataFrame(columns=["Index","Trading_Pair","Opening Time","Opening Price","Closing Price","Volume","Closing Time","No. of Trades"])  #Create a pandas dataframe and save the trading_pairs in it
    
    #Loop through each trading pair and get it's candlestick data for the prescribed period
    for item in trading_pairs:
        klines = client.get_historical_klines(item[0], Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC") #create a variable to store the candlestick data for the defined period
        #Create a loop to extract and print the necessary data from the historical candlestick information
        counter=0 #Create a counter that will be used to reference individual rows for each set of trading pairs
        #Loop through the price data for each hour of the period defined above and extract specific items of interest such as opening times, trade volumes and prices
        for hourly_data in klines:
            index = counter
            opening_time = hourly_data[0]

            #Multiply opening and closing prices by corresponding USD values from the usd_pricesdf
            opening_price = float(hourly_data[1])*float(usd_pricesdf["Opening Price"][counter]) 
            closing_price = float(hourly_data[4])*float(usd_pricesdf["Closing Price"][counter])

            volume = hourly_data[5]
            closing_time = hourly_data[6]
            no_of_trades = hourly_data[8]


            #create a new dataframe to hold the data above. This dataframe will be concatenated with the main dataframe 'daily_klinedf'
            kline_info = [index, item[0],opening_time,opening_price,closing_price,volume,closing_time,no_of_trades]
            pair_df=pd.DataFrame(columns=["Index","Trading_Pair","Opening Time","Opening Price","Closing Price","Volume","Closing Time","No. of Trades"], data=[kline_info])
            daily_klinedf=pd.concat([daily_klinedf,pair_df],ignore_index=True)

            #Save the data above to a csv file as well. This path will save to a different folder every day
            with open('C:/Users/Charlie.O/Documents/Python Projects/Binance Get Data/Data/'+str(date.today())+'/daily_BTC_kline.csv', 'a', newline='', encoding= 'utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerow(kline_info)
            counter+=1
    daily_klinedf.to_pickle('C:/Users/Charlie.O/Documents/Python Projects/Binance Get Data/Data/'+str(date.today())+'/daily_BTC_kline_df') #pickle the 'daily_klinedf' to save the dataframe locally
    
        

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