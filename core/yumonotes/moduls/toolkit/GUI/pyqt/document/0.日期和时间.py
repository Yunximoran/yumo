from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

# 当前时间
now = QDate.currentDate()  # 日期
dtime = QDateTime.currentDateTime()  # 日期和时间
ntime = QTime.currentTime()  # 时间


class DT:
    now = QDate.currentDate()
    dtime = QDateTime.currentDateTime()
    nowTime = QTime.currentTime()

    ObjList = [now, dtime, nowTime]
    ObjNameList = ['Date', 'Date Time', 'Time']

    ISO = Qt.DateFormat.ISODate
    RFC = Qt.DateFormat.RFC2822Date

    def __init__(self):
        for i, Name in enumerate(self.ObjNameList):
            print(f"current: {Name} is:")
            self.Out(self.ObjList[i])

    def Out(self, Obj):
        print("\tFormat ISO", Obj.toString(self.ISO))
        print("\tFormat RFC", Obj.toString(self.RFC))
        print()


class UTF:
    def __init__(self):
        pass

#
# # UTC时间
# print("Universal datetime:", dtime.toUTC().toString(Qt.DateFormat.ISODate))
# print(f"the offset form UTC is: {dtime.offsetFromUtc()}")  # 获取本地时间 和 标准时间
# print("local datetime: ", dtime.toString(Qt.DateFormat.ISODate))


# b = QDate(1945, 5, 7)
# print(b.daysInYear())
# print(b.daysInMonth())

C = DT()

