from fastapi import APIRouter , Depends , status , UploadFile , File
from auth.oauth2 import get_current_user
from typing import List
from random import choice
from string import ascii_letters
from schemas import PostBase , PostDisplay , UserAuth
from sqlalchemy.orm import Session
from db.databases import get_db
from db import db_post
from shutil import copyfileobj
from fastapi.exceptions import HTTPException

images_url_types = ["uploaded" , 'url']

router = APIRouter(prefix='/post' , tags=['post',])

@router.post('/create_post' , response_model=PostDisplay)
def create_post(request:PostBase ,db:Session=Depends(get_db),curent_user:UserAuth=Depends(get_current_user)):
    if request.image_url_type not in images_url_types:
        return HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE ,
                            detail="enter between url or uploaded")
    return db_post.create_post(request , db)

@router.post('/delete_post')
def delete_post(id:int ,db:Session=Depends(get_db),curent_user:UserAuth=Depends(get_current_user)):
    return db_post.delete_post(id , db , curent_user.id)

@router.post('/upload_file')
def upload_file(file:UploadFile=File(...)):
    new_word = "".join(choice(ascii_letters) for _ in range(6))
    new_name = f"_{new_word}.".join(file.filename.rsplit('.',1))
    path = f"uploaded_file/{new_name}"
    with open(path , "w+b") as myfile:
        copyfileobj(file.file , myfile)
    return {"path" : path}


@router.get('/get_posts' , response_model=List[PostDisplay])
def get_posts(db:Session=Depends(get_db)):
    return db_post.get_posts(db)


