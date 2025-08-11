import datetime
class Flight:
    def __init__(self, flight_no, dep_time):
        self.flight_no = flight_no
        self.dep_time = dep_time # UTC timestamp
    def flight_time_convert(self):
        dt = datetime.datetime.utcfromtimestamp(self.dep_time)
        # fix_2 修复时间格式（将“年/月/日”改为“-”分隔）
        return dt.strftime("%Y-%m-%d %H:%M")