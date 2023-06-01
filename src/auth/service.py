from fastapi import Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src.core.middleware.error import ApiError
from src.core.database import get_db

from .handler import TokenHandler
from .model import User
from .schema import Login, Register, Token



class AuthService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

    def login(self, login_dto: Login):
        user = self.db.query(User).filter(User.username == login_dto.login).first()
        if not user:
            raise ApiError(message="Incorrect username or password", error="Incorrect username or password", status_code=401)  # ApiError(message="Incorrect username or password", error="Incorrect username or password", status_code=401)
        if not self.pwd_context.verify(login_dto.password, user.hashed_password):
            raise ApiError(message="Incorrect username or password", error="Incorrect username or password", status_code=401) # ApiError(message="Incorrect username or password", error="Incorrect username or password", status_code=401)

        token = TokenHandler.create_access_token(user.username)
        return Token(token=token, name=user.name, email=user.username)

    def register(self, dto: Register):
        hashed_password = self.pwd_context.hash(dto.password)

        user = User(
            name=dto.name,
            avatar=dto.avatar,
            username=dto.email,
            hashed_password=hashed_password,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

