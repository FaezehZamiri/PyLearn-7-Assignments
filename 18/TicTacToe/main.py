from PySide6.QtWidgets import QApplication , QMessageBox
from PySide6.QtUiTools import QUiLoader
from functools import partial
import sys
import random

my_app = QApplication(sys.argv)
loader = QUiLoader()
my_window = loader.load("TicTacToe/mainwindow.ui")
my_window.show()

player = 1
select = "User"
x_win = 0
o_win = 0
tie = 0

cell =[[my_window.btn_1,my_window.btn_2,my_window.btn_3],
       [my_window.btn_4,my_window.btn_5,my_window.btn_6],
       [my_window.btn_7,my_window.btn_8,my_window.btn_9]]

def select_player(n):
    global select
    if n == 0:
        select = "User"
    elif n == 1:
        select = "CPU"
   
def play(btn):
    global player
    if player == 1:
        if btn.text()=="":
            btn.setText("X")
            btn.setStyleSheet("color:#ff5500;background-color:rgb(0, 0, 67);border-radius:15px;box-shadow:20px 20px #888888;") 
            if select == "CPU":
                cpu_play()
            else:
                player = 2
    elif player == 2 and select == "User":
        if btn.text()=="":
            btn.setText("O")
            btn.setStyleSheet("color:#ffffff;background-color:rgb(0, 0, 67);border-radius:15px;box-shadow:20px 20px #888888;")
            player = 1
    check()

def cpu_play():
    global player
    while True:
        r=random.randint(0,2)
        c=random.randint(0,2)       
        if cell[r][c].text() == '':
            cell[r][c].setText('O')
            cell[r][c].setStyleSheet("color:#ffffff;background-color:rgb(0, 0, 67);border-radius:15px;box-shadow:20px 20px #888888;")
            player = 1
            break

def check():
    global x_win , o_win , tie ,player 
    if (cell[2][0].text()=='X' and cell[2][1].text()=='X' and cell[2][2].text()=='X') or (cell[1][0].text()=='X' and cell[1][1].text()=='X' and cell[1][2].text()=='X') or (cell[0][0].text()=='X' and cell[0][1].text()=='X' and cell[0][2].text()=='X') or (cell[0][2].text()=='X' and cell[1][1].text()=='X' and cell[2][0].text()=='X') or (cell[0][0].text()=='X' and cell[1][1].text()=='X' and cell[2][2].text()=='X') or (cell[0][0].text()=='X' and cell[1][0].text()=='X' and cell[2][0].text()=='X') or (cell[0][1].text()=='X' and cell[1][1].text()=='X' and cell[2][1].text()=='X') or (cell[0][2].text()=='X' and cell[1][2].text()=='X' and cell[2][2].text()=='X'):
        x_win += 1
        player = 1
        msg = QMessageBox(text = "You Win!")
        msg.exec()
        start_again()
    elif (cell[2][0].text()=='O' and cell[2][1].text()=='O' and cell[2][2].text()=='O') or (cell[1][0].text()=='O' and cell[1][1].text()=='O' and cell[1][2].text()=='O') or (cell[0][0].text()=='O' and cell[0][1].text()=='O' and cell[0][2].text()=='O') or (cell[0][2].text()=='O' and cell[1][1].text()=='O' and cell[2][0].text()=='O') or (cell[0][0].text()=='O' and cell[1][1].text()=='O' and cell[2][2].text()=='O') or (cell[0][0].text()=='O' and cell[1][0].text()=='O' and cell[2][0].text()=='O') or (cell[0][1].text()=='O' and cell[1][1].text()=='O' and cell[2][1].text()=='O') or (cell[0][2].text()=='O' and cell[1][2].text()=='O' and cell[2][2].text()=='O'):
        o_win += 1
        player = 1
        msg = QMessageBox(text = "Player 2 Wins!")
        msg.exec()
        start_again() 
    else:
        k=0  
        for i in range(3):
            for j in range(3):
                if cell[i][j].text()!="":
                    k += 1
        if k == 9 : 
            tie += 1    
            player = 1
            msg = QMessageBox(text = "You are Tie")
            msg.exec()
            start_again()

    my_window.btn_xwin.setText(str(x_win))
    my_window.btn_owin.setText(str(o_win))
    my_window.btn_tie.setText(str(tie))

def start_again():
    for i in range(3):
        for j in range(3):
            cell[i][j].setText('')


for i in range(3):
    for j in range(3):
        cell[i][j].clicked.connect(partial(play,cell[i][j]))


my_window.btn_startagain.clicked.connect(start_again)
my_window.Player.clicked.connect(partial(select_player,0))
my_window.CPU.clicked.connect(partial(select_player,1))

my_app.exec() 