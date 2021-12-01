# -*- coding: utf-8 -*-
import telebot
from telebot import types


bot = telebot.TeleBot('Я спрятал. Введите свой токен')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать. Это SimpleBot и у него simple возможности')

@bot.message_handler(commands=['list'])
def lis(message):
    bot.send_message(message.chat.id, '/start , /help, /list')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Для вывода списка команд пропишите команду /list')
    bot.send_message(message.chat.id, 'Существуют также 3 сообщения,которые знает только создатель бота')

@bot.message_handler(content_types=['text'])
def messages(message):
    if message.text.lower() == "сайт":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/') 
    if message.text.lower() == "добро":
        bot.send_photo(message.chat.id, 'http://risovach.ru/upload/2013/11/mem/tvoe-vyrazhenie-lica_35383249_orig_.jpeg')
    if message.text.lower() == "ги":
        bot.send_photo(message.chat.id, 'https://i.pinimg.com/736x/a9/b8/9b/a9b89ba5494ae40b3ddc47bf6e82651e--samurai-gintama.jpg')


bot.infinity_polling()
