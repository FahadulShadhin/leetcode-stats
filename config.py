import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

    def variables(self):
        return {
            'leetCodeGraphqlEndpoint': os.getenv('LEETCODE_GRAPHQL_ENDPOINT')
        }
