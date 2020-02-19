import logging


__logger = logging.getLogger('GlobalLogger')
__logger.setLevel(logging.INFO)
__handler = logging.FileHandler('runtime.log')
__handler.setFormatter(logging.Formatter('[%(levelname)s]%(asctime)s: %(message)s'))
__logger.addHandler(__handler)

def INFO(*args):
  __logger.info(*args)

def ERROR(*args):
  __logger.error(*args)

def FATAL(*args):
  __logger.critical(*args)

def WARN(*args):
  __logger.warning(*args)

def DEBUG(*args):
  __logger.debug(*args)

