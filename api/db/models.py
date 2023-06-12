from db.databases import base
from sqlalchemy import Column , Integer , String , ForeignKey , DateTime
from sqlalchemy.orm import relationship

class DBuser(base):
    __tablename__ = 'DBuser'
    
    id = Column(Integer , index=True , primary_key=True)
    user_name = Column(String)
    password = Column(String)
    email = Column(String)
    post = relationship('DBpost' , back_populates= 'user')
    
class DBpost(base):
    __tablename__ = 'DBpost'
    
    id = Column(Integer , index=True , primary_key=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer , ForeignKey('DBuser.id'))
    user = relationship('DBuser' , back_populates= 'post')
    comments = relationship('DBcomment' , back_populates= 'posts')
    
class DBcomment(base):
    __tablename__ = "DBcomment"
    
    id = Column(Integer , index=True , primary_key=True)
    text = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer , ForeignKey('DBuser.id'))
    post_id = Column(Integer , ForeignKey('DBpost.id'))
    user = relationship('DBuser')
    posts = relationship('DBpost' , back_populates= 'comments')
    
    