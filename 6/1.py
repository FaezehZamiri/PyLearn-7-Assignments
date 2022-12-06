import random
from termcolor import colored
import time

game=[['_','_','_'],['_','_','_'],['_','_','_']]

def showGame():
    for i in range(3):
        for j in range(3):                
            print(game[i][j],end=' ')
        print()
def playerMove():
    while True:
        row=int(input('Enter Row : '))
        col=int(input('Enter Column : '))
        if 0<= row <=2 and 0<= col <=2 :
            if game[row][col]=='_':
                    game[row][col]=colored('X','red')
                    break
            else:
                print("Enter An Other Row or Column")
        else:
            print("Enter An Other Row or Column between 0-2")
    return row,col
def playerMoveTwo():
    while True:
        row=int(input('Enter Row : '))
        col=int(input('Enter Column : '))
        if 0<= row <=2 and 0<= col <=2 :
            if game[row][col]=='_':
                    game[row][col]='O'
                    break
            else:
                print("Enter An Other Row or Column")
        else:
            print("Enter An Other Row or Column between 0-2")
    return row,col
def computerMove():
    while True:
        r=random.randint(0,2)
        c=random.randint(0,2)
        if game[r][c]=='_':
            game[r][c]='O'
            break

def check(select):
    c=0
    for i in range(3):
        if game[i][:]==['O', 'O', 'O']: 
            if select==1:
                print("Computer Wins... \U0001f600")
                c=1
            elif select==2:
                print("Player 2 Wins... \U0001f600")
                c=1
        elif game[i][:]==[colored('X','red'), colored('X','red'), colored('X','red')]:
            if select==1:
                print("You Wins... \U0001f600")
                c=1
            elif select==2:
                print("Player 1 Wins... \U0001f600")
                c=1
    if (game[0][2]=='O' and game[1][1]=='O' and game[2][0]=='O') or (game[0][0]=='O' and game[1][1]=='O' and game[2][2]=='O') or (game[0][0]=='O' and game[1][0]=='O' and game[2][0]=='O') or (game[0][1]=='O' and game[1][1]=='O' and game[2][1]=='O') or (game[0][2]=='O' and game[1][2]=='O' and game[2][2]=='O'):
        if select==1:
            print("Computer Wins... \U0001f600")
            c=1
        elif select==2:
            print("Player 2 Wins... \U0001f600")
            c=1
    elif (game[0][2]==colored('X','red') and game[1][1]==colored('X','red') and game[2][0]==colored('X','red')) or (game[0][0]==colored('X','red') and game[1][1]==colored('X','red') and game[2][2]==colored('X','red')) or  (game[0][0]==colored('X','red') and game[1][0]==colored('X','red') and game[2][0]==colored('X','red')) or (game[0][1]==colored('X','red') and game[1][1]==colored('X','red') and game[2][1]==colored('X','red')) or (game[0][2]==colored('X','red') and game[1][2]==colored('X','red') and game[2][2]==colored('X','red')) :
        if select==1:
            print("You Wins... \U0001f600")
            c=1
        elif select==2:
            print("Player 1 Wins... \U0001f600")
            c=1
    return c
def stopGame(c):
    l=0
    for i in range(3):
        for j in range(3):
            if game[i][j]=='_':
                l=l+1
    if  c!=1  and  l<1:
        c=2
        print('You are Tie...')
    return c

select=int(input("select you want to play with : \n 1.computer \n 2.an other player :"))
showGame()
while True:
    start=time.time()
    if select==1:
        playerMove()
        computerMove()
    elif select==2:
        print("player 1")
        playerMove()
        showGame()
        print("player 2")
        playerMoveTwo()
    else:
        print("sth went wrong!")
        break
    showGame()
    c=check(select)
    c=stopGame(c)
    if c==1:
        end = time.time()
        break
    elif c==2:
        end = time.time()
        break
    else:
        continue
    
    

print(f"Runtime of the Game is {end - start}")       
