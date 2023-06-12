from schemas import CommentBase
from db.models import DBcomment
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.exceptions import HTTPException

def create_comment(request:DBcomment , db:Session):
    new_comment = DBcomment(
        text = request.text,
        post_id = request.post_id,
        timestamp = datetime.now(),
        user_id = request.user_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_comment_by_post_id(id:int ,db:Session):
    return db.query(DBcomment).filter(DBcomment.post_id==id).all()

def delete_comment(id:int , db:Session , user_id:int ):
    comment = db.query(DBcomment).filter(DBcomment.id ==id).first()
    if not comment:
        raise HTTPException(status_code=404 , detail="this comment not exist")
    if comment.user_id == user_id or comment.post.user.id == user_id:
        db.delete(comment)
        db.commit()
        return 'Ok'
    
    raise HTTPException(status_code=403 , detail="you cant use this !")