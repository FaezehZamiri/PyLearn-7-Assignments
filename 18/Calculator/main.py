from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial
import math

my_app = QApplication([])
loader = QUiLoader()
my_window = loader.load('Calculator/mainwindow.ui')
my_window.show()

def number(x):
    t = my_window.lineEdit.text()
    my_window.lineEdit.setText(t + str(x))

def number_10():
    t = my_window.lineEdit.text()
    if len(t.split('.'))<2:
        my_window.lineEdit.setText(t + '.')    

my_window.btn_0.clicked.connect(partial(number,0))
my_window.btn_1.clicked.connect(partial(number,1))
my_window.btn_2.clicked.connect(partial(number,2))
my_window.btn_3.clicked.connect(partial(number,3))
my_window.btn_4.clicked.connect(partial(number,4))
my_window.btn_5.clicked.connect(partial(number,5))
my_window.btn_6.clicked.connect(partial(number,6))
my_window.btn_7.clicked.connect(partial(number,7))
my_window.btn_8.clicked.connect(partial(number,8))
my_window.btn_9.clicked.connect(partial(number,9))
my_window.btn_10.clicked.connect(number_10)

def ac():
    my_window.lineEdit.setText("")

def sum():
    global a , operator
    a = float(my_window.lineEdit.text())
    operator = '+'
    my_window.lineEdit.setText("")

def sub():
    global a , operator
    a = float(my_window.lineEdit.text())
    operator = '-'
    my_window.lineEdit.setText("")

def mul():
    global a , operator
    a = float(my_window.lineEdit.text())
    operator = '*'
    my_window.lineEdit.setText("")

def dev():
    global a , operator
    a = float(my_window.lineEdit.text())
    operator = '/'
    my_window.lineEdit.setText("")

def pre():
    a = float(my_window.lineEdit.text())
    c = a/100
    my_window.lineEdit.setText(str(c))

def negpos():
    a = float(my_window.lineEdit.text())
    c = -1*a
    my_window.lineEdit.setText(str(c))

def sqrt():
    a = float(my_window.lineEdit.text())
    c = math.sqrt(a)
    my_window.lineEdit.setText(str(c))

def sin():
    a = float(my_window.lineEdit.text())
    c = math.sin(a)
    my_window.lineEdit.setText(str(c))

def cos():
    a = float(my_window.lineEdit.text())
    c = math.cos(a)
    my_window.lineEdit.setText(str(c))

def tan():
    a = float(my_window.lineEdit.text())
    if math.cos(a)!= 0 :
        c = math.sin(a)/math.cos(a)
    else:
        c = 'Inf'
    my_window.lineEdit.setText(str(c))

def cot():
    a = float(my_window.lineEdit.text())
    if math.sin(a)!= 0 :
        c = math.cos(a)/math.sin(a)
    else:
        c = 'Inf'
    my_window.lineEdit.setText(str(c))

def log():
    a = float(my_window.lineEdit.text())
    if a > 0 :
        c = math.log(a,10)
    else:
        c = 'Invalid Input'
    my_window.lineEdit.setText(str(c))

def ln():
    a = float(my_window.lineEdit.text())
    if a > 0 :
        c = math.log(a)
    else:
        c = 'Invalid Input'
    my_window.lineEdit.setText(str(c))

def result():
    try :
        b = float(my_window.lineEdit.text())
        if operator == '+':
            c = a + b
        if operator == '-':
            c = a - b
        if operator == '*':
            c = a * b
        if operator == '/':
            if b != 0:
                c = a / b
            else:
                c = "Can NOT divide by Zero"
        my_window.lineEdit.setText(str(c))
    except ValueError:
        my_window.lineEdit.setText("Invalid Input")

my_window.btn_sum.clicked.connect(sum)
my_window.btn_sub.clicked.connect(sub)
my_window.btn_mul.clicked.connect(mul)
my_window.btn_dev.clicked.connect(dev)
my_window.btn_pre.clicked.connect(pre)
my_window.btn_negpos.clicked.connect(negpos)
my_window.btn_sqrt.clicked.connect(sqrt)
my_window.btn_sin.clicked.connect(sin)
my_window.btn_cos.clicked.connect(cos)
my_window.btn_tan.clicked.connect(tan)
my_window.btn_cot.clicked.connect(cot)
my_window.btn_log.clicked.connect(log)
my_window.btn_ln.clicked.connect(ln)
my_window.btn_equal.clicked.connect(result)
my_window.btn_ac.clicked.connect(ac)

my_app.exec()