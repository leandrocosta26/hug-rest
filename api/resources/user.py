import json
import pdb
from config.mongo import database
from bson.objectid import ObjectId

def create_user(user):
    database.users.save(user)
    return {"message": "user created"}


def remove_user(_id):
    database.users.find_one_and_delete({"_id": ObjectId(_id)})
    return {"message": "user removed!"}


def update_user(_id, user):
    user = database.users.find_one_and_replace({"_id": ObjectId(_id)}, user)
    return {"message": "user updated!"}


def get_user_by_id(_id):
    print(_id)
    user = database.users.find_one({"_id": ObjectId(_id)})
    print(user)
    return {
                "id": str(user["_id"]), 
                'username': user["user_name"], 
                'name': user["name"], 
                'age': user["age"]
            }


def get_all_users():
    users = []

    for user in database.users.find():
        users.append({"id": str(user["_id"]), 'username': user["user_name"], 'name': user["name"], 'age': user["age"]})

    return users
