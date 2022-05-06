# -*- coding: utf-8 -*-

import logging, os, datetime, inspect

LOGGING_FOLDER = 'log'

def _getLogFilePath():
    x = datetime.datetime.now()
    logName = x.strftime("%Y_%m_%d_%H_%M_%S")+'.log'
    return os.path.join(LOGGING_FOLDER,logName)

def configureLogger():
    
    scriptFileName = os.path.basename(inspect.getfile(inspect.currentframe()))
    logger = logging.getLogger(scriptFileName)
    logger.setLevel(logging.DEBUG)
    logFilePath = _getLogFilePath()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(threadName)s - %(message)s')
    handler = logging.FileHandler(logFilePath)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger,handler  
    