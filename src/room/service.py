from fastapi import Depends
from src.core.database import SessionLocal, get_db

from src.core.middleware.error import ApiError

from src.auth.model import User
from src.meet.model import Meet

from .model import Position
from .schema import ToggleMute, UpdatePosition, CreateDirectionPosition


class RoomService:
    def __init__(self, db: SessionLocal = Depends(get_db)):
        self.db = db
# encontrar a sala

    def get_room(self, link: str):
        meet = self._get_meet(link)
        objects = meet.object_meets
        return {
            'link': link,
            'name': meet.name,
            'color': meet.color,
            'objects': objects
        }
# metodo listar position do usuario

    def list_users_position(self, link: str):
        meet = self._get_meet(link)
        return self.db.query(Position).filter(Position.meet_id == meet.id).all()
# metodo deletar position

    def delete_users_position(self, client_id: str):
        self.db.query(Position).filter(
            Position.client_id == client_id).delete()
        self.db.commit()
# atualizar posiçao de um determinado usuario



    def create_direction_position(self, user_id, link, client_id, dto: CreateDirectionPosition):
        meet = self._get_meet(link)
        user = self.db.query(User).filter(User.id == user_id).first()
    
        # criar objeto de position
        position = self.db.query(Position).filter(Position.client_id == client_id).one()

        if dto.direction == 'right' and position.orientation == 'right' and position.x < 7:
            position.x += 1
        elif dto.direction == 'left' and position.orientation == 'left' and position.x > 0:
            position.x -= 1
        elif dto.direction == 'up' and position.orientation == 'back' and position.y > 0:
            position.y -= 1
        elif dto.direction == 'down' and position.orientation == 'front' and position.y < 7:
            position.y += 1

        if dto.direction == 'right' and position.orientation != 'right':
            position.orientation = 'right'
        elif dto.direction == 'left' and position.orientation != 'left':
            position.orientation = 'left'
        elif dto.direction == 'up' and position.orientation != 'back':
            position.orientation = 'back'
        elif dto.direction == 'down' and position.orientation != 'front':
            position.orientation = 'front'

        self.db.commit()

    def update_user_position(self, user_id, link, client_id, dto: UpdatePosition):
        meet = self.__get_meet(link)
        user = self.db.query(User).filter(User.id == user_id).first()
        
        position = Position(
            x=dto.x,
            y=dto.y,
            orientation=dto.orientation,
            user_id=user.id,
            meet_id=meet.id,
            client_id=client_id,
            name=user.name,
            avatar=user.avatar
        )
        # pegar todos usuario dessa sala, todas posiçoes dessa sala,ai fazemos a verificaçao, se o usuario ja estiver nesta sala
        # só atualiza a posiçao dele,senao a gente adiciona um novo usuario
        users_in_room = self.db.query(Position).filter(
            Position.meet_id == meet.id).all()

        if len(users_in_room) > 20:
            raise Exception('Meet is full')
        # verificar se o usuario ja esta na sala e se tiver mais que 20
        if any(user for user in users_in_room if user.user_id == user.id or user.client_id == client_id):
            position = self.db.query(Position).filter(
                Position.client_id == client_id).one()
            position.x = dto.x
            position.y = dto.y
            position.orientation = dto.orientation
        elif len(users_in_room) > 20:
            raise ApiError(message="Meet is full",
                           error="Update Meet Error", status_code=400)

        else:
            self.db.add(position)
            self.db.commit()

        # metodo atualizar o fato de estar mudo ou nao
        # desafio muted
        # create Permitir que o criador da sala, possa mutar e desmutar outros participantes. O resto dos usuários só poderá mutar e desmutar a si mesmo

    def update_user_mute(self, dto: ToggleMute):
        meet = self._get_meet(dto.link)
        
        owner_user = self.db.query(User).filter(User.username == meet.owner).first()
        
        user = self.db.query(User).filter(User.id == dto.user_id).first()
        
        user_mute = self.db.query(User).filter(User.id == dto.user_to_mute).first()
    
        if user.id == user_mute.id or user.id == owner_user.id:
            self.db.query(Position)\
                .filter(Position.meet_id == meet.id)\
                .filter(Position.user_id == user_mute.id)\
                .update({'muted': dto.muted})
    
        self.db.commit()

    # metodo achar a sala pelo link

    def _get_meet(self, link):
        return self.db.query(Meet).filter(Meet.link == link).one()
