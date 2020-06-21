from typing import List, Optional, Any
from datetime import datetime, timedelta

import jwt
from jwt import PyJWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.db import models

SECRET_KEY = "2b794740e42015617c7cfd4ab5dc6b43c6dca23f988df3a650f33c0c34919044"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    username: str = None

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str = None
    email: str = None

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class UserInDB(User):
    password: str

    class Config:
        orm_mode = True


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_user(db: Session, username: str) -> Optional[UserInDB]:
    db_user = db.query(
        models.User).filter(models.User.username == username).first()
    if db_user:
        # return db_user
        # return UserInDB(**dict(db_user))
        return db_user


def authenticate_user(db: Session, username: str,
                      password: str) -> Optional[models.User]:
    user = get_user(db, username)
    if not user:
        return False
    if not user.check_password(password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(db: Session = Depends(get_db),
                     token: str = Depends(oauth2_scheme)) -> User:
    creditials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Counld't validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise creditials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise creditials_exception
    user = get_user(db, token_data.username)
    if user is None:
        raise creditials_exception
    return user

