"""
Endpoint Customers Module
"""
import http
from datetime import datetime
from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.models.validations.customer import Customer
from app.utils.logger import logger

router = APIRouter()


@router.post("/customer")
def customer_post(customer: Customer):
    """
    :param customer:
    :return: HTTP Responses 200, 400
    """
    try:
        logger.info(f"Received data: {customer.json()}")
        return {
            "DateTime": f"{datetime.now()}",
            "Message": "Data imported with success",
        }

    except Exception as err:
        logger.error(f"Error: {err} Route: /")
        content = {
            "Error": f"{err}",
            "DateTime": f"{datetime.now()}",
            "Message": "Import error",
        }

        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content=content)


@router.get("/customer")
def customer_get():
    """
    :return: Customers
    """
    try:
        return JSONResponse(status_code=http.HTTPStatus.OK, content={})

    except Exception as err:
        logger.error(f"Error: {err} Route: ")
        content = {
            "Error": f"{err}",
            "DateTime": f"{datetime.now()}",
            "Message": "Error on get customers",
        }

        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content=content)
