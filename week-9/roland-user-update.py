#Title: Assignment 9.3
#Author: Professor Krasso 
#Date: 12/13/2020
#Modified By: Jonathan Roland
#Description: demonstration of updating and deleting documents in MongoDB via Python script

import pymongo

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost',27017)

db = client.web335

db.users.update_one(

    {"employee_id": "0000008"},

    {

        "$set": {

            "email": "jdroland@my365.bellevue.edu"

        }

    }

)

pprint.pprint(db.users.find_one({"employee_id": "0000008"},{"email":1,"employee_id":1,"first_name":1,"last_name":1}))