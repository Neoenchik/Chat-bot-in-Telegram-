import telebot;
import requests
from telebot import types
from bs4 import BeautifulSoup
import xlwt
import xlrd
from xlutils.copy import copy
import datetime
import math
from threading import Thread
import time

bot=telebot.TeleBot("5400490995:AAGbLQDrKpNMRvhB0bXf4B4U1Js3a9PmuaY")
site = "https://krisha.kz/arenda/kvartiry/?"
time1=int(datetime.datetime.today().strftime("%M"))
#soup = BeautifulSoup(response.text,'lxml')
#print(response.status_code)

mes2 = "Для начала выберите какой комнатности будет квартира:"
b=[False,False,False,False,False]
keyboard=None
keybutton=[]


def KeyB():
    global keyboard
    keyboard = types.InlineKeyboardMarkup()
    for i in range(0,len(keybutton)):
        keyboard.add(keybutton[i])

def rem(k):
    global keybutton
    for i in range(0,len(keybutton)):
        if keybutton[i].callback_data==k:
            print(i)
            keybutton.pop(i)
            break

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global keyboard
    global mes2
    global site
    global keybutton
    global b
    if call.data == "1r":
        if b[0]==False:
            keybutton[0].text="✅1-комн."
            site=site+"das[live.rooms][]=1&"
            b[0]=True
        else:
            keybutton[0].text="❌1-комн."
            site.replace("das[live.rooms][]=1&","")
            b[0]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = mes2, reply_markup = keyboard)
    if call.data == "2r":
        if b[1]==False:
            keybutton[1].text="✅2-комн."
            site=site+"das[live.rooms][]=2&"
            b[1]=True
        else:
            keybutton[1].text="❌2-комн."
            site.replace("das[live.rooms][]=2&","")
            b[1]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = mes2, reply_markup = keyboard)
    if call.data == "3r":
        if b[2]==False:
            keybutton[2].text="✅3-комн."
            site=site+"das[live.rooms][]=3&"
            b[2]=True
        else:
            keybutton[2].text="❌3-комн."
            site.replace("das[live.rooms][]=3&","")
            b[2]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = mes2, reply_markup = keyboard)
    if call.data == "4r":
        if b[3]==False:
            keybutton[3].text="✅4-комн."
            site=site+"das[live.rooms][]=4&"
            b[3]=True
        else:
            keybutton[3].text="❌4-комн."
            site.replace("das[live.rooms][]=4&","")
            b[3]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = mes2, reply_markup = keyboard)
    if call.data == "5r":
        if b[4]==False:
            keybutton[4].text="✅5+ комн."
            site=site+"das[live.rooms][]=5.100&"
            b[4]=True
        else:
            keybutton[4].text="❌5+ комн."
            site.replace("das[live.rooms][]=5.100&","")
            b[4]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = mes2, reply_markup = keyboard)
    if call.data == "c1":
        mes="Вы выбрали количество комнат"
        if b[0]==b[1] and b[1]==b[2] and b[2]==False and b[2]==b[3] and b[3]==b[4]:
            mes="Выбран любое количество комнат"
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id, text = mes)
        b=[False,False,False]
        term(call)
    if call.data == "hour":
        if b[0]==False:
            keybutton[0].text="✅По часам"
            site=site+"das[rent.period]=4&"
            b[0]=True
        else:
            keybutton[0].text="❌По часам"
            site.replace("das[rent.period]=4&","")
            b[0]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите на какой срок арендовать квартиру:", reply_markup = keyboard)
    if call.data == "days":
        if b[1]==False:
            keybutton[1].text="✅Посуточно"
            site=site+"das[rent.period]=1&"
            b[1]=True
        else:
            keybutton[1].text="❌Посуточно"
            site.replace("das[rent.period]=1&","")
            b[1]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите на какой срок арендовать квартиру:", reply_markup = keyboard)
    if call.data == "long":
        if b[2]==False:
            keybutton[2].text="✅На длительный срок"
            site=site+"das[rent.period]=2&"
            b[2]=True
        else:
            keybutton[2].text="❌На длительный срок"
            site.replace("das[rent.period]=2&","")
            b[2]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите на какой срок арендовать квартиру:", reply_markup = keyboard)
    if call.data == "c2":
        mes="Вы выбрали сроки аренды"
        if b[0]==b[1] and b[1]==b[2] and b[2]==False:
            mes="Выбрано на любой срок"
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id, text = mes)
        b=[False,False,False,False]
        type_home(call)
    if call.data == "brick":
        if b[0]==False:
            keybutton[0].text="✅Кирпичный"
            site=site+"das[flat.building]=1&"
            b[0]=True
        else:
            keybutton[0].text="❌Кирпичный"
            site.replace("das[flat.building]=1&","")
            b[0]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип дома:", reply_markup = keyboard)
    if call.data == "panel":
        if b[1]==False:
            keybutton[1].text="✅Панельный"
            site=site+"das[flat.building]=2&"
            b[1]=True
        else:
            keybutton[1].text="❌Панельный"
            site.replace("das[flat.building]=2&","")
            b[1]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип дома:", reply_markup = keyboard)
    if call.data == "monolith":
        if b[2]==False:
            keybutton[2].text="✅Монолитный"
            site=site+"das[flat.building]=3&"
            b[2]=True
        else:
            keybutton[2].text="❌Монолитный"
            site.replace("das[flat.building]=3&","")
            b[2]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип дома:", reply_markup = keyboard)
    if call.data == "other":
        if b[3]==False:
            keybutton[3].text="✅Иное"
            site=site+"das[flat.building]=0&"
            b[3]=True
        else:
            keybutton[3].text="❌Иное"
            site.replace("das[flat.building]=0&","")
            b[3]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип дома:", reply_markup = keyboard)
    if call.data == "c3":
        mes="Вы выбрали тип дома"
        if b[0]==b[1] and b[1]==b[2] and b[2]==False and b[2]==b[3]:
            mes="Выбран любой тип дома"
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id, text = mes)
        b=[False,False,False]
        furniture(call)
    if call.data == "full":
        if b[0]==False:
            keybutton[0].text="✅Полностью"
            site=site+"das[live.furniture]=1&"
            b[0]=True
        else:
            keybutton[0].text="❌Полностью"
            site.replace("das[live.furniture]=1&","")
            b[0]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите мебелирование квартиры:", reply_markup = keyboard)
    if call.data == "partly":
        if b[1]==False:
            keybutton[1].text="✅Частично"
            site=site+"das[live.furniture]=2&"
            b[1]=True
        else:
            keybutton[1].text="❌Частично"
            site.replace("das[live.furniture]=2&","")
            b[1]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите мебелирование квартиры:", reply_markup = keyboard)
    if call.data == "nothing":
        if b[2]==False:
            keybutton[2].text="✅Без мебели"
            site=site+"das[live.furniture]=3&"
            b[2]=True
        else:
            keybutton[2].text="❌Без мебели"
            site.replace("das[live.furniture]=3&","")
            b[2]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите мебелирование квартиры:", reply_markup = keyboard)
    if call.data == "c4":
        mes="Мебелирование выбрано"
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id, text = mes)
        b=[False,False,False,False]
        ethernet(call)
    if call.data == "ADSL":
        if b[0]==False:
            keybutton[0].text="✅ADSL"
            site=site+"das[inet.type][]=1&"
            b[0]=True
        else:
            keybutton[0].text="❌ADSL"
            site.replace("das[inet.type][]=1&","")
            b[0]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип Интернета в квартире:", reply_markup = keyboard)
    if call.data == "TV":
        if b[1]==False:
            keybutton[1].text="✅Через TV кабель"
            site=site+"das[inet.type][]=2&"
            b[1]=True
        else:
            keybutton[1].text="❌Через TV кабель"
            site.replace("das[inet.type][]=2&","")
            b[1]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип Интернета в квартире:", reply_markup = keyboard)
    if call.data == "wired":
        if b[2]==False:
            keybutton[2].text="✅проводной"
            site=site+"das[inet.type][]=3&"
            b[2]=True
        else:
            keybutton[2].text="❌проводной"
            site.replace("das[inet.type][]=3&","")
            b[2]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип Интернета в квартире:", reply_markup = keyboard)
    if call.data == "optics":
        if b[3]==False:
            keybutton[3].text="✅оптика"
            site=site+"das[inet.type][]=4&"
            b[3]=True
        else:
            keybutton[3].text="❌оптика"
            site.replace("das[inet.type][]=4&","")
            b[3]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип Интернета в квартире:", reply_markup = keyboard)
    if call.data == "c5":
        mes="Вы выбрали тип интернета в квартире"
        if b[0]==b[1] and b[1]==b[2] and b[2]==False and b[2]==b[3]:
            mes="Выбрано любой тип"
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id, text = mes)
        b=[False,False,False,False]
        bathroom(call)
    if call.data == "separate":
        if b[0]==False:
            keybutton[0].text="✅Раздельный"
            site=site+"das[flat.toilet]=1&"
            b[0]=True
        else:
            keybutton[0].text="❌Раздельный"
            site.replace("das[flat.toilet]=1&","")
            b[0]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип санузла в квартире:", reply_markup = keyboard)
    if call.data == "combined":
        if b[1]==False:
            keybutton[1].text="✅Совмещенный"
            site=site+"das[flat.toilet]=2&"
            b[1]=True
        else:
            keybutton[1].text="❌Совмещенный"
            site.replace("das[flat.toilet]=2&","")
            b[1]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип санузла в квартире:", reply_markup = keyboard)
    if call.data == "two":
        if b[2]==False:
            keybutton[2].text="✅2 с/у и более"
            site=site+"das[flat.toilet]=3&"
            b[2]=True
        else:
            keybutton[2].text="❌2 с/у и более"
            site.replace("das[flat.toilet]=3&","")
            b[2]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип санузла в квартире:", reply_markup = keyboard)
    if call.data == "no":
        if b[3]==False:
            keybutton[3].text="✅Нет"
            site=site+"das[flat.toilet]=4&"
            b[3]=True
        else:
            keybutton[3].text="❌Нет"
            site.replace("das[flat.toilet]=4&","")
            b[3]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите тип санузла в квартире:", reply_markup = keyboard)
    if call.data == "c6":
        mes="Вы выбрали тип санузла в квартире"
        if b[0]==b[1] and b[1]==b[2] and b[2]==False and b[2]==b[3]:
            mes="Выбран любой тип санузла"
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id, text = mes)
        b=[False,False,False,False,False]
        condition(call)
    if call.data == "good":
        if b[0]==False:
            keybutton[0].text="✅Хорошее"
            site=site+"das[flat.toilet]=1&"
            b[0]=True
        else:
            keybutton[0].text="❌Хорошее"
            site.replace("das[flat.toilet]=1&","")
            b[0]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите состояние квартиры:", reply_markup = keyboard)
    if call.data == "average":
        if b[1]==False:
            keybutton[1].text="✅Среднее"
            site=site+"das[flat.toilet]=2&"
            b[1]=True
        else:
            keybutton[1].text="❌Среднее"
            site.replace("das[flat.toilet]=2&","")
            b[1]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите состояние квартиры:", reply_markup = keyboard)
    if call.data == "repair":
        if b[2]==False:
            keybutton[2].text="✅Требует ремонта"
            site=site+"das[flat.toilet]=3&"
            b[2]=True
        else:
            keybutton[2].text="❌Требует ремонта"
            site.replace("das[flat.toilet]=3&","")
            b[2]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите состояние квартиры:", reply_markup = keyboard)
    if call.data == "free_layout":
        if b[3]==False:
            keybutton[3].text="✅Свободная планировка"
            site=site+"das[flat.toilet]=4&"
            b[3]=True
        else:
            keybutton[3].text="❌Свободная планировка"
            site.replace("das[flat.toilet]=4&","")
            b[3]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите состояние квартиры:", reply_markup = keyboard)
    if call.data == "rough_finish":
        if b[4]==False:
            keybutton[4].text="✅Черновая отделка"
            site=site+"das[flat.toilet]=4&"
            b[4]=True
        else:
            keybutton[4].text="❌Черновая отделка"
            site.replace("das[flat.toilet]=4&","")
            b[4]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Выберите состояние квартиры:", reply_markup = keyboard)
    if call.data == "c7":
        mes="Вы выбрали состояние квартиры"
        if b[0]==b[1] and b[1]==b[2] and b[2]==False and b[2]==b[3] and b[3]==b[4]:
            mes="Выбран любое состояние квартиры"
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id, text = mes)
        b=[False,False,False,False]
        area_from(call)
    if call.data == "last":
        if b[0]==False:
            keybutton[0].text="✅Не последний этаж"
            site=site+"das[flat.toilet]=2&"
            b[0]=True
        else:
            keybutton[0].text="❌Не последний этаж"
            site.replace("das[flat.toilet]=2&","")
            b[0]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Отметьте то, что вам еще нужно:", reply_markup = keyboard)
    if call.data == "first":
        if b[1]==False:
            keybutton[1].text="✅Не первый этаж"
            site=site+"das[flat.toilet]=3&"
            b[1]=True
        else:
            keybutton[1].text="❌Не первый этаж"
            site.replace("das[flat.toilet]=3&","")
            b[1]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Отметьте то, что вам еще нужно:", reply_markup = keyboard)
    if call.data == "photo":
        if b[2]==False:
            keybutton[2].text="✅Есть фото"
            site=site+"das[flat.toilet]=4&"
            b[2]=True
        else:
            keybutton[2].text="❌Есть фото"
            site.replace("das[flat.toilet]=4&","")
            b[2]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Отметьте то, что вам еще нужно:", reply_markup = keyboard)
    if call.data == "owner":
        if b[3]==False:
            keybutton[3].text="✅От хозяев"
            site=site+"das[flat.toilet]=4&"
            b[3]=True
        else:
            keybutton[3].text="❌От хозяев"
            site.replace("das[flat.toilet]=4&","")
            b[3]=False
        KeyB()
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id,text = "Отметьте то, что вам еще нужно:", reply_markup = keyboard)
    if call.data == "c8":
        mes="Вы выбрали"
        bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.id, text = mes)
        b=[False,False,False,False]
        end(call)

