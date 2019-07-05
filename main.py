import ThreadManager
import log
import time

Tag = 'main.py'


def start():
    ThreadManager.init()
    log.w('------start test------')
    for i in range(6):
        time.sleep(3)
        log.w(Tag, "i  :  " + str(i))
    ThreadManager.stop()
    pass


start()
