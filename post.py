from io import FileIO
import os
from os import path
import requests
import datetime
from datetime import date, timedelta
import logging

now = datetime.datetime.now()
now = now.strftime("%Y%m%d %H%M%S")
    
# Get Exe current directory
path = os.getcwd()
print("Current Directory", path)
    
logfile = path + '\\PriceTicket_log\\priceticket_' + str(now) + '.log'

logging.basicConfig(filename=logfile, #"newfile.log", 
                        format='%(asctime)s %(message)s', 
                        filemode='w') 
  
# Creating an object 
logger = logging.getLogger() 
 
# Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)
logger.debug(date.today())

branch = [929, 875, 928, 862, 867]
api = {
    "929": "https://api-eu.vusion.io/vcloud/v1/stores/courts_sg.mega/items/files/",
    "875": "https://api-eu.vusion.io/vcloud/v1/stores/courts_sg.nex/items/files/",
    "928": "https://api-eu.vusion.io/vcloud/v1/stores/courts_sg.928/items/files/",
    "862": "https://api-eu.vusion.io/vcloud/v1/stores/courts_sg.862/items/files/",
    "867": "https://api-eu.vusion.io/vcloud/v1/stores/courts_sg.867/items/files/"
}

for i in branch:
    
    def upload_digital_price_ticket_feed(i):
            priceTicketFileName = 'BC_digital_price_ticket_feed_'+ str(i) + '__' + str(date.today() - timedelta(days=1)) + '.csv'
            base = api.get(str(i))+priceTicketFileName
            rawfilepath = '\\\\srvsinfs\\Crystal\\Digital_PriceTicket_Feed\\Archive\\' + priceTicketFileName 
            logger.debug(priceTicketFileName) 
            logger.debug(path) 
            logger.debug(base)
            headers1 = {
                'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': 'c51d2bd6c51a451c9d1a098deb509e6a',
                }
            with open(rawfilepath, 'rb') as file:
                r = requests.post(url=base, data=file, verify=False, headers=headers1, timeout=None)
            logger.debug(r) 
            logger.debug(r.status_code) 
    
    upload_digital_price_ticket_feed(i)

logging.shutdown()

