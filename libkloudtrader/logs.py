import logging


def start_logger(module):
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s",
                        datefmt='%A, %B %d, %Y %I:%M:%S %p',
                        level="INFO")
    logging.getLogger('boto3').setLevel(logging.CRITICAL)
    logging.getLogger('botocore').setLevel(logging.CRITICAL)
    logger = logging.getLogger(module)
    return logger
