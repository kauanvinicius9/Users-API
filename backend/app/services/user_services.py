from app.database.db import Users, save_users

def get_user_by_id(user_id):
    for user in Users:
        if user["id"] == user_id:
            return user
    return {}

def add_user(user):
    new_user = user.model_dump()

    new_user["id"] = max((u["id"] for u in Users), default=0) + 1

    Users.append(new_user)
    save_users()

    return new_user


def edit_user(user_id, user):
    for index, current_user in enumerate(Users):
        if current_user["id"] == user_id:
            updated_user = user.model_dump()
            updated_user["id"] = user_id

            Users[index] = updated_user
            save_users()

            return updated_user

    return {"message": "User not found"}


def remove_user(user_id):
    for index, user in enumerate(Users):
        if user["id"] == user_id:
            deleted = Users.pop(index)
            save_users()

            return deleted

    return {"message": "User not found"}