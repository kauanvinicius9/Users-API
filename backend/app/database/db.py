import json

FILE_PATH = "app/database/db.json"

with open(FILE_PATH, "r", encoding="utf-8") as file:
    Users = json.load(file)

def save_users():
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(Users, file, indent=4, ensure_ascii=False)