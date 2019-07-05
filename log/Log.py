import entity.messageEntity as MessageEntity
import ThreadManager as Manager


def w(*args):
    if len(args) > 1:
        tag = args[0]
        msg = args[1]
    else:
        tag = "Log"
        msg = args[0]
    m = str(tag) + " | " + str(msg)
    Manager.send_message_for_tag("Log", MessageEntity.MessageEntity(m))