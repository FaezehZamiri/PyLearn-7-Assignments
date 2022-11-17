from random import randint

print("rock")
print("paper")
print("sci")

player1win=0
player2win=0

while player1win<3 and player2win<3:
    x=randint(1,3)
    if x==1:
        computerMove="rock"
    elif x==2:
        computerMove="paper"
    elif x==3:
        computerMove="sci"   

    player_1=input("player_1_move :").lower()
    player_2=computerMove

    print(f"player_2_move :{computerMove}")

    if player_1==player_2:
        print("you are tie...")
    elif player_1=="rock":
        if player_2=="paper":
            print("player_2 wins... ")
            player2win+=1
        elif player_2=="sci":
            print("player_1 wins... ") 
            player1win+=1
    elif player_1=="paper":
        if player_2=="rock":
            print("player_1 wins... ")
            player1win+=1
        elif player_2=="sci":
            print("player_2 wins... ")
            player2win+=1 
    elif player_1=="sci":
        if player_2=="paper":
            print("player_1 wins... ")
            player1win+=1
        elif player_2=="rock":
            print("player_2 wins... ")
            player2win+=1 
    else:
        print("sth went wrong , pls try again...")

if player1win==3:
    print("finally player_1 win \U0001f600")
elif player2win==3:
    print("finally player_2 win \U0001f600")
