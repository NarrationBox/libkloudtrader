import logging


def start_logger(module, ignore_module=None):
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s",
                        datefmt='%A, %B %d, %Y %I:%M:%S %p',
                        level="INFO")
    logging.getLogger('boto3').setLevel(logging.CRITICAL)
    logging.getLogger('botocore').setLevel(logging.CRITICAL)
    if ignore_module:
        logging.getLogger(ignore_module).setLevel(logging.CRITICAL)
    logger = logging.getLogger(module)
    return logger
