import time
from PySide6.QtCore import QThread , Signal 
from Time import Time

class StopWatchThread(QThread):
    signal = Signal(Time)
    def __init__(self):
        super().__init__()
        self.time = Time(0,0,0)
    
    def run(self):
        while True:
            self.time.sum()
            self.signal.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.second = 0
        self.time.minute = 0
        self.time.hour = 0
        self.signal.emit(self.time)