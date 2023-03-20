class Time():
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second =second

    def sum(self):
        self.second += 1

        if self.second >= 60:
            self.second -= 60
            self.minute += 1
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

    def subtraction(self):
        self.second -= 1

        for i in range(3):
            if self.hour < 0:
                self.second *= -1
                self.hour *= -1
                self.minute *= -1
            if self.minute < 0:
                self.minute += 60
                self.hour -= 1
            if self.second <0:
                self.second +=60
                self.minute -=1


