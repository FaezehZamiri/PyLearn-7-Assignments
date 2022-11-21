import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste']

print("You can guess from list :")
print(words)
print("You Have 6 Choice")

word = random.choice(words) 
joon = 6
user_character =''
correct = []
wrong = []
count = 0

while joon > 0:
    print('Correct Choice :')
    for i in range(len(word)):
        if word[i] in correct:
            print(word[i],end=" ")
        else:
            print("-",end=" ")
    print()

    print('Wrorg Choice :')
    for letter in wrong:
            print(letter,end=" ")     
 
    print()
    
    user_character = input("Enter Character : ") 
    user_character=user_character.lower()

    if len(user_character)==1:
        if user_character in correct :
            continue

        if user_character in word:
            for letter in word:
                if user_character ==letter:
                    count = count+1
                    correct.append(user_character)
            print('##################')
            print('👍✅')
            
        else:
            joon = joon - 1
            wrong.append(user_character)
            print('##################')
            print('👎❌')
            

        if  len(correct)==len(word):
            for i in range(len(word)):
                print(word[i],end=" ")
            print("\nYou Win ... \U0001f600")
            break
        if joon==0:
            print("Game Over ... \U0001f620")
            break
    else:
        print('##################')
        print('You Should Enter Just ONE Character!')
                

