import logging
import coloredlogs

coloredlogs.DEFAULT_FIELD_STYLES = {'asctime': {'color': 'green'}}
coloredlogs.DEFAULT_LEVEL_STYLES = {
    'critical': {
        'color': 'red'
    },
    'debug': {
        'color': 'white'
    },
    'error': {
        'color': 'red',
        'bold': True
    },
    'info': {
        'color': 'cyan',
        'bold': True
    },
    'notice': {
        'color': 'magenta',
        'bold': True
    },
    'spam': {
        'color': 'green',
        'faint': True
    },
    'success': {
        'color': 'green',
        'bold': True
    },
    'verbose': {
        'color': 'blue'
    },
    'warning': {
        'color': 'yellow',
        'bold': True
    }
}
coloredlogs.install(fmt="%(asctime)s: %(message)s",
                    datefmt='%A %Y-%m-%d %I:%M:%S %p',
                    level="INFO")
def init_logger(module):
    logger = logging.getLogger(module)
    return logger