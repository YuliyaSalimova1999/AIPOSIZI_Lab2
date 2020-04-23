import logging
import logging.handlers
import os

class Logger:
    logger = logging.getLogger("simple")
    logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(
              'log_journal.log', maxBytes=1024*1024)

    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def log_in_file(self, message):
        self.logger.info(message)

