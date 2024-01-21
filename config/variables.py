import os
from dotenv import load_dotenv


class Variables:
    def __init__(self):
        load_dotenv()

        self.leetCodeGraphqlEndpoint = os.getenv('LEETCODE_GRAPHQL_ENDPOINT')
        self.mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
        self.db_name = os.getenv('DB_NAME', 'leetcode-stats')
        self.collection_name = os.getenv('COLLECTION_NAME', 'stats')