@bot.message_handler(commands=["start"])
def start(message):
    mes1 = "Вас приветствует чат-бот объявлений для аренды квартир с сайта Krisha.kz"
    bot.send_message(message.from_user.id, mes1)
    global site
    global keybutton
    global keyboard
    global b
    b=[False,False,False,False,False]
    site = "https://krisha.kz/arenda/kvartiry/?"
    keybutton=[]
    keybutton.append(types.InlineKeyboardButton (text="❌1-комн.", callback_data='1r'))
    keybutton.append(types.InlineKeyboardButton (text="❌2-комн.", callback_data='2r'))
    keybutton.append(types.InlineKeyboardButton (text="❌3-комн.", callback_data='3r'))
    keybutton.append(types.InlineKeyboardButton (text="❌4-комн.", callback_data='4r'))
    keybutton.append(types.InlineKeyboardButton (text="❌5+ комн.", callback_data='5r'))
    keybutton.append(types.InlineKeyboardButton (text="Даллее", callback_data='c1'))
    KeyB()
    bot.send_message(message.from_user.id, mes2, reply_markup=keyboard)

        
def term(message):
    global keybutton
    global keyboard
    keybutton=[]
    keybutton.append(types.InlineKeyboardButton (text="❌По часам", callback_data='hour'))
    keybutton.append(types.InlineKeyboardButton (text="❌Посуточно", callback_data='days'))
    keybutton.append(types.InlineKeyboardButton (text="❌На длительный срок", callback_data='long'))
    keybutton.append(types.InlineKeyboardButton (text="Далее", callback_data='c2'))
    KeyB()
    bot.send_message(message.from_user.id, "Выберите на какой срок арендовать квартиру:",reply_markup=keyboard)

