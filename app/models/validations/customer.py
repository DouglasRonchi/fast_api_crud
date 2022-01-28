"""
Customer validation module
"""
from pydantic import BaseModel, Field


class Customer(BaseModel):
    """
    Customer Validation Class
    """

    name: str = Field(..., example="Lorem Ipsum")
    age: int = Field(..., example=25)
