from logging import getLogger, DEBUG


class Logger:
    def __init__(self, log_name=__name__):
        self.logger = getLogger(log_name)
        self.logger.setLevel(DEBUG)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
