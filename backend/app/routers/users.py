from fastapi import APIRouter
from app.schemas.users import User
from app.services.user_services import *

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/{user_id}")
def get_user(user_id: int):
    return get_user_by_id(user_id)

@router.post("/")
def create_user(user: User):
    return add_user(user)

@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    return edit_user(user_id, user)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return remove_user(user_id)