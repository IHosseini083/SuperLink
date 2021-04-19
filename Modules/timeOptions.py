from datetime import datetime as dt


class TimeOptions:
    def __init__(self):
        self.ctime = dt.now()
    @property
    def year(self):
        return self.ctime.strftime("%Y")
    
    @property
    def month(self):
        return self.ctime.strftime("%m")
    
    @property
    def day(self):
        return self.ctime.strftime("%d")
        
    @property
    def calendar(self):
        return self.ctime.strftime("%Y-%m-%d")
        
    @property
    def clock(self):
        return self.ctime.strftime("%H:%M:%S")
