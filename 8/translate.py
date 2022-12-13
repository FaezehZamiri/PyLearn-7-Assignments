dicts=[]
def showMenu():
    print("1-Add New Word")
    print("2-Translation English To Persian")
    print("3-Translation Persian To English")
    print("4-Show Words")
    print("5-Exit")

def load():
    f=open("words.txt",'r')
    f=f.read()
    words=f.split("\n")
    lists=[]
    for i in range(len(words)):
            lists.append(words[i].split(','))
    for i in range(len(lists)):
        Dict={}
        Dict["English"]=lists[i][0]
        Dict["Persian"]=lists[i][1]
        dicts.append(Dict)

def add():
    while True:
        english=input('Please Enter English of Word : ')
        persian=input('Please Enter Persian of Word : ')
        Dict={}
        Dict["English"]=english
        Dict["Persian"]=persian
        dicts.append(Dict)
        print("Word Added Successfully!")
        q=input("Do Want to Add another Word? (Y/N)").lower()
        if q=='n':
            break

def showWords():
    print(dicts)

def e2p():
    while True:
        sen=input("Please Enter Yor Sentence : ").lower()
        words=sen.split(" ")
        translate=[]
        for i in range(len(words)):
            for j in range(len(dicts)):
                if words[i]==dicts[j]['English']:
                    translate.append(dicts[j]['Persian'])
     
        final=" ".join(translate)
        print(final)
        q=input("Do Want to Translate another Sentence? (Y/N)").lower()
        if q=='n':
            break

def p2e():
    while True:
        sen=input("Please Enter Yor Sentence : ").lower()
        words=sen.split(" ")
        translate=[]
        for i in range(len(words)):
            for j in range(len(dicts)):
                if words[i]==dicts[j]['Persian']:
                    translate.append(dicts[j]['English'])
        
        final=" ".join(translate)
        print(final)
        q=input("Do Want to Translate another Sentence? (Y/N)").lower()
        if q=='n':
            break

def saveAndExit():
    file=open('words.txt','w')
    file.flush()
    for i in range(len(dicts)):
        if i==len(dicts)-1:
            row=dicts[i]['English'] +','+ dicts[i]['Persian']
        else:
            row=dicts[i]['English'] +','+ dicts[i]['Persian']+'\n'
        file.write(row)
    file.close()
    exit()
while True:
    load()
    showMenu()
    choice=int(input("Please Select a Number : "))

    if choice==1:
        add()
    elif choice==2:
        e2p()
    elif choice==3:
        p2e()
    elif choice==4:
        showWords()
    elif choice==5:
        saveAndExit()
        break
    else:
        print("Try Again!")
