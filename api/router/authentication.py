from fastapi import Depends , status , APIRouter
from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.databases import get_db
from auth.oauth2 import create_access_token
from db.models import DBuser
from fastapi.security.oauth2 import OAuth2PasswordRequestForm



router = APIRouter(tags=["authentication"])

@router.post('/token' , summary="register" , description="you can take a token from here")
def get_token(request:OAuth2PasswordRequestForm =Depends() , db:Session =Depends(get_db)):
    
    user = db.query(DBuser).filter(DBuser.user_name == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="incorrect value")
    
    if not Hash.verify(user.password , request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="incorrect password")

    temp_token = create_access_token(data={"sub":request.username})
    
    return {
        'access_token' : temp_token,
        'type_token' : 'bearer',
        'userID' : user.id,
        'username' : user,
    }
    
    