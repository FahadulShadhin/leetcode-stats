from fastapi import FastAPI
from routes import routes
from config import Config

config = Config()
config.connectDB()

app = FastAPI()

app.include_router(routes.router)
