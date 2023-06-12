from pydantic import BaseModel 
from datetime import datetime
from typing import Optional , List


class UserBase(BaseModel):
    user_name : str
    password : str
    email : str
    
class UserDisplay(BaseModel):
    id : int
    user_name : str
    email : str
    
    class Config:
        orm_mode = True
    
class PostBase(BaseModel):
    image_url : str
    image_url_type : str
    caption : str
    user_id : int

class User(BaseModel):
    id : int
    user_name : str
    
    class Config:
        orm_mode = True
        
class CommentBase(BaseModel):
    text : str 
    timestamp : datetime
    user_id : int
    post_id : int
    
class CommentDisplay(BaseModel):
    id : int
    text : str 
    timestamp : datetime
    user : User
    
    class Config:
        orm_mode = True
        
class PostDisplay(BaseModel):
    id : int
    image_url : str
    image_url_type : str
    caption : str
    user : User
    comment : List[CommentDisplay]
    
    class Config:
        orm_mode = True
        
class UserAuth(BaseModel):
    id : int
    user_name : str
    email : str
    
    class Config:
        orm_mode = True
        
