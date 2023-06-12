from schemas import UserBase
from db.models import DBuser
from sqlalchemy.orm import Session
from fastapi import Depends
from db.databases import get_db
from db.hash import Hash
from fastapi.exceptions import HTTPException

def create_user(request:UserBase , db:Session):
    user = DBuser(
        user_name = request.user_name,
        password = Hash.bcrypt(request.password),
        email = request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_user_name(username:str  ,db:Session):
    user = db.query(DBuser).filter(DBuser.user_name == username).first()
    if not user:
        raise HTTPException(status_code=404 , detail="user not found")
    return user