# ------------------------------
# 2017/09 - RPi3 (wifi)
# /dev/ttyAMA0 previously used to access# https://github.com/octopusengine/simpleBitcoinMachine
#
# ing.Jan Copak - Czechrepublic / Prague
# octopusengine.eu | newreality.eu
#--------------------------------------------
#
#--------------------------------------------
#https://github.com/blockchain/receive-payments-demos/blob/master/python/receive_demo/views.py
#2017/08> https://chain.so/api/v2/get_tx_received/LTC/LNTKxPMWDNAHT1rUkAGmS81CMBHqB3W723
#--------------------------------------------
import urllib
import time
import datetime
from urllib import urlopen
import json    
import requests 

debugPrint = True
#my wallet address:
wallAdrBTC="11r118H2Qv4oHfjFuJnuU8GZHGNqwEH9e"
wallAdrLTC="LNTKxPMWDNAHT1rUkAGmS81CMBHqB3W723"

#---server time--- (start > RPi was off-line)
def getServerTime():
   serverTime = urlopen("http://www.octopusengine.eu/api/datetime.php").read()
   return str(serverTime)   
   
if (debugPrint):
   print(">>> octopusengine.org/api --- getServerTime()")	
   print(getServerTime())
   print("")

#---bitstamp BTC/USD LTC/USD

#bcfile = urlopen("https://www.bitstamp.net/api/ticker/").read()
jBtc = requests.get("https://www.bitstamp.net/api/ticker/")
Btcc = jBtc.json()['last']
time.sleep(1)

jLtc = requests.get("https://www.bitstamp.net/api/v2/ticker/ltcusd/")
Ltcc = jLtc.json()['last']
time.sleep(2)

if (debugPrint):
   if (debugPrint): print(">>> bitstamp.net/api/ticker ---")	
   print("BTC:"+str(Btcc))
   print("LTC:"+str(Ltcc))

   print(">>> bitcoin last transaction ---")

resourceBTC = "https://chain.so/api/v2/get_tx_received/BTC/"+wallAdrBTC
j = requests.get(resourceBTC)
#print(j.json()['data']['txs'])  
arrayCnt = len(j.json()['data']['txs'])

#print(j.json()['data']['txs'][0]['time']) 
#print(j.json()['data']['txs'][arrayCnt-1]['time'])  
print(arrayCnt)  
print("last >")
print(datetime.datetime.fromtimestamp(int(j.json()['data']['txs'][arrayCnt-1]['time'])).strftime('%Y-%m-%d %H:%M:%S'))
print(j.json()['data']['txs'][arrayCnt-1]['value'])     
time.sleep(2)
  
print("--- litecoin last transaction ---")
resourceLTC = "https://chain.so/api/v2/get_tx_received/LTC/"+wallAdrLTC
#print(resourceLTC)   
j = requests.get(resourceLTC)
#print(j.json()['data']['txs'])  
arrayCnt = len(j.json()['data']['txs'])
print(arrayCnt)  
#print(j.json()['data']['txs'][0]['time'])  
print("last >")
#print(j.json()['data']['txs'][arrayCnt-1]['time'])  
print(datetime.datetime.fromtimestamp(int(j.json()['data']['txs'][arrayCnt-1]['time'])).strftime('%Y-%m-%d %H:%M:%S'))
print(j.json()['data']['txs'][arrayCnt-1]['value'])     
    
#---/end 

 
