from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_main_window import Ui_MainWindow
from database import Database
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.widgets = []
        self.db = Database()
        self.show_task()
        self.ui.pushButton.clicked.connect(self.new_task) 
        
    def show_task(self):
        for i in reversed(range(self.ui.GL_Tasks.count())): 
            self.ui.GL_Tasks.itemAt(i).widget().setParent(None)
        Tasks = self.db.get_task()
        Tasks = self.sort_task(Tasks)
        for i in range(len(Tasks)):
            new_ckechbox = QCheckBox()
            new_label = QLabel() 
            new_btn = QPushButton()
            #new_ckechbox.setText(Tasks[i][1])
            new_label.setText(Tasks[i][1])
            new_btn.setText("×")

            new_btn.setStyleSheet("height:20px;border:none;color:rgb(255, 0, 127);font-family:'Forte'; font-size:25pt;") 
            new_ckechbox.setStyleSheet("height:20px;border-radius:10px;font-family:'Forte'; font-size:20pt;") 

            if Tasks[i][4] == "Normal":
                new_label.setStyleSheet("color:rgb(199, 142, 255);font-family:'Forte'; font-size:15pt;") 
            else:
                new_label.setStyleSheet("color:rgb(255, 0, 127);font-family:'Forte'; font-size:15pt;") 

            self.ui.GL_Tasks.addWidget(new_ckechbox,i,0)
            self.ui.GL_Tasks.addWidget(new_label,i,1)
            self.ui.GL_Tasks.addWidget(new_btn,i,2)

            if Tasks[i][3] == 1:
                new_ckechbox.setChecked(True)

            self.widgets.append([new_ckechbox,new_label,new_btn])
            new_ckechbox.toggled.connect(partial(self.do_task, Tasks[i][1], new_ckechbox))
            new_btn.clicked.connect(partial(self.remove_task,Tasks[i][1],[new_ckechbox,new_label,new_btn]))
            new_label.mousePressEvent = partial(self.show_info,Tasks[i])

    def new_task(self):
        new_title = self.ui.lineEdit.text()
        new_description = self.ui.textEdit.toPlainText()
        new_priority = self.ui.comboBox.currentText()
        new_time = self.ui.dateTimeEdit.text()
        feedback = self.db.add_new_task(new_title,new_description,new_priority,new_time)
        if feedback == True:
            self.show_task()
            self.ui.lineEdit.setText("")
            self.ui.textEdit.setText("")
        else:
            msg = QMessageBox()
            msg.setText('Try Again!')
            msg.exec()

    def do_task(self, title,ckechbox,m):
        if ckechbox.isChecked():
            status = 1
        else:
            status = 0
        feedback = self.db.task_done(title, status)
        if feedback == True:
            self.show_task()
        else:
            msg_box = QMessageBox()
            msg_box.setText("Try Again!")
            msg_box.exec()
    
    def remove_task(self, title,Array):  
        feedback = self.db.remove_task(title)
        if feedback == True:
            for widget in Array:
                widget.deleteLater()
        else:
            msg_box = QMessageBox()
            msg_box.setText("Try Again")
            msg_box.exec()

    def sort_task(self, Tasks):
        done_task = []
        for task in Tasks:
            if task[3] == 1:
                Tasks.remove(task)
                done_task.append(task)

        sorted_tasks = Tasks + done_task
        return sorted_tasks
        
    def show_info(self,task,m):
        info = f"Title : {task[1]} \nDescription : {task[2]} \nPriority : {task[4]} \nTime : {task[5]} "
        msg_box = QMessageBox()
        msg_box.setText(info)
        msg_box.exec()

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()