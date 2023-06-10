from pydantic import BaseModel, Field

#atualizar a position

class UpdatePosition(BaseModel):
    x: int = Field(..., ge=0, le=7)
    y: int = Field(..., ge=0, le=7)
    orientation: str = Field(..., regex='(top|right|bottom|left)')
#mudar o estado de mutado e nao mutado


class ToggleMute(BaseModel):
    user_id: str
    link: str
    muted: bool
    user_mute: str
#desafio


class CreateDirectionPosition(BaseModel):
    direction: str = Field(..., regex='(up|down|left|right )')
