"""
Routers Module
"""
from fastapi import APIRouter

from app.endpoints.v1 import endpoint_customers

router_v1 = APIRouter()

router_v1.include_router(endpoint_customers.router, tags=["customers"])
