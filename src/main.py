from fastapi import FastAPI
from src.core.config import get_settings


app = FastAPI()


@app.get("/")
def read_root():
    settings = get_settings()
    return {"Hello": "World", 'log_level': settings.log_level}
