"""
Mongo Repository Module
"""
import mongoengine

from app.settings.settings import Settings
from app.utils.logger import logger


class MongoDB:
    """
    MongoDB Class
    """

    def __init__(self):
        self.settings = Settings()
        self.__set_connection()

    def __set_connection(self):
        """
        :return: None
        """
        logger.debug("Connecting to Mongo")
        mongoengine.connect(host=self.settings.MONGODB_HOST)
        logger.debug("Connected to Mongo")