def type_home(message):
    global keybutton
    global keyboard
    keybutton=[]
    keybutton.append(types.InlineKeyboardButton (text="❌Кирпичный", callback_data='brick'))
    keybutton.append(types.InlineKeyboardButton (text="❌Панельный", callback_data='panel'))
    keybutton.append(types.InlineKeyboardButton (text="❌Монолитный", callback_data='monolith'))
    keybutton.append(types.InlineKeyboardButton (text="❌иное", callback_data='other'))
    keybutton.append(types.InlineKeyboardButton (text="Далее", callback_data='c3'))
    KeyB()
    bot.send_message(message.from_user.id,"Выберите тип дома:",reply_markup=keyboard)

def furniture(message):
    global keybutton
    global keyboard
    keybutton=[]
    keybutton.append(types.InlineKeyboardButton (text="❌Полностью", callback_data='full'))
    keybutton.append(types.InlineKeyboardButton (text="❌Частично", callback_data='partly'))
    keybutton.append(types.InlineKeyboardButton (text="❌Без мебели", callback_data='nothing'))
    keybutton.append(types.InlineKeyboardButton (text="Далее", callback_data='c4'))
    KeyB()
    bot.send_message(message.from_user.id, "Выберите мебелирование квартиры:",reply_markup=keyboard)

