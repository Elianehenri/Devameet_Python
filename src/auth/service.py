from fastapi import HTTPException
from .schema import Login


class AuthService:
    def login(self, dto: Login):
        if not (dto.login == 'admin@admin.com' and dto.password == 'senha_segura'):
            raise HTTPException(400, 'Invalid login or password')
        
        return {' message': 'login success'}
