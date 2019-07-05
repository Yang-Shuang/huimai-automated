import base.BaseThread as BaseThread;
import time;
logPath = 'log/file/';
class LogThread (BaseThread.BaseThread):
    def __init__(self):
        super().__init__();
        t = time.time();
        self.threadID = 'LogThread' + str(t);
        self.name = 'LogThread' + str(t);
        self.runState = True;
        self.messageQuene = [];
        self.index = 1;
        pass;
    def add(self):
        self.index += 1;
        print(self.index);
    def run(self):
        print('-----log thread start-----');
        global logPath;
        logPath = logPath + time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()) + '.txt';
        while self.runState:
            if len(self.messageQuene) > 0:
                msg = self.messageQuene[0];
                print(msg);
                with open(logPath,'a') as f:
                    f.write(str(msg) + '\n');
                self.messageQuene.remove(msg);
    def receiveMsg(self, message):
        self.messageQuene.append(message);
def singleLog():
    return singleLog;
singleLog = LogThread();
del LogThread;