def ethernet(message):
    global keybutton
    global keyboard
    keybutton=[]
    keybutton.append(types.InlineKeyboardButton (text="❌ADSL", callback_data='ADSL'))
    keybutton.append(types.InlineKeyboardButton (text="❌Через TV кабель", callback_data='TV'))
    keybutton.append(types.InlineKeyboardButton (text="❌проводной", callback_data='wired'))
    keybutton.append(types.InlineKeyboardButton (text="❌оптика", callback_data='optics'))
    keybutton.append(types.InlineKeyboardButton (text="Далее", callback_data='c5'))
    KeyB()
    bot.send_message(message.from_user.id,"Выберите тип Интернета в квартире:",reply_markup=keyboard)
    
def bathroom(message):
    global keybutton
    global keyboard
    keybutton=[]
    keybutton.append(types.InlineKeyboardButton (text="❌Раздельный", callback_data='separate'))
    keybutton.append(types.InlineKeyboardButton (text="❌Совмещенный", callback_data='combined'))
    keybutton.append(types.InlineKeyboardButton (text="❌2 с/у и более", callback_data='two'))
    keybutton.append(types.InlineKeyboardButton (text="❌Нет", callback_data='no'))
    keybutton.append(types.InlineKeyboardButton (text="Далее", callback_data='c6'))
    KeyB()
    bot.send_message(message.from_user.id,"Выберите тип санузла в квартире:",reply_markup=keyboard)

