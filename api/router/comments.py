from fastapi import APIRouter , Depends , status 
from auth.oauth2 import get_current_user
from typing import List
from schemas import CommentBase , CommentDisplay , UserAuth
from sqlalchemy.orm import Session
from db.databases import get_db
from db import db_comment
from fastapi.exceptions import HTTPException


router = APIRouter(prefix='/comment' , tags=['comment',])

@router.post('/create_comment' , response_model=CommentDisplay , summary="create your comment" , description="you can create your comment from here")
def create_comment(request:CommentBase ,db:Session=Depends(get_db)):
    return db_comment.create_comment(request , db)

@router.get('/get_comments' , response_model=List[CommentDisplay])
def get_comments(id:int ,db:Session=Depends(get_db)):
    return db_comment.get_comment_by_post_id(id ,db)

@router.post('/delete_comment')
def delete_comment(id:int ,db:Session=Depends(get_db),curent_user:UserAuth=Depends(get_current_user)):
    return db_comment.delete_comment(id , db , user_id = curent_user.id)
