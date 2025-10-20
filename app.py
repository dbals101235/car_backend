from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from config import config
from routers.cars import router as cars_router

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(config.DB_URL)
    app.database = app.mongodb_client[config.DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(cars_router, prefix="/cars", tags=["cars"])

@app.get("/")
async def root():
    return {"message": "Root working!"}
