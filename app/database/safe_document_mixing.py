"""
Safe Document Mixing Module
"""
import time
import pymongo

from app.utils.logger import logger


class SafeDocumentMixin:
    """
    SafeDocumentMixing Class
    """
    def save_safe(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        for attempt in range(5):
            try:
                return self.save(*args, **kwargs)
            except pymongo.errors.AutoReconnect as err:
                wait_t = 0.5 * pow(2, attempt)  # exponential back off
                logger.warning("PyMongo auto-reconnecting... %s. Waiting %.1f seconds.", str(err), wait_t)
                time.sleep(wait_t)

    @classmethod
    def objects_safe(cls, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        for attempt in range(5):
            try:
                return cls.objects(*args, **kwargs)
            except pymongo.errors.AutoReconnect as err:
                wait_t = 0.5 * pow(2, attempt)  # exponential back off
                logger.warning("PyMongo auto-reconnecting... %s. Waiting %.1f seconds.", str(err), wait_t)
                time.sleep(wait_t)

    def update_safe(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        for attempt in range(5):
            try:
                return self.update(*args, **kwargs)
            except pymongo.errors.AutoReconnect as err:
                wait_t = 0.5 * pow(2, attempt)  # exponential back off
                logger.warning("PyMongo auto-reconnecting... %s. Waiting %.1f seconds.", str(err), wait_t)
                time.sleep(wait_t)
