import time
from PySide6.QtCore import QThread , Signal
from Time import Time

class TimerThread(QThread):
    signal = Signal(Time)
    def __init__(self,h,m,s):
        super().__init__()
        self.h = h
        self.m = m 
        self.s = s
        self.time = Time(self.h,self.m,self.s)

    def run(self):
        while True:
            self.time.subtraction()
            self.signal.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.second = 0
        self.time.minute = 16
        self.time.hour = 0
        self.signal.emit(self.time)
