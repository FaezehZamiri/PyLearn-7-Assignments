import telebot
import random
import gtts
import qrcode
import numpy as np
from telebot import types


bot = telebot.TeleBot("2037137248:AAECpNJdM3DU6IQgeGYiMK2opl6jnt9TGfg", parse_mode=None) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"Welcome to My Bot {message.from_user.username}")


@bot.message_handler(commands=['game'],func=lambda m: True)
def input(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add('New Game!')
    msg = bot.send_message(message.chat.id,"Please Enter a Integer Number Between 10 , 40: ",reply_markup=markup) 
    PCNumber = random.randint(10,40)
    print(PCNumber)
    bot.register_next_step_handler(msg, game,PCNumber)
    
def game(message,PCNumber): 

    print(message.text)
    YourNumber = message.text
    if  YourNumber=='/game' or YourNumber=='New Game!':
        bot.send_message(message.chat.id, 'New Game!')
        input(message)
        return
    elif not YourNumber.isdigit():
        msg = bot.reply_to(message, 'You Should Enter a Valid Integer Number.')
        bot.register_next_step_handler(msg, game,PCNumber)
        return
    YourNumber=int(message.text)
    bot.register_next_step_handler(message, game,PCNumber)

    if YourNumber == PCNumber:
        bot.send_message(message.chat.id,'You Win!')
        bot.stop_bot()# check please
        return           
    elif YourNumber > PCNumber:
        bot.send_message(message.chat.id,'Go Down!')
    else:
        bot.send_message(message.chat.id,'Go Up!')



@bot.message_handler(commands=['age'],func=lambda m: True)
def inputage(message):
    msg = bot.send_message(message.chat.id,'Please Enter Your Birth Date :\nFormat : yyyy/MM/dd')
    bot.register_next_step_handler(msg, age)

def age(message):
    try:
        Date = message.text
        Date = Date.split('/')
        print(Date)

        y = 1401 - int(Date[0])
        m = 9 - int(Date[1])
        d = 25 - int(Date[2])
        if m <=0:
            m = m + 12
            y = y - 1 
        if d <=0:
            d = d + 30
        
        age = f"Now your exact age is {y} years, {m} month, {d} days old"
        bot.send_message(message.chat.id,age)
    except ValueError:
        bot.send_message(message.chat.id,'Please Enter Valid Format!')
        inputage(message)
        return


@bot.message_handler(commands=['voice'],func=lambda m: True)
def inputsentence(message):
    msg = bot.send_message(message.chat.id,'Please Enter a English Sentence : ')
    bot.register_next_step_handler(msg, voice)

def voice(message):
    sentence = message.text
    voice = gtts.gTTS(sentence,lang = 'en' ,slow=False)
    voice.save('voice.mp3')
    voices = open('voice.mp3', 'rb')
    bot.send_voice(message.chat.id, voices)


@bot.message_handler(commands=['qrcode'],func=lambda m: True)
def inputstring(message):
    msg = bot.send_message(message.chat.id,'Please Enter a String : ')
    bot.register_next_step_handler(msg, makeqrcode)

def makeqrcode(message):
    string = message.text
    img = qrcode.make(string)
    img.save('qrcode.png')
    img = open('qrcode.png', 'rb')
    bot.send_photo(message.chat.id, img)


@bot.message_handler(commands=['max'],func=lambda m: True)
def inputmax(message):
    msg = bot.send_message(message.chat.id,'Please Enter an Array :\nFormat : 1,2,3,4 ')
    bot.register_next_step_handler(msg, max)

def max(message):
    try:
        array = message.text
        array = array.split(',')
        print(array)
        lists=[]
        for element in array:
            lists.append(float(element))
        print(np.max(lists))
        bot.send_message(message.chat.id,f'The Maximun is {np.max(lists)}')
    except:
        bot.send_message(message.chat.id,'Please Enter Valid Format!')
        inputmax(message)
        return


@bot.message_handler(commands=['argmax'],func=lambda m: True)
def inputargmax(message):
    msg = bot.send_message(message.chat.id,'Please Enter an Array :\nFormat : 1,2,3,4 ')
    bot.register_next_step_handler(msg, argmax)

def argmax(message):
    try:
        array = message.text
        array = array.split(',')
        print(array)
        lists=[]
        for element in array:
            lists.append(float(element))
        print(lists.index(np.max(lists)))
        bot.send_message(message.chat.id,f'The Index of Maximun is {lists.index(np.max(lists))}')
    except:
        bot.send_message(message.chat.id,'Please Enter Valid Format!')
        inputargmax(message)
        return


@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id,"""\
command /start
Print welcome with user name
command /game
Run the number guessing game. The user guesses a number and the bot guides (go up, go down, you win)
command /age
Get the date of birth in Hijri and calculate the age.
command /voice
Receive a sentence in English from the user and send it as voice.
command /max
Receive an array as 14,7,78,15,8,19,20 from the user and print the largest value.
command /argmax
Receive an array as 14,7,78,15,8,19,20 from the user and print the index of the largest value.
command /qrcode
Receive a string from the user and generate its qrcode.
    """)



bot.infinity_polling()