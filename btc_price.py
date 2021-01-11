import requests
import time

version = "v1.0"
print("---------------------\n", version, "Bitcoin to USD\n---------------------")

bitcoinUrlAddress = 'https://joebohack.com/storage/personal/btc_price.php'
parameter = {'rate': float}

def refreshDataBTC():
    responseBTC = requests.post(bitcoinUrlAddress, data = parameter)
    print ("1 Bitcoin ~= $" + str(responseBTC.text), "USD |", time.ctime(), "|")
    print("Waiting 65 seconds before requesting information again..")

while True:
    refreshDataBTC()
    time.sleep(65) #It takes around 60 seconds for the API to refresh so we call it after 60 seconds
