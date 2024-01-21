import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient


class Config:
    def __init__(self):
        load_dotenv()

    def variables(self) -> dict:
        return {
            'leetCodeGraphqlEndpoint': os.getenv('LEETCODE_GRAPHQL_ENDPOINT'),
            'mongo_uri': os.getenv('MONGO_URI', 'mongodb://localhost:27017'),
            'db_name': os.getenv('DB_NAME'),
            'colelction_name': os.getenv('COLLECTION_NAME', '')
        }

    def connectDB(self):
        variables = self.variables()
        mongo_uri = variables['mongo_uri']
        db_name = variables['db_name']
        client = AsyncIOMotorClient(mongo_uri)
        db = client.get_database(db_name)

        try:
            client.admin.command('ping')
            print("Pinged your deployment. You have successfully connected to MongoDB!")
        except Exception as e:
            print(e)
