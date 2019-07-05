import log.LogThread as LogThread;
import time;
logThread = LogThread.singleLog;
def init():
    global logThread;
    if (logThread.isAlive() != True):
        logThread.start();
    pass;
def stop():
    if len(logThread.messageQuene) == 0:
        logThread.runState = False;
    else:
        time.sleep(3);
        stop();
def sendMessage(msgEntity):
    pass
def sendMessageForTag(tag,msgEntity):
    if tag == 'Log':
        logThread.receiveMsg(msgEntity);
    pass;