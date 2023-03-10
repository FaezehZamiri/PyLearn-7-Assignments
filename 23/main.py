from PySide6.QtWidgets import *
from PySide6 import QtCore
from ui_main_window import Ui_MainWindow
from sudoku import Sudoku
from functools import partial
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lineEdits = [[None for i in range(9)]for j in range(9)]
        self.newGame()
        self.ui.actionNew_Game.triggered.connect(self.newGame)
        self.ui.actionOpen_File.triggered.connect(self.openFile)
        self.ui.actionSolve.triggered.connect(self.solveGame)

    def showGame(self):
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setStyleSheet("height:50px;font-family:'Forte'; font-size:25pt;")
                new_cell.setAlignment(QtCore.Qt.AlignCenter)
                new_cell.setReadOnly(False)
                if self.puzzle.board[i][j] == None:
                    new_cell.setText('')
                else:
                    new_cell.setText(str(self.puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.gridLayout.addWidget(new_cell,i,j)
                new_cell.textChanged.connect(partial(self.validation,i,j))
                self.lineEdits[i][j] = new_cell

    def newGame(self):    
        self.puzzle = Sudoku(3 , seed = random.randint(1,100)).difficulty(0.5)   
        self.showGame()

    def validation(self,i,j,text):
        if text not in ['1','2','3','4','5','6','7','8','9']:
            self.lineEdits[i][j].setText('')
        self.check(i,j,text)
        self.check_winner()
        if self.lineEdits[i][j].text() == '':
            self.lineEdits[i][j].setStyleSheet("background-color:white;height:50px;font-family:'Forte'; font-size:25pt;")
    
    def openFile(self):
        try:
            filename = QFileDialog.getOpenFileName(self,"Open File")
            data = open(str(filename[0]),'r') 
            data = data.read()
            rows = data.split('\n')
            columns = []
            board = [[None for i in range(9)]for j in range(9)]
            for row in rows:
                columns.append(row.split(' '))
            for i in range(9):
                for j in range(9):
                    board[i][j] = int(columns[i][j])
            self.puzzle = Sudoku(3, 3, board=board)
            self.showGame()
        except:
            msg = QMessageBox()
            msg.setText('Try Again!')
            msg.exec()

    def check(self,i,j,text):
        #ROW 
        for kk in range(9):
            for k in range(9):
                row = self.lineEdits[kk][k].text()
                if row == text and k != j and i == kk:
                    self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")
        #COl
        for ll in range(9):
            for l in range(9):
                col = self.lineEdits[l][ll].text()
                if col == text and i != l and j == ll:
                    self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")

    
        #Cell 3*3
        if (i in [0,1,2]) and (j in [0,1,2]):
            print('cell1')
            for hh in range(3):
                for h in range(3):
                    cell_1 = self.lineEdits[hh][h].text()
                    if cell_1 == text and hh != i and h != j:
                        self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")

        if (i in [0,1,2]) and (j in [3,4,5]):
            print('cell2')
            for hh in range(3):
                for h in range(3,6):
                    cell_2 = self.lineEdits[hh][h].text()
                    if cell_2 == text and hh != i and h != j:
                        self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")

        if (i in [0,1,2]) and (j in [6,7,8]):
            print('cell3')
            for hh in range(3):
                for h in range(6,9):
                    cell_3 = self.lineEdits[hh][h].text()
                    if cell_3 == text and hh != i and h != j:
                        self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")
        
        if (i in [3,4,5]) and (j in [0,1,2]):
            print('cell4')
            for hh in range(3,6):
                for h in range(0,3):
                    cell_4 = self.lineEdits[hh][h].text()
                    if cell_4 == text and hh != i and h != j:
                        self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")

        if (i in [3,4,5]) and (j in [3,4,5]):
            print('cell5')
            for hh in range(3,6):
                for h in range(3,6):
                    cell_5 = self.lineEdits[hh][h].text()
                    if cell_5 == text and hh != i and h != j:
                        self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")

        if (i in [3,4,5]) and (j in [6,7,8]):
            print('cell6')
            for hh in range(3,6):
                for h in range(6,9):
                    cell_6 = self.lineEdits[hh][h].text()
                    if cell_6 == text and hh != i and h != j:
                        self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")

        if (i in [6,7,8]) and (j in [0,1,2]):
            print('cell7')
            for hh in range(6,9):
                for h in range(0,3):
                    cell_7 = self.lineEdits[hh][h].text()
                    if cell_7 == text and hh != i and h != j:
                        self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")

        if (i in [6,7,8]) and (j in [3,4,5]):
            print('cell8')
            for hh in range(6,9):
                for h in range(3,6):
                    cell_8 = self.lineEdits[hh][h].text()
                    if cell_8 == text and hh != i and h != j:
                        self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")

        if (i in [6,7,8]) and (j in [6,7,8]):
            print('cell9')
            for hh in range(6,9):
                for h in range(6,9):
                    cell_9 = self.lineEdits[hh][h].text()
                    if cell_9 == text and hh != i and h != j:
                        self.lineEdits[i][j].setStyleSheet("background-color:#ff5d60;height:50px;height:50px;font-family:'Forte'; font-size:25pt;color:#fff")

    def check_winner(self):
        solve = self.puzzle.solve()
        print(solve) 
        count = 0
        for ii in range(9):
            for jj in range(9):
                if str(solve.board[ii][jj]) == self.lineEdits[ii][jj].text():
                    count = count + 1
        if count == 81:
            msg = QMessageBox()
            msg.setText('You Win!')
            msg.exec()

    def solveGame(self):
        solve = self.puzzle.solve()
        self.puzzle = Sudoku(3, 3, board=solve.board)
        self.showGame()

        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()