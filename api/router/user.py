from fastapi import APIRouter , Depends
from schemas import UserBase , UserDisplay
from sqlalchemy.orm import Session
from db.databases import get_db
from db import db_user



router = APIRouter(prefix='/user' , tags=['user',])

@router.post('/create_user' , response_model=UserDisplay)
def create_user(request:UserBase ,db:Session=Depends(get_db)):
    return db_user.create_user(request , db)


