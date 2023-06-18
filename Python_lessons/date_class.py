class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

        # Check if the date is valid
        if self.day > self.get_days_in_month():
            self.day = self.get_days_in_month()

        if self.month > 12:
            self.month = 12

        if self.day > 365 + self.year:
            self.day = 365 + self.year

        if self.month > 12 + self.year:
            self.month = 12 + self.year

    def __repr__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    def add_day(self, days):
        self.day += days

        while self.day > self.get_days_in_month():
            self.day = self.get_days_in_month()
            self.month += 1

            if self.month > 12:
                self.month = 1
                self.year += 1

    def add_month(self, months):
        self.month += months

        while self.month > 12:
            self.month = 12
            self.year += 1

    def add_year(self, years):
        self.year += years

    def __is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def get_days_in_month(self):
        if self.month == 2:
            if self.__is_leap_year():
                return 29
            else:
                return 28
        elif self.month in [4, 6, 9, 11]:
            return 30
        else:
            return 31
        
date_class = Date(2015,13,8)
print(date_class)