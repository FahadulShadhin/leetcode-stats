from fastapi import FastAPI
from routes import routes
from config.db import DBConfig

db_config = DBConfig()

app = FastAPI()

app.include_router(routes.router)
