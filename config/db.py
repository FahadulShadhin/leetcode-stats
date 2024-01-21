from .variables import Variables
from motor.motor_asyncio import AsyncIOMotorClient


class DBConfig:
    def __init__(self):
        self.variables = Variables()
        self.client = AsyncIOMotorClient(self.variables.mongo_uri)
        self.db = self.client[self.variables.db_name]
        self.collection = self.client[self.variables.collection_name]

    def connect_db(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You have successfully connected to MongoDB!")
        except Exception as e:
            print(e)
