import sys
import os
import requests
import time
import threading


version = "v1.3"
print("---------------------\n", version, "Bitcoin to USD\n---------------------")

logDataToFile = "true"

fileName65Seconds = "bitcoin_price_data_65_seconds"
fileName5Minutes = "bitcoin_price_data_5_minutes"
fileName10Minutes = "bitcoin_price_data_10_minutes"
fileName30Minutes = "bitcoin_price_data_30_minutes"

bitcoinUrlAddress = 'https://joebohack.com/storage/personal/btc_price.php'
parameter = {'rate': float}

def refreshDataBTC65Seconds():
    while True:
        responseBTC65Seconds = requests.post(bitcoinUrlAddress, data = parameter)
        print ("1 Bitcoin ~= $" + str(responseBTC65Seconds.text) + " USD |" + time.ctime() + "|")
        print("Waiting 65 seconds before requesting information again..")

        if logDataToFile == "true":
            with open(os.path.join(sys.path[0], fileName65Seconds + ".log"), "a") as log:
                log.write("1 Bitcoin ~= $" + str(responseBTC65Seconds.text) + " USD |" + time.ctime() + "|\n")
            time.sleep(65)
        else:
            time.sleep(65)

def refreshDataBTC5Minutes():
    while True:
        responseBTC5Minutes = requests.post(bitcoinUrlAddress, data = parameter)
        print ("1 Bitcoin ~= $" + str(responseBTC5Minutes.text) + " USD |" + time.ctime() + "|")
        print("Waiting 5 minutes before requesting information again..")

        if logDataToFile == "true":
            with open(os.path.join(sys.path[0], fileName5Minutes + ".log"), "a") as log:
                log.write("1 Bitcoin ~= $" + str(responseBTC5Minutes.text) + " USD |" + time.ctime() + "|\n")
            time.sleep(300)
        else:
            time.sleep(300)

def refreshDataBTC10Minutes():
    while True:
        responseBTC10Minutes = requests.post(bitcoinUrlAddress, data = parameter)
        print ("1 Bitcoin ~= $" + str(responseBTC10Minutes.text) + " USD |" + time.ctime() + "|")
        print("Waiting 10 minutes before requesting information again..")

        if logDataToFile == "true":
            with open(os.path.join(sys.path[0], fileName10Minutes + ".log"), "a") as log:
                log.write("1 Bitcoin ~= $" + str(responseBTC10Minutes.text) + " USD |" + time.ctime() + "|\n")
            time.sleep(600)
        else:
            time.sleep(600)

def refreshDataBTC30Minutes():
    while True:
        responseBTC30Minutes = requests.post(bitcoinUrlAddress, data = parameter)
        print ("1 Bitcoin ~= $" + str(responseBTC30Minutes.text) + " USD |" + time.ctime() + "|")
        print("Waiting 30 minutes before requesting information again..")

        if logDataToFile == "true":
            with open(os.path.join(sys.path[0], fileName30Minutes + ".log"), "a") as log:
                log.write("1 Bitcoin ~= $" + str(responseBTC30Minutes.text) + " USD |" + time.ctime() + "|\n")
            time.sleep(1800)
        else:
            time.sleep(1800)

# this will allow for running multiple loops while the program runs
thread1 = threading.Thread(target=refreshDataBTC65Seconds)
thread1.start()

thread2 = threading.Thread(target=refreshDataBTC5Minutes)
thread2.start()

thread3 = threading.Thread(target=refreshDataBTC10Minutes)
thread3.start()

thread4 = threading.Thread(target=refreshDataBTC30Minutes)
thread4.start()