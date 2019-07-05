import threading;
import ThreadManager;
import log;
import time;
import sys;
import requests;

Tag = 'main.py';

def start():
    ThreadManager.init();
    ThreadManager.init();
    ThreadManager.init();
    ThreadManager.init();
    log.l('------start test------');    
    # log.log(sys.path);
    # requests.get();
    for i in range(6):
        time.sleep(3);
        log.l(Tag,"i  :  " + str(i));
    ThreadManager.stop();
    pass;

start();
