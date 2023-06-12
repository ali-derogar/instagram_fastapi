from datetime import datetime, timedelta
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from fastapi import Depends , HTTPException , status
from sqlalchemy.orm import Session
from db.databases import get_db
from db.db_user import get_user_by_user_name
from typing import Annotated

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def create_access_token(data: dict, expires_delta:Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token:str =Depends(oauth2_scheme),db:Session=Depends(get_db)):
    
    error_credential = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= "you are unauthorized please checked",
        headers={"WWW-authenticate" : "bearer"}
        )

    print(token)
    print('**************************************')

    
    try:
        _Dict = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
        username = _Dict.get("sub")
        if not username:
            raise error_credential
    
    except JWTError:
        raise error_credential
        
    user = get_user_by_user_name(username , db)
    
    return user
    
    
    
    
    
    