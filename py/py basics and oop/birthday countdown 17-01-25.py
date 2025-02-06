"""
Birthday counter
use datetime to get current date. have user enter birthday in specific format. countdown to their next birthday
"""

from datetime import datetime
now = datetime.now() # year, month, day, hour, minute, second
bday = input("What is your birthday? In the form of MM DD\n> ")
blist = bday.split(" ")
month = int(blist[0])
day = int(blist[1])
if datetime.now()>datetime(int(now.year), month, day):
    difference = datetime(int(now.year+1), month, day) - datetime.now()
else:
    difference = datetime(int(now.year), month, day) - datetime.now()

print(f"Days until your birthday: {difference}")