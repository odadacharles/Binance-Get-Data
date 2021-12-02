#This python script retrieves the current account balances of the user

#import the relevant libraries
from binance.client import Client
import config
from datetime import datetime

#define a method that will retrieve the account data from binance
def main():
    client = Client(config.API_KEY,config.API_SECRET, testnet=False) #create a client instance that retrieves the api key and secret from the config script
    info = client.get_account()                                      #Create a variable to store all information provided by the 'get_account' method
    unx_time = info['updateTime']                                    #Get the unix time stamp from the account information
    current_date = datetime.utcfromtimestamp(unx_time/1000).strftime('%Y-%m-%d %H:%M:%S') #Convert the unix timestamp to a readable format
    print(current_date)                                              #print the date and time information associated with the retrieved account information

    #Loop through the assets in the account information and print all assets with a 'free' balance greater than zero. Same can be done for 'Locked' balances
    for asset in info['balances']:
        asset_val1 = float(asset['free'])
        asset_val2 = float(asset['locked'])

        if asset_val1>0 or asset_val2>0:
            print(asset['asset'])
            print("Free: "+str(asset_val1)) 
            print("Locked: "+str(asset_val2))

#Run the function above if the condition below is met
if __name__ == "__main__":
    main()