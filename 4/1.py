import qrcode

user_name = input("Please Enter Your Name : ")
user_num = input("Please Enter Your Number : ")

users = "Name : "+ user_name + '\n' + "Phone Number : "+user_num
print(users)
img = qrcode.make(users)
img.save("user.png")