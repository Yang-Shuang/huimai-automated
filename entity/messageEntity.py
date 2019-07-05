import time;

class MessageEntity(object):
    def __init__(self,msg):
        self.timelong = time.localtime();
        self.msg = msg;
    def setTime(self,t):
        self.timelong = t;
    def setMsg(self,msg):
        self.msg = msg;
    def __repr__(self):
        self.timeStr = time.strftime("%Y-%m-%d %H:%M:%S", self.timelong);
        return self.timeStr + ' | ' + self.msg;