from config.db import DBConfig
from bson.objectid import ObjectId


class DBService:
    def __init__(self, leetcode_username: str):
        self.db_config = DBConfig()
        self.collection = self.db_config.collection
        self.username = leetcode_username

    def user_esists_in_db(self):
        existing_user = self.collection.find_one({'username': self.username})
        if existing_user:
            return existing_user['_id']
        return False

    def get_stats_from_db(self):
        user_id = self.user_esists_in_db()

        if user_id:
            cursor_response = self.collection.find(
                {'_id': ObjectId(user_id)}, {'_id': 0})

            stats = {}
            for document in cursor_response:
                stats = document
            return stats
        return None

    def save_stats_to_db(self, new_stats):
        new_stats_dict = new_stats.dict()
        result = self.collection.insert_one(new_stats_dict)
