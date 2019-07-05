import log.LogThread as LogThread
import time
logThread = LogThread.singlelog


def init():
    global logThread
    if logThread.isAlive() is not True:
        logThread.start()
    pass


def stop():
    if len(logThread.messageQuene) == 0:
        logThread.runState = False
    else:
        time.sleep(3)
        stop()


def send_message(msgEntity):
    pass


def send_message_for_tag(tag, entity):
    if tag == 'Log':
        logThread.receive_msg(entity)
