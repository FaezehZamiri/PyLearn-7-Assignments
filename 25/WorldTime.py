import time 
import pytz
from  datetime import datetime
from PySide6.QtCore import QThread , Signal 
from Time import Time

class WorldTimeThread(QThread):
    signal = Signal(Time)
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.tehran = pytz.timezone('Asia/Tehran')
            self.tehran_time = datetime.now(self.tehran).strftime("%H:%M:%S")

            self.berlin = pytz.timezone('Europe/Berlin')
            self.berlin_time = datetime.now(self.berlin).strftime("%H:%M:%S")

            self.newyork = pytz.timezone('America/New_York')
            self.newyork_time = datetime.now(self.newyork).strftime("%H:%M:%S")

            time.sleep(1)
            self.signal.emit([self.tehran_time,self.berlin_time,self.newyork_time])