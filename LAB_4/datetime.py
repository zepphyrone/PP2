# 1
import datetime


tday = datetime.date.today()
tdelta = datetime.timedelta(days = 5)
subtract = tday - tdelta
print(subtract)

# 2
tday = datetime.date.today()
yesterday = tday - datetime.timedelta(days = 1)
tomorrow = tday + datetime.timedelta(days = 1)
print(yesterday, tday, tomorrow, sep="\n")

# 3
t = datetime.datetime.today()
drop = t.replace(microsecond=0)
print(drop)

# 4
tday = datetime.date.today()
b = datetime.date(2006, 1, 23)
diff = tday - b
print(diff.total_seconds())