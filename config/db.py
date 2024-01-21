from .variables import Variables
from pymongo import MongoClient


class DBConfig:
    def __init__(self):
        self.variables = Variables()
        self.client = MongoClient(self.variables.mongo_uri)
        self.db = self.client[self.variables.db_name]
        self.collection = self.db[self.variables.collection_name]
