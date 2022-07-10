import logging
import inspect


class Utils:
    def custom_logger(log_level=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(Utils.__name__)
        # set log level
        logger.setLevel(log_level)
        # create console handler or file handler and set the log level
        fh = logging.FileHandler("automation_log.log", mode='w')
        # create formatter how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # add formatter to console or file handler
        fh.setFormatter(formatter)
        # add console or file handler to logger
        logger.addHandler(fh)
        return logger


