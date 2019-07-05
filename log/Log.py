import entity.messageEntity as MessageEntity;
import ThreadManager as manager;


def l(*args):
    if len(args) > 1:
        tag = args[0];
        msg = args[1];
    else:
        tag = "Log";
        msg = args[0];
    m = str(tag) + " | " + str(msg);
    manager.sendMessageForTag("Log",MessageEntity.MessageEntity(m))
    pass;