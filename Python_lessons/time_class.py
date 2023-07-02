class TimeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        extra_minutes = second // 60
        extra_hours = (minute + extra_minutes) // 60
        self.__second = second % 60
        self.__minute = (minute + extra_minutes) % 60
        self.__hour = (hour + extra_hours) % 24
      
    @property
    def hour(self):
        return self.__hour
    
    @hour.setter
    def hour(self, new_hour):
        if new_hour < 0 or new_hour > 24:
            raise TimeError("Invalid hour value")
        extra_minutes = self.__second // 60
        extra_hours = (self.__minute + extra_minutes) // 60
        self.__hour = (new_hour + extra_hours) % 24
    
    def __repr__(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"
    
    def add_hour(self, h):
        self.hour = (self.hour + h) % 24
    
    def add_minute(self, m):
        extra_hours = (self.__minute + m) // 60
        self.__minute = (self.__minute + m) % 60
        self.add_hour(extra_hours)
    
    def add_second(self, s):
        extra_minutes = (self.__second + s) // 60
        self.__second = (self.__second + s) % 60
        self.add_minute(extra_minutes)


time_class = Time(25, 61, 60)
#print(time_class)
#time_class.add_second(2)
#print(time_class))
print(time_class)