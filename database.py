import json
import os

FILE = "users.json"

def load_users():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_users(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def get_user(users, user_id):
    user_id = str(user_id)

    if user_id not in users:
        users[user_id] = {
            "vip": 0,
            "coins": 0,
            "spins": 3
        }

    return users[user_id]
