from people import Friend
from datetime import datetime

myobj = datetime.now()
day = myobj.day
month = myobj.month
hour = myobj.hour
minute = myobj.minute


def send(friend):
    if day == friend.day and month == friend.month:
        friend.message()


friend1 = Friend("+##########1", "Happy Birthday!", 1, 12)
send(friend1)

friend2 = Friend("+##########2", "Happy Birthday!", 23, 9)
send(friend2)

