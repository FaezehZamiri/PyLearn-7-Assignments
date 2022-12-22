class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator =denominator

    def sum(self):
        ...
    def subtraction(self):
        ...
    def multiplication(self):
        ...
    def division(self):
        ...
    def show(self):
        ...


class Time:
    def __init__(self,hour,minute,seconds):
        self.hour = hour
        self.minute = minute
        self.seconds = seconds

    def sum(self):
        ...
    def subtraction(self):
        ...
    def time2seconds(self):
        ...
    def time2minute(self):
        ...
    def time2hour(self):
        ...
    def show(self):
        ...


class DateAD:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def date2hijri(self):
        ...
    def subtraction(self):
        ...
    def show(self):
        ...
