from distutils.log import INFO
from hashlib import new
import pymongo
import re

client = pymongo.MongoClient("mongodb+srv://bdcard:103626@cluster0.crijo.mongodb.net/?retryWrites=true&w=majority")
db = client.bdcard
collection = db.users

def clean(birthday,phonenumber,messages):
    new_birthday=str(birthday[5:])
    new_birthday=re.sub('[-]', '', new_birthday)

    new_phonenumber=re.sub('[-=,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', phonenumber)
    infos={'phonenumber':new_phonenumber,'message':messages}

    add(new_birthday,infos)
    
def check(new_birthday):
    saved=db.collection.find({"birthday": new_birthday}) #if there is no data return 0
    for data in saved:
        return data
    return 0

def add(new_birthday,infos):
    #check the date, if there is no such a date, add value
    info=check(new_birthday)    

    if info==0:        
        tmp=[infos]
        data={"birthday":new_birthday,"birthday_cards":tmp}
        collection.insert_one(data)
    else:
        info['birthday'].append(infos)
        collection.delete_one({"birthday": new_birthday})
        collection.insert_one(info)


