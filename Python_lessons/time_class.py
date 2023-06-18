class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.second = second % 60
        extra_minutes = second // 60
        self.minute = (minute + extra_minutes) % 60
        extra_hours = (minute + extra_minutes) // 60
        self.hour = (hour + extra_hours) % 24
    
    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    def add_hour(self, h):
        self.hour = (self.hour + h) % 24
    
    def add_minute(self, m):
        self.minute = (self.minute + m) % 60
        extra_hours = (self.minute + m) // 60
        self.hour = (self.hour + extra_hours) % 24
    
    def add_second(self, s):
        self.second = (self.second + s) % 60
        extra_minutes = (self.second + s) // 60
        self.minute = (self.minute + extra_minutes) % 60
        extra_hours = (self.minute + extra_minutes) // 60
        self.hour = (self.hour + extra_hours) % 24

time_class = Time(1,241,121)
#time_class.add_second(0)
#time_class.add_hour(25)
print(time_class)
