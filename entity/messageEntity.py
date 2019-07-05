import time


class MessageEntity(object):
    def __init__(self, msg):
        self.time = time.localtime()
        self.msg = msg

    def set_time(self, t):
        self.time = t

    def set_msg(self, msg):
        self.msg = msg

    def __repr__(self):
        self.timeStr = time.strftime("%Y-%m-%d %H:%M:%S", self.time)
        return self.timeStr + ' | ' + self.msg
