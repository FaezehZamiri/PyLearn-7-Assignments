from Media import Media
from Film import Film
from Serial import Serial
from Clip import Clip
from Documentary import Documentary

Medias=[]
def load(filename):
    data=open(filename,'r')
    data=data.read()
    mediaList=data.split("\n")
    for i in range(len(mediaList)):
        mediasInfo=mediaList[i].split(",")
        myDict={'id':int(mediasInfo[0]),
                'name':mediasInfo[1],
                'director':mediasInfo[2],
                'IMDB':float(mediasInfo[3]),
                'url':mediasInfo[4],
                'duration':float(mediasInfo[5]),
                'casts':mediasInfo[6]}
        if len(mediasInfo)>7:
            myDict['parts']=int(mediasInfo[7])
        Medias.append(myDict)

def add():
    iD=int(input("Pls Enter ID : "))
    name=input("Pls Enter Name : ")
    director=input("Pls Enter Director : ")
    IMDB=float(input("Pls Enter IMDB : "))
    url=input("Pls Enter URL : ")
    duration=float(input("Pls Enter Duration : "))
    casts=input("Pls Enter Casts : ")
    Medias.append({'id':iD,'name':name,'director':director,'IMDB':IMDB,'url':url,'duration':duration,'casts':casts})
    if len(Medias[0])>7:
        Medias[len(Medias)]['parts']=int(input("Pls Enter Parts : "))
    print("Media Added Successfully!")

def show_edit_menu():
    print("1-Edit Name")
    print("2-Edit Director")
    print("3-Edit IMDB")
    print("4-Edit URL")
    print("5-Edit Duration")
    print("6-Edit Casts")
    print("7-End Edit")        
    if len(Medias[0])>7:
        print("8-Edit Parts")

def edit():
    id=int(input("Pls Enter Media Id :" ))
    for i in range(len(Medias)):
        if Medias[i]['id']==id:
            while True:
                show_edit_menu()
                edit=int(input("Pls Choose from Edit Menu : "))
                if edit==1:
                    Medias[i]['name']=input("Pls Enter New Name : ")
                    print("Media Edited Successfully!")
                elif edit==2:
                    Medias[i]['director']=input("Pls Enter New Director : ")
                    print("Media Edited Successfully!")
                elif edit==3:
                    Medias[i]['IMDB']=float(input("Pls Enter New IMDB : "))
                    print("Media Edited Successfully!")
                elif edit==4:
                    Medias[i]['url']=input("Pls Enter New URL : ")
                    print("Media Edited Successfully!")
                elif edit==5:
                    Medias[i]['duration']=float(input("Pls Enter New Duration : "))
                    print("Media Edited Successfully!")
                elif edit==6:
                    Medias[i]['casts']=input("Pls Enter New Casts : ")
                    print("Media Edited Successfully!")
                elif edit==7:
                    break
                elif edit==8:
                    Medias[i]['parts']=input("Pls Enter New Parts : ")
                    print("Media Edited Successfully!")
                else:
                    print("Value Error ,Try Again !")

def search():
    print("1-Search With Name Or Id ")
    print("2-Search With Duration ")
    choice=int(input("Which Method do You Want to Search : "))
    if choice==1:
        userKey=input("Pls Enter Media Id or Product Name : " )
        f=0
        for i in range(len(Medias)):
            if str(Medias[i]['id'])==userKey or (Medias[i]['name'].lower()==userKey.lower()) :
                print(Medias[i])
                f=1
        if f==0:   
            print("Media Not Found!")
    elif choice==2:
        print("Duration between A and B ")
        A=int(input("A : "))
        B=int(input("B : "))
        f=0
        for i in range(len(Medias)):
            if Medias[i]['duration']<=B and Medias[i]['duration']>=A:
                print(Medias[i])
                f=1
        if f==0:   
            print("Media Not Found!")      

    else:
        print('Try Again !')

def delete():
    iD=int(input("Pls Enter Media Id :" ))
    for i in range(len(Medias)):
        if Medias[i]['id']==iD:
            Medias.pop(i)
            print("Medias Removed Successfully!")
            break

