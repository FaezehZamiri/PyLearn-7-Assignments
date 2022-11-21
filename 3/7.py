Sen = input("Please Enter Your Sentence : ")
n=1
for letter in Sen.rstrip():
    if letter == ' ':
        n=n+1

print(f"Your Sentence Has {n} Words")