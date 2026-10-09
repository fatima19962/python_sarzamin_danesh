class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def setHour(self, hour):
        self.__hour = hour if 0 <= hour <= 23 else 0

    def setMinute(self, minute):
        self.__minute = minute if 0 <= minute <= 59 else 0

    def setSecond(self, second):
        self.__second = second if 0 <= second <= 59 else 0

    def getHour(self): return self.__hour
    def getMinute(self): return self.__minute
    def getSecond(self): return self.__second

    def copy(self):
        return Time(self.__hour, self.__minute, self.__second)

    def __add__(self, other):
        total_seconds = (self.__hour * 3600 + self.__minute * 60 + self.__second) + \
                        (other.__hour * 3600 + other.__minute * 60 + other.__second)
        total_seconds %= 24 * 3600
        h, rem = divmod(total_seconds, 3600)
        m, s = divmod(rem, 60)
        return Time(h, m, s)

    def __sub__(self, other):
        total_seconds = (self.__hour * 3600 + self.__minute * 60 + self.__second) - \
                        (other.__hour * 3600 + other.__minute * 60 + other.__second)
        total_seconds %= 24 * 3600
        h, rem = divmod(total_seconds, 3600)
        m, s = divmod(rem, 60)
        return Time(h, m, s)

    def addHour(self, hour):
        res = self.copy()
        res.__hour = (res.__hour + hour) % 24
        return res

    def addMinute(self, minute):
        total_seconds = self.__hour * 3600 + self.__minute * 60 + self.__second + minute * 60
        total_seconds %= 24 * 3600
        h, rem = divmod(total_seconds, 3600)
        m, s = divmod(rem, 60)
        return Time(h, m, s)

    def addSecond(self, second):
        total_seconds = self.__hour * 3600 + self.__minute * 60 + self.__second + second
        total_seconds %= 24 * 3600
        h, rem = divmod(total_seconds, 3600)
        m, s = divmod(rem, 60)
        return Time(h, m, s)

    def subHour(self, hour):
        return self.addHour(-hour)

    def subMinute(self, minute):
        return self.addMinute(-minute)

    def subSecond(self, second):
        return self.addSecond(-second)

    def AMPM(self):
        hour = self.__hour
        suffix = "AM"
        if hour == 0:
            hour = 12
        elif hour == 12:
            suffix = "PM"
        elif hour > 12:
            hour -= 12
            suffix = "PM"
        return f"{hour:02}:{self.__minute:02}:{self.__second:02} {suffix}"

    def __str__(self):
        return f"({self.__hour:02}:{self.__minute:02}:{self.__second:02})"

time1=input("enter time1").split(":")
time2=input("enter time2").split(":")
t1=Time(int(time1[0]),int(time1[1]),int(time1[2]))
t2=Time(int(time2[0]),int(time2[1]),int(time2[2]))
t3=t1+t2
print(str(t1)+"+"+str(t2)+"="+str(t3))
t3=t1-t2
print(str(t1)+"-"+str(t2)+"="+str(t3))
hour=int(input("enter hour to add"))
t3=t1.addHour(hour)
print(str(t1)+" + "+str(hour)+" hour = "+str(t3))
t3=t2.subHour(hour)
print(str(t2)+" - "+str(hour)+" hour = "+str(t3))
minute=int(input("enter minute to add"))
t3=t1.addMinute(minute)
print(str(t1)+" + "+str(minute)+" minute = "+str(t3))
t3=t2.subMinute(minute)
print(str(t2)+" - "+str(minute)+" minute = "+str(t3))
second=int(input("enter second to add"))
t3=t1.addSecond(second)
print(str(t1)+" + "+str(second)+" second = "+str(t3))
t3=t2.subSecond(second)
print(str(t2)+" - "+str(second)+" second = "+str(t3))
print(str(t1)+" in AM/PM format is "+t1.AMPM())
print(str(t2)+" in AM/PM format is "+t2.AMPM())
