import logging

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


logging.basicConfig(format=bcolors.WARNING+bcolors.BOLD+"%(asctime)s %(levelname)s: %(message)s",
                    datefmt='%A %B %d, %Y %I:%M:%S %p',
                    level="INFO")
def start_logger(module):
    logger = logging.getLogger(module)
    return logger