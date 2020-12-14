#Title: Assignment 9.2
#Author: Professor Krasso 
#Date: 12/13/2020
#Modified By: Jonathan Roland
#Description: demonstration of querying and creating documents in MongoDB via Python script

import pymongo

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost',27017)

db = client.web335

user = {

    "first_name": "Johann",

    "last_name": "Bach",

    "email": "bachrocks@me.com",

    "employee_id": "0000008",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000008"}))