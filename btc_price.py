import sys
import os
import requests
import time
import threading


version = "v1.4"
print("---------------------\n", version, "Bitcoin to USD\n---------------------")

logDataToFile = "true"

fileName_65Seconds = "bitcoin_price_data_65_seconds"
fileName_5Minutes = "bitcoin_price_data_5_minutes"
fileName_10Minutes = "bitcoin_price_data_10_minutes"
fileName_30Minutes = "bitcoin_price_data_30_minutes"

bitcoinUrlAddress = 'https://joebohack.com/storage/personal/btc_price.php'
parameter = {'rate': float}

def refreshData_65Seconds():
    while True:
        response_65Seconds = requests.post(bitcoinUrlAddress, data = parameter)
        print ("1 Bitcoin ~= $" + str(response_65Seconds.text) + " USD |" + time.ctime() + "|")
        print("Waiting 65 seconds before requesting information again..")

        if logDataToFile == "true":
            with open(os.path.join(sys.path[0], fileName_65Seconds + ".log"), "a") as log:
                log.write("1 Bitcoin ~= $" + str(response_65Seconds.text) + " USD |" + time.ctime() + "|\n")
            time.sleep(65)
        else:
            time.sleep(65)

def refreshData_5Minutes():
    while True:
        response_5Minutes = requests.post(bitcoinUrlAddress, data = parameter)
        print ("1 Bitcoin ~= $" + str(response_5Minutes.text) + " USD |" + time.ctime() + "|")
        print("Waiting 5 minutes before requesting information again..")

        if logDataToFile == "true":
            with open(os.path.join(sys.path[0], fileName_5Minutes + ".log"), "a") as log:
                log.write("1 Bitcoin ~= $" + str(response_5Minutes.text) + " USD |" + time.ctime() + "|\n")
            time.sleep(300)
        else:
            time.sleep(300)

def refreshData_10Minutes():
    while True:
        response_10Minutes = requests.post(bitcoinUrlAddress, data = parameter)
        print ("1 Bitcoin ~= $" + str(response_10Minutes.text) + " USD |" + time.ctime() + "|")
        print("Waiting 10 minutes before requesting information again..")

        if logDataToFile == "true":
            with open(os.path.join(sys.path[0], fileName_10Minutes + ".log"), "a") as log:
                log.write("1 Bitcoin ~= $" + str(response_10Minutes.text) + " USD |" + time.ctime() + "|\n")
            time.sleep(600)
        else:
            time.sleep(600)

def refreshData_30Minutes():
    while True:
        response_30Minutes = requests.post(bitcoinUrlAddress, data = parameter)
        print ("1 Bitcoin ~= $" + str(response_30Minutes.text) + " USD |" + time.ctime() + "|")
        print("Waiting 30 minutes before requesting information again..")

        if logDataToFile == "true":
            with open(os.path.join(sys.path[0], fileName_30Minutes + ".log"), "a") as log:
                log.write("1 Bitcoin ~= $" + str(response_30Minutes.text) + " USD |" + time.ctime() + "|\n")
            time.sleep(1800)
        else:
            time.sleep(1800)

# this will allow for running multiple loops while the program runs
thread1 = threading.Thread(target=refreshData_65Seconds)
thread1.start()

thread2 = threading.Thread(target=refreshData_5Minutes)
thread2.start()

thread3 = threading.Thread(target=refreshData_10Minutes)
thread3.start()

thread4 = threading.Thread(target=refreshData_30Minutes)
thread4.start()