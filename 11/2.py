class Time():
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second =second

    def sum(self, other):
        result = Time()
        result.hour = self.hour + other.hour
        result.minute = self.minute + other.minute
        result.second = self.second + other.second

        if result.second >= 60:
            result.second -= 60
            result.minute += 1
        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1
        return result

    def subtraction(self, other):
        result = Time()
        result.hour = self.hour - other.hour
        result.minute = self.minute - other.minute
        result.second = self.second - other.second

        for i in range(3):
            if result.hour < 0:
                result.second *= -1
                result.hour *= -1
                result.minute *= -1
            if result.minute < 0:
                result.minute += 60
                result.hour -= 1
            if result.second <0:
                result.second +=60
                result.minute -=1

        return result

    def time2second(self):
        result = self.hour * 3600 + self.minute * 60 + self.second
        print(result)

    def second2time(self):
        result=Time()
        result.hour = self.second // 3600
        result.minute = ( self.second - result.hour * 3600) // 60
        result.second = self.second - result.hour * 3600 - result.minute * 60
        return result

    def GMT2local(self):
        result = Time()
        result.hour = self.hour - 3
        result.minute = self.minute - 30
        result.second = self.second

        for i in range(3):
            if result.hour < 0:
                result.second *= -1
                result.hour *= -1
                result.minute *= -1
            if result.minute < 0:
                result.minute += 60
                result.hour -= 1
            if result.second <0:
                result.second +=60
                result.minute -=1
        return result

    def show(self):
        print(f"{self.hour} : {self.minute} : {self.second}")


