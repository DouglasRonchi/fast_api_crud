"""
Main Module
"""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware

from app.endpoints.v1 import router_v1
from app.database.mongo_repository import MongoDB
from app.utils.logger import logger

app = FastAPI(title="CUSTOMERS CRUD")


@app.on_event("startup")
async def create_conn_db():
    """
    This method create the mongo DB connection

    :return: None
    """
    MongoDB()
    logger.info("Starting customers crud...")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_v1, prefix="/v1")
# app.include_router(router_v2, prefix="/v2")


def custom_openapi():
    """
    Custom Open API method
    :return: None
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Customers Crud",
        version="1.1.0",
        description="Customers Crud",
        routes=app.routes,

        servers=[{"url": "http://127.0.0.1:8000/"}]
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
