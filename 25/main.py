import time
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QThread , Signal
from ui_main_window import Ui_MainWindow
from Time import Time
from Database import Database
from StopWatch import StopWatchThread
from WorldTime import WorldTimeThread
from Timer import TimerThread
from Alarm import AlarmThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ###########    Alarm    ############
        self.db = Database()
        self.show_alarm()
        self.ui.btn_add_alarm.setText('+')
        self.ui.btn_add_alarm.clicked.connect(self.new_alarm)
        self.thread_alarm = AlarmThread()
        self.thread_alarm.start()
        self.thread_alarm.signal.connect(self.notif_alarm)


        ########### Stop Watch ############
        self.thread_stopwatch = StopWatchThread()
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)
        self.thread_stopwatch.signal.connect(self.show_number_stopwatch)

        ###########   Timer    ############
        self.second = int(self.ui.lineEdit_second_timer.text())
        self.minute = int(self.ui.lineEdit_min_timer.text())
        self.hour = int(self.ui.lineEdit_hour_timer.text())
        self.thread_timer = TimerThread(self.hour,self.minute,self.second)
        self.t = Time(self.hour,self.minute,self.second)
        self.show_number_timer(self.t)
        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)
        self.thread_timer.signal.connect(self.show_number_timer)

        ########### World Time ############
        self.thread_worldtime = WorldTimeThread()
        self.thread_worldtime.signal.connect(self.show_time)
        self.thread_worldtime.start()


    ########### World Time ############
    def show_time(self,time):
        self.ui.time_tehran.setText(str(time[0]))
        self.ui.time_berlin.setText(str(time[1]))
        self.ui.time_newyork.setText(str(time[2]))

    ###########   Timer    ############
    def show_number_timer(self,time):
        self.ui.lineEdit_hour_timer.setText(f"{time.hour}")
        self.ui.lineEdit_min_timer.setText(f"{time.minute}")
        self.ui.lineEdit_second_timer.setText(f"{time.second}")
        if time.second == 0 and time.minute == 0 and time.hour == 0:
            self.stop_timer()
            msg = QMessageBox()
            msg.setWindowTitle('Timer')
            msg.setText("Timer Ended!")
            msg.setStandardButtons(QMessageBox.Reset | QMessageBox.Close)
            msg.setIcon(QMessageBox.Question)
            button = msg.exec()
            if button == QMessageBox.Reset:
                self.reset_timer()
    def start_timer(self):
        self.thread_timer.start()  
    def stop_timer(self):
        self.thread_timer.terminate()
    def reset_timer(self):
        self.thread_timer.reset()
        self.stop_timer()

    ########### Stop Watch ############
    def show_number_stopwatch(self,time):
        self.ui.label_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")
    def start_stopwatch(self):
        self.thread_stopwatch.start()
    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()
    def reset_stopwatch(self):
        self.thread_stopwatch.reset()
        self.stop_stopwatch()

    ###########    Alarm    ############
    def show_alarm(self):
        for i in reversed(range(self.ui.GL_Alarms.count())): 
            self.ui.GL_Alarms.itemAt(i).widget().setParent(None)
        self.Alarms = self.db.get_alarms()
        for i in range(len(self.Alarms)):
            new_label = QTimeEdit()
            new_btn = QPushButton()
            edit_btn = QPushButton()
            end_btn = QPushButton()
            new_label.setSpecialValueText(self.Alarms[i][1])
            new_btn.setText("❌")
            edit_btn.setText('📝')
            end_btn.setText('✔')
            new_label.setEnabled(False)
            end_btn.setEnabled(False)
            new_label.setDisplayFormat('hh:mm:ss AP')

            new_btn.setStyleSheet("border:none;font-size:18pt") 
            new_label.setStyleSheet("height:20px;border-radius:10px;font-family:'Seven Segment'; font-size:20pt;color:rgb(255, 138, 5);") 
            edit_btn.setStyleSheet("border:none;font-size:18pt")
            end_btn.setStyleSheet("border:none;font-size:18pt")

            self.ui.GL_Alarms.addWidget(new_label,i,0)
            self.ui.GL_Alarms.addWidget(new_btn,i,1)
            self.ui.GL_Alarms.addWidget(edit_btn,i,2)
            self.ui.GL_Alarms.addWidget(end_btn,i,3)

            new_btn.clicked.connect(partial(self.remove_alarm,self.Alarms[i][1],[new_label,new_btn,edit_btn,end_btn]))
            edit_btn.clicked.connect(partial(self.edit_alarm,self.Alarms[i][0],new_label,end_btn))
        self.update_alarm_list()
        

    def new_alarm(self):
        new_time = self.ui.timeEdit.text()
        feedback = self.db.add_new_alarm(new_time)
        if feedback == True:
            self.show_alarm()
        else:
            msg = QMessageBox()
            msg.setText('Try Again!')
            msg.exec()

    def remove_alarm(self, time,Array):  
        feedback = self.db.remove_alarm(time)
        if feedback == True:
            for widget in Array:
                widget.deleteLater()
        else:
            msg_box = QMessageBox()
            msg_box.setText("Try Again!")
            msg_box.exec()
        self.update_alarm_list()

    def edit_alarm(self,id,time,btn):
        time.setEnabled(True)
        btn.setEnabled(True)
        btn.clicked.connect(partial(self.done_edit,id,time,btn))

    def done_edit(self,id,time,btn):
        new_time = time.text()
        feedback = self.db.edit_alarm(id,new_time)
        if feedback == True:
            time.setEnabled(False)
            btn.setEnabled(False)
            self.show_alarm()
        else:
            msg_box = QMessageBox()
            msg_box.setText("Try Again!")
            msg_box.exec()
        self.update_alarm_list()

    def update_alarm_list(self):
        self.alarm_list = []
        self.Alarms = self.db.get_alarms()
        for i in range(len(self.Alarms)):
            self.alarm_list.append(self.Alarms[i][1])
        return self.alarm_list 
    
    def notif_alarm(self,mytime):
        self.alarm_list = self.update_alarm_list()
        for i in range(len(self.alarm_list)):
            alarm = self.alarm_list[i][0:8]
            #print(alarm,mytime)
            if  alarm == mytime:
                msg = QMessageBox()
                msg.setWindowTitle('Alarm')
                msg.setText(f"It is {alarm} !")
                msg.setIcon(QMessageBox.Question)
                msg.exec()                  
            else:
               ...

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
