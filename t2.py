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

time1=int(datetime.datetime.today().strftime("%M"))
def advert(link):
    response = requests.get(link)
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
while True:
    if math.fabs(time1-int(datetime.datetime.today().strftime("%M"))):
        print("EBATЬ + 5 =")
        time1=int(datetime.datetime.today().strftime("%M"))
        print(time1)
        rb=xlrd.open_workbook('users.xls', on_demand=True)
        rs=rb.sheet_by_name("Users")
        num=int(rs.cell(0,0).value)
        wb=copy(rb)
        sh =wb.get_sheet(0)
        print(rs.cell(1,0).value)
        for i in range(1,num+1):
            lk=advert(rs.cell(i,1).value)
            print(lk+"!="+rs.cell(i,2).value)
            if(lk!=rs.cell(i,2).value):
                sh.write(i,2,lk)
                send_advert(rs.cell(i,1).value,int(rs.cell(i,0).value),int(rs.cell(i,3).value))
        rb.release_resources()
        del rb
        wb.save("users.xls")
bot.infinity_polling()
