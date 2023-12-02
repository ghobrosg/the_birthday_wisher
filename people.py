import pywhatkit
import time


class Friend:
    def __init__(self, number, msg, day: int, month: int):
        self.number = number
        self.msg = msg
        self.day = day
        self.month = month

    def message(self):
        pywhatkit.sendwhatmsg_instantly(self.number, self.msg, 5, tab_close=True)
        time.sleep(5)


class Group:
    def __init__(self, idx, msg, day, month):
        self.idx = idx
        self.msg = msg
        self.day = day
        self.month = month

    def group_message(self):
        pywhatkit.sendwhatmsg_to_group_instantly(self.idx, self.msg, 5, tab_close=True)
        time.sleep(5)
