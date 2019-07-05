import threading;
import entity.messageEntity;
class BaseThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self);
        pass;
    def receiveMsg(self,message):
        pass;
    def sendMsg(message):
        pass;
    def getTag(self):
        raise NotImplementedError(self.name + " 此线程没有重写实现此方法");