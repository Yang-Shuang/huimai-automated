import threading


class BaseThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def receive_msg(self, message):
        pass

    def send_msg(message):
        pass

    def get_tag(self):
        raise NotImplementedError(self.name + " 此线程没有重写实现此方法")
