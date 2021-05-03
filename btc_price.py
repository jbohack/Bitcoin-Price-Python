import sys
import os
import requests
import time
import threading


version = "v2.3"
print("---------------------\n", version, "Bitcoin to USD\n---------------------\n")

# you can modify the file names for the logs here
fileName_1 = "bitcoin_price_data_1"
fileName_2 = "bitcoin_price_data_2"
fileName_3 = "bitcoin_price_data_3"
fileName_4 = "bitcoin_price_data_4"

# enable / disable logging data to a log file per interval
logData_1 = "true" 
logData_2 = "true"  
logData_3 = "true"
logData_4 = "true"

# enable / disable logging data to the terminal per interval
# recommended to keep atleast one enabled so that you can verify the program is working properly with a glance
logToTerminal_1 = "true"
logToTerminal_2 = "true"
logToTerminal_3 = "true"
logToTerminal_4 = "true"

# enable / disable printing status code 
showStatusCode = input("Would you like to show status codes? y/n: ")

# enable / disable logging to a file completly
logDataToFile = input("Would you like to enable the logging to file module? y/n: ")

# configure the amount of logs to enable at once
amountOfLogs = int(input("How many logs would you like to enable? 1-4: "))

bitcoinUrlAddress = 'https://joebohack.com/storage/personal/btc_price.php'
parameter = {'rate': float}

# per run intervals
if amountOfLogs >= 1: 
    if logToTerminal_1 == "true" or logData_1 == "true":
        log1_interval = int(input("\n(Log 1)\n-------\nHow many seconds would you like to wait for the data to be refreshed? \n"))
    if amountOfLogs >= 2: 
        if logToTerminal_2 == "true" or logData_2 == "true":
            log2_interval = int(input("\n(Log 2)\n-------\nHow many seconds would you like to wait for the data to be refreshed? \n"))
        if amountOfLogs >= 3: 
            if logToTerminal_3 == "true" or logData_3 == "true":
                log3_interval = int(input("\n(Log 3)\n-------\nHow many seconds would you like to wait for the data to be refreshed? \n"))
                if amountOfLogs >= 4: 
                        if logToTerminal_4 == "true" or logData_4 == "true":
                            log4_interval = int(input("\n(Log 4)\n-------\nHow many seconds would you like to wait for the data to be refreshed? \n"))

if amountOfLogs >= 1: 
    def refreshData_1():
        while True:
            response_1 = requests.post(bitcoinUrlAddress, data = parameter)

            if response_1.status_code != 200:
                print("An error has occurred while requesting the data.")

            if showStatusCode == "y":
                print("Status Code:", response_1.status_code)

            if logToTerminal_1 == "true":
                if response_1.status_code == 200:
                    print ("1 Bitcoin ~= $" + str(response_1.text) + " USD |" + time.ctime() + "|")
                    print("Waiting", log1_interval, "seconds before requesting information again..")
                    print("-------------------------------------------------------")

            if logDataToFile == "y" and logData_1 == "true":
                if response_1.status_code == 200:
                    try:
                        with open(os.path.join(sys.path[0], fileName_1 + ".log"), "a") as log:
                            log.write("1 Bitcoin ~= $" + str(response_1.text) + " USD |" + time.ctime() + "|\n")
                    except:
                        print("An error has occurred while writing to the file!")
            time.sleep(log1_interval)      

if amountOfLogs >= 2: 
    def refreshData_2():
        while True:
            response_2 = requests.post(bitcoinUrlAddress, data = parameter)

            if response_2.status_code != 200:
                print("An error has occurred while requesting the data.")        

            if showStatusCode == "y":
                print("Status Code:", response_2.status_code)

            if logToTerminal_2 == "true":
                if response_2.status_code == 200:
                    print ("1 Bitcoin ~= $" + str(response_2.text) + " USD |" + time.ctime() + "|")
                    print("Waiting", log2_interval, "seconds before requesting information again..")
                    print("-------------------------------------------------------")
                
            if logDataToFile == "y" and logData_2 == "true":
                if response_2.status_code == 200:
                    try:
                        with open(os.path.join(sys.path[0], fileName_2 + ".log"), "a") as log:
                            log.write("1 Bitcoin ~= $" + str(response_2.text) + " USD |" + time.ctime() + "|\n")
                    except:
                        print("An error has occurred while writing to the file!")
            time.sleep(log2_interval)

if amountOfLogs >= 3:             
    def refreshData_3():
        while True:
            response_3 = requests.post(bitcoinUrlAddress, data = parameter)

            if response_3.status_code != 200:
                print("An error has occurred while requesting the data.")

            if showStatusCode == "y":
                print("Status Code:", response_3.status_code)

            if logToTerminal_3 == "true":
                if response_3.status_code == 200:
                    print ("1 Bitcoin ~= $" + str(response_3.text) + " USD |" + time.ctime() + "|")
                    print("Waiting", log3_interval, "seconds before requesting information again..")
                    print("-------------------------------------------------------")

            if logDataToFile == "y" and logData_3 == "true":
                if response_3.status_code == 200:
                    try:
                        with open(os.path.join(sys.path[0], fileName_3 + ".log"), "a") as log:
                            log.write("1 Bitcoin ~= $" + str(response_3.text) + " USD |" + time.ctime() + "|\n")
                    except:
                        print("An error has occurred while writing to the file!")
            time.sleep(log3_interval)

if amountOfLogs >= 4:             
    def refreshData_4():
        while True:
            response_4 = requests.post(bitcoinUrlAddress, data = parameter)

            if response_4.status_code != 200:
                print("An error has occurred while requesting the data.")

            if showStatusCode == "y":
                print("Status Code:", response_4.status_code)

            if logToTerminal_4 == "true":
                if response_4.status_code == 200:
                    print ("1 Bitcoin ~= $" + str(response_4.text) + " USD |" + time.ctime() + "|")
                    print("Waiting", log4_interval, "seconds before requesting information again..")
                    print("-------------------------------------------------------")

            if logDataToFile == "y" and logData_4 == "true":
                if response_4.status_code == 200:
                    try:
                        with open(os.path.join(sys.path[0], fileName_4 + ".log"), "a") as log:
                            log.write("1 Bitcoin ~= $" + str(response_4.text) + " USD |" + time.ctime() + "|\n")
                    except:
                        print("An error has occurred while writing to the file!")
            time.sleep(log4_interval)
            
# this will allow for running multiple loops while the program runs
if amountOfLogs >= 1: 
    thread1 = threading.Thread(target=refreshData_1)
    thread1.start()
if amountOfLogs >= 2: 
    thread2 = threading.Thread(target=refreshData_2)
    thread2.start()
if amountOfLogs >= 3: 
    thread3 = threading.Thread(target=refreshData_3)
    thread3.start()
if amountOfLogs >= 4: 
    thread4 = threading.Thread(target=refreshData_4)
    thread4.start()