# -*- coding: utf-8 -*-

import logging, os, datetime, inspect, errno

LOGGING_FOLDER = 'log'

def _getLogFilePath():
    x = datetime.datetime.now()
    logName = x.strftime("%Y_%m_%d_%H_%M_%S")+'.log'
    return os.path.join(LOGGING_FOLDER,logName)

def createFolder():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    logPath = os.path.join(path,LOGGING_FOLDER)
    try:
        os.mkdir(logPath)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
        
def configureLogger():
    
    scriptFileName = os.path.basename(inspect.getfile(inspect.currentframe()))
    logger = logging.getLogger(scriptFileName)
    logger.setLevel(logging.DEBUG)
    logFilePath = _getLogFilePath()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(threadName)s - %(message)s')
    """
    #Create file in case it didn't exist
    
    try:
        f = open(logFilePath,"x")
    finally:
        f.close()
     """
    createFolder()
    handler = logging.FileHandler(logFilePath)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger,handler  

def removeLogger(logger, handler):
    
    logger.removeHandler(handler)
    handler.close()
    
if __name__ == "__main__":
    logger,handler = configureLogger()
    
    logger.removeHandler(handler)
    handler.close()