import instaloader
import getpass
from instaloader.exceptions import TwoFactorAuthRequiredException

file = open("followers.txt","r")
old_followers=[]
for line in file:
    old_followers.append(line)

file.close()

loader = instaloader.Instaloader()
user=input("Enter Username :")
password=getpass.getpass("Enter Password :")

try:
    login = loader.login(user,password)
except TwoFactorAuthRequiredException:
    code = int(input("Enter Code : "))
    loader.two_factor_login(code)

profile = instaloader.Profile.from_username(loader.context,user)

new_followers =[]
for follower in profile.get_followers():
    new_followers.append(follower)

#for old_follower in old_followers:
#    if old_follower not in new_followers:
#       print(old_follower)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

file = open("followers.txt","w")
for follower in new_followers:
    file.write(follower + "\n")

file.close()

