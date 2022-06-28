import random, schedule, time
from datetime import datetime,timedelta
from twilio.rest import Client
from twilio_credentials import twilio_account, twilio_token, twilio_number
import database
import re
import pymongo
import os

client = pymongo.MongoClient("mongodb+srv://bdcard:103626@cluster0.crijo.mongodb.net/?retryWrites=true&w=majority")
db = client.bdcard
collection = db.users

def send_message(number,quotes):
    account=twilio_account
    token=twilio_token
    client=Client(account,token)
    quote=quotes
    #send a message
    message=client.messages.create(to=number,from_=twilio_number,body=quote)
    print(message.sid)

def check():
    now = datetime.now()
    time1=str(now)
    time2=time1[5:10]
    time3=re.sub('[-]', '', time2)

    #check friend's birthday in db, if timedelta is zero, run the function
    data=collection.find_one({"birthday": time3}) 
    #use for loops
    print(data)
    for element in data['birthday_cards']:
        print(element['phonenumber'])
        print(element['message'])
        send_message(element['phonenumber'],element['message'])    

#today's date
schedule.every().day.at("00:00").do(check)
   
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)