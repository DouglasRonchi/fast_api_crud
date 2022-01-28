"""
Looger Module
"""
import logging


class Logger:
    """
    Logger class
    """

    INFO = logging.INFO
    DEBUG = logging.DEBUG
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITITAL = logging.CRITICAL

    def __init__(self, name=__name__):
        # create logger
        self.logger_worker = logging.getLogger(name)
        self.__config_logger()

    def __config_logger(self):
        """
        Config logger
        """
        self.logger_worker.setLevel(self.DEBUG)
        self.__config_handler(logging.DEBUG)
        self.__config_handler(logging.DEBUG, "debug.log")

    def __config_handler(self, level, file=None):
        console_handler = logging.FileHandler(file) if file else logging.StreamHandler()
        console_handler.setLevel(level)
        formatter = logging.Formatter(
            " %(asctime)s | %(levelname)s | %(module)s:%(lineno)s => %(message)s"
        )
        console_handler.setFormatter(formatter)
        self.logger_worker.addHandler(console_handler)

    def get_logger(self):
        """
        Log message
        """
        return self.logger_worker

    def set_level(self, level):
        """Set Logger level"""
        self.logger_worker.setLevel(level)


logger = Logger().get_logger()