def exitAndSave(filename):
    f=open(filename,'w')
    if len(Medias[0])>7:
        for i in range(len(Medias)):
            if i==len(Medias)-1:
                row=str(Medias[i]['id']) +','+Medias[i]['name']+','+Medias[i]['director']+','+str(Medias[i]['IMDB'])+','+Medias[i]['url']+','+str(Medias[i]['duration'])+','+Medias[i]['casts']+','+str(Medias[i]['parts'])
            else:
                row=str(Medias[i]['id']) +','+Medias[i]['name']+','+Medias[i]['director']+','+str(Medias[i]['IMDB'])+','+Medias[i]['url']+','+str(Medias[i]['duration'])+','+Medias[i]['casts']+','+str(Medias[i]['parts'])+'\n'
            f.write(row)
    else:
        for i in range(len(Medias)):
            if i==len(Medias)-1:
                row=str(Medias[i]['id']) +','+Medias[i]['name']+','+Medias[i]['director']+','+str(Medias[i]['IMDB'])+','+Medias[i]['url']+','+str(Medias[i]['duration'])+','+Medias[i]['casts']
            else:
                row=str(Medias[i]['id']) +','+Medias[i]['name']+','+Medias[i]['director']+','+str(Medias[i]['IMDB'])+','+Medias[i]['url']+','+str(Medias[i]['duration'])+','+Medias[i]['casts']+'\n'
            f.write(row)
    f.close()
    exit()

def showMenu(Categorize,filename):
    while True:
        print("1-Add Media")
        print("2-Edit Media")
        print("3-Delete Media")
        print("4-Search")
        print("5-Show List")
        print("6-Download")
        print("7-Exit")
        choice=int(input("Please Select A Number : "))
        if choice==1:
            add()
        elif choice==2:
            edit()
        elif choice==3:
            delete()
        elif choice==4:
            search()
        elif choice==5:
            if len(Medias[0])>7:
                print('id'+'\t'+'Name'+'\t\t'+'Director'+'\t'+'IMDB'+'\t'+'Duration'+'\t'+'Casts'+'\t'+'Parts')
                for i in range(len(Medias)):
                    media=Categorize(Medias[i]['id'],Medias[i]['name'],Medias[i]['director'],Medias[i]['IMDB'],Medias[i]['url'],Medias[i]['duration'],Medias[i]['casts'],Medias[i]['parts'])
                    media.showInfo()
            else:
                print('id'+'\t'+'Name'+'\t\t\t'+'Director'+'\t'+'IMDB'+'\t'+'Duration'+'\t'+'Casts')
                for i in range(len(Medias)):
                    media=Categorize(Medias[i]['id'],Medias[i]['name'],Medias[i]['director'],Medias[i]['IMDB'],Medias[i]['url'],Medias[i]['duration'],Medias[i]['casts'])
                    media.showInfo()
        elif choice==6:
            userKey=input("Pls Enter Media Id or Product Name : " )
            f=0
            for i in range(len(Medias)):
                if str(Medias[i]['id'])==userKey or (Medias[i]['name'].lower()==userKey.lower()) :
                    media=Categorize(Medias[i]['id'],Medias[i]['name'],Medias[i]['director'],Medias[i]['IMDB'],Medias[i]['url'],Medias[i]['duration'],Medias[i]['casts'])
                    media.download()
                    print(Medias[i]['url'])
                    f=1
            if f==0:   
                print("Media Not Found!")
        elif choice==7:
            exitAndSave(str(filename))
            break
        else:
            print("Try Again!")
   
while True:
    #showMainMenu()
    Media().showMainMenu()
    choice=int(input('Please Select A Categorize : '))

    if choice==1:
        load("films.txt")
        showMenu(Film,"films.txt")
    elif choice==2:
        load("clip.txt")
        showMenu(Clip,"clip.txt")
    elif choice==3:
        load("serial.txt")
        showMenu(Serial,"serial.txt")
    elif choice==4:
        load("documentary.txt")
        showMenu(Documentary,"documentary.txt")
    elif choice==5:
        break
    else:
        print("Try Again!")