import random


hands = ["✋","🤚"]

count_user = 0
count_computer1 = 0
count_computer2 = 0

for i in range(5):
    print("1.",hands[0],"2.",hands[1])
    User_Choice = int(input("Please Choice One of Them and Enter Number of It :"))

    User = hands[User_Choice-1]
    Computer1 = random.choice(hands)
    Computer2 = random.choice(hands)
    if Computer1 == Computer2 and Computer1 != User:
        print("User : ",User)
        print("Computer1 :",Computer1)
        print("Computer2 :",Computer2)
        print("User Win!")
        count_user += 1
    elif User == Computer2 and Computer1 != User:
        print("User : ",User)
        print("Computer1 :",Computer1)
        print("Computer2 :",Computer2)
        print("Computer1 Win!")
        count_computer1 += 1
    elif User == Computer1 and Computer2 != User:
        print("User : ",User)
        print("Computer1 :",Computer1)
        print("Computer2 :",Computer2)
        print("Computer2 Win!")
        count_computer2 += 1
    else:
        print("User : ",User)
        print("Computer1 :",Computer1)
        print("Computer2 :",Computer2)
        print("Try Again!")

count = [count_user,count_computer1,count_computer2]
if max(count) == count_user :
    print("User Win!")
elif max(count) == count_computer1 :
    print("Computer 1 Win!")
elif max(count) == count_computer2 :
    print("Computer 2 Win!")
else:
    print("No One Win!")
