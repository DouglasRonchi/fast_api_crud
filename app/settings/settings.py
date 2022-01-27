"""
Settings Module
"""
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """ Backend Inventory Settings"""

    MONGODB_HOST: str = Field(..., env="MONGODB_URI")
