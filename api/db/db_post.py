from schemas import PostBase
from db.models import DBpost
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.exceptions import HTTPException

def create_post(request:PostBase , db:Session):
    new_post = DBpost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.now(),
        user_id = request.user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db:Session):
    return db.query(DBpost).all()

def delete_post(id:int , db:Session , Author_id:int ):
    post = db.query(DBpost).filter(DBpost.id ==id).first()
    if not post:
        raise HTTPException(status_code=404 , detail="this post not exist")
    if post.id != Author_id:
        raise HTTPException(status_code=403 , detail="you cant use this !")
    
    db.delete(post)
    db.commit()
    return 'Ok'
    