def condition(message):
    global keybutton
    global keyboard
    keybutton=[]
    keybutton.append(types.InlineKeyboardButton (text="❌Хорошее", callback_data='good'))
    keybutton.append(types.InlineKeyboardButton (text="❌Среднее", callback_data='average'))
    keybutton.append(types.InlineKeyboardButton (text="❌Требует ремонта", callback_data='repair'))
    keybutton.append(types.InlineKeyboardButton (text="❌Свободная планировка", callback_data='free_layout'))  
    keybutton.append(types.InlineKeyboardButton (text="❌Черновая отделка", callback_data='rough_finish'))
    keybutton.append(types.InlineKeyboardButton (text="Далее", callback_data='c7'))
    KeyB()
    bot.send_message(message.from_user.id,"Выберите состояние квартиры:",reply_markup=keyboard)
    
kb=types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True,one_time_keyboard=True)
skip=types.KeyboardButton(text="Пропустить")
kb.add(skip)
bl=0
def area_from(message):
    global kb
    global bl
    bl=1
    msg=bot.send_message(message.from_user.id, "Напишите от скольки квадратных метров будет площадь квартиры? Либо нажмите кнопку пропустить", reply_markup=kb)
    bot.register_next_step_handler(msg,get_text_messages)
def area_to(message):
    global kb
    msg=bot.send_message(message.from_user.id, "Теперь напите до скольки квадратных метров будет площадь квартиры? Либо нажмите кнопку пропустить", reply_markup=kb)
    bot.register_next_step_handler(msg,get_text_messages)

def price_from(message):
    global kb
    msg=bot.send_message(message.from_user.id, "Напишите от скольки тенге должна быть стоимость квартиры? Либо нажмите кнопку пропустить", reply_markup=kb)
    bot.register_next_step_handler(msg,get_text_messages)
def price_to(message):
    global kb
    msg=bot.send_message(message.from_user.id, "Напишите до скольки тенге должна быть стоимость квартиры? Либо нажмите кнопку пропустить", reply_markup=kb)
    bot.register_next_step_handler(msg,get_text_messages)

