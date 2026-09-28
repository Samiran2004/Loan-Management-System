from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI, Request
from pymongo import AsyncMongoClient
from pymongo import server_api
from pymongo.server_api import ServerApi

from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI)-> AsyncIterator[None]:
    client = AsyncMongoClient(
        settings.mongodb_url,
        server_api = ServerApi(
            version="1",
            strict=True,
            deprecation_errors=True
        ),
    )
    
    await client.admin.command("ping")
    
    app.state.mongodb_client = client
    app.state.mongodb = client[settings.mongodb_database]
    
    print("MongoDB Connected.")
    
    try:
        yield
    finally:
        await client.close()
        print("MongoDB connection closed.")

def get_database(request: Request):
    return request.app.state.mongodb