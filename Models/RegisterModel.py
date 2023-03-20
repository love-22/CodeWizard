import pymongo
from pymongo import MongoClient


class RegisterModel:

    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.codewizard
        self.users = self.db.Users

    def insert_user(self, data):

        uuid = self.users.insert_one({"username": data.username, "name": data.name, "birthday": data.birthday,
                                      "password": data.password, "email": data.email}).inserted_id
        print("uid is", uuid)
