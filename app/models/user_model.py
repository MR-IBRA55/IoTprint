from typing import Dict

from app import mongo


class UserModel:
    @classmethod
    def register_user(cls, data: Dict) -> None:
        mongo.db.users.insert_one(data)

    @classmethod
    def get_user_by_username(cls, username: str) -> Dict:
        return mongo.db.users.find_one({"username": username})