def floor_from(message):
    global kb
    msg=bot.send_message(message.from_user.id, "Напишите начинает от какого этажа должна находиться квартира? Либо нажмите кнопку пропустить", reply_markup=kb)
    bot.register_next_step_handler(msg,get_text_messages)
def floor_to(message):
    global kb
    msg=bot.send_message(message.from_user.id, "Напишите до какого этажа должна находиться квартира? Либо нажмите кнопку пропустить", reply_markup=kb)
    bot.register_next_step_handler(msg,get_text_messages)

def other(message):
    global keybutton
    global keyboard
    keybutton=[]
    keybutton.append(types.InlineKeyboardButton (text="❌Не последний этаж", callback_data='last'))
    keybutton.append(types.InlineKeyboardButton (text="❌Не первый этаж", callback_data='first'))
    keybutton.append(types.InlineKeyboardButton (text="❌Есть фото", callback_data='photo'))
    keybutton.append(types.InlineKeyboardButton (text="❌От хозяев", callback_data='owner'))
    keybutton.append(types.InlineKeyboardButton (text="Далее", callback_data='c8'))
    KeyB()
    bot.send_message(message.from_user.id,"Отметьте то, что вам еще нужно:",reply_markup=keyboard)

def end(message):
    global site
    true=False
    time.sleep(1)
    bot.send_message(message.from_user.id, "Вы завершили выбор объявлений аренды квартиры\n Новые объявления будут приходить следующими сообщениями")
    link=advert(site)
    rb = xlrd.open_workbook('users.xls',  on_demand = True)
    rs = rb.sheet_by_name('Users')
    num=rs.cell(0,0).value
    wb=copy(rb)
    rb.release_resources()
    del rb
    sh =wb.get_sheet(0)
    num=int(num+1)
    sh.write(0,0,num)
    sh.write(num,0,message.from_user.id)
    sh.write(num,1,site)
    sh.write(num,2,link)
    sh.write(num,3,message.message.chat.id)
    wb.save("users.xls")
    send_advert(site,message.from_user.id,message.message.chat.id)
    true=True

def advert(link):
    response = requests.get(site)
    bs= BeautifulSoup(response.text, "lxml")
    a=bs.main.find_all('a', class_="a-card__image")
    return 'https://krisha.kz/'+a[3].attrs['href']

def send_advert(site,userId,chatId):
    print(site)
    response = requests.get(site)
    bs= BeautifulSoup(response.text, "lxml")
    name=bs.main.find_all('a', class_="a-card__title")[3].text
    a=bs.main.find_all('a', class_="a-card__image")
    picture=a[3].picture.attrs['data-full-src']
    price=bs.main.find_all('div', class_="a-card__price")[3].text
    link=advert(site)
    bot.send_photo(chatId,picture)
    bot.send_message(userId, name+price+'\n'+link+'\n' )
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global bl
    global site
    if message.text!='Пропустить' and bl==1:
        site=site+"das[live.square][from]=="+message.text+"&"
        bl=2
        area_to(message)
    elif message.text=='Пропустить' and bl==1:
        area_to(message)
        bl=2
    elif message.text!='Пропустить' and bl==2:
        site=site+"das[live.square][to]=="+message.text+"&"
        bl=3
        price_from(message)
    elif message.text=='Пропустить' and bl==2:
        price_from(message)
        bl=3
    elif message.text!='Пропустить' and bl==3:
        site=site+"das[price][from]="+message.text+"&"
        bl=4
        price_to(message)
    elif message.text=='Пропустить' and bl==3:
        price_to(message)
        bl=4
    elif message.text!='Пропустить' and bl==4:
        site=site+"das[price][to]="+message.text+"&"
        bl=5
        floor_from(message)
    elif message.text=='Пропустить' and bl==4:
        floor_from(message)
        bl=5
    elif message.text!='Пропустить' and bl==5:
        site=site+"das[flat.floor][from]=="+message.text+"&"
        bl=6
        floor_to(message)
    elif message.text=='Пропустить' and bl==5:
        floor_to(message)
        bl=6
    elif message.text!='Пропустить' and bl==6:
        site=site+"das[flat.floor][to]=="+message.text+"&"
        other(message)
        bl=0
    elif message.text=='Пропустить' and bl==6:
        other(message)
        bl=0
print(time1)
true=True
Thread(target=bot.infinity_polling).start()
