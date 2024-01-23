from config.db import DBConfig
from bson.objectid import ObjectId


class DBService:
    def __init__(self, leetcode_username: str):
        self.db_config = DBConfig()
        self.collection = self.db_config.collection
        self.username = leetcode_username

    def user_exists_in_db(self) -> ObjectId:
        existing_user = self.collection.find_one(
            {'username': self.username}, {'_id': 1})

        if existing_user:
            return existing_user['_id']
        return None

    def get_stats_from_db(self, user_id: ObjectId) -> dict:
        cursor_response = self.collection.find(
            {'_id': ObjectId(user_id)}, {'_id': 0})

        stats = {}
        for document in cursor_response:
            stats = document
        return stats

    def save_stats_to_db(self, new_stats):
        new_stats_dict = new_stats.dict()
        result = self.collection.insert_one(new_stats_dict)
