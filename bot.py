# -*- coding: utf-8 -*-
import telebot
from telebot import types
import sqlite3
import shutil
import requests

with open('key.txt', 'r') as f:
	code = f.read()
	
bot = telebot.TeleBot(code)

@bot.message_handler(content_types=['text'])
def get_text_messages(msg):
	conn = sqlite3.connect('FoodShare.db', check_same_thread = False)
	cursor = conn.cursor()
	if msg.text.lower() == "start" or msg.text == "/start":
		sql="""
			SELECT user_id FROM users
			"""
		
		cursor.execute(sql)
		a=cursor.fetchall()
		if msg.from_user.id in a:
			pass
		else:
			bot.send_message(msg.from_user.id,
				"Мы не знакомы, укажи свой город.\n Список доступных городов: Москва")
			bot.register_next_step_handler(msg, get_city)
		conn.close()
	else:
		bot.send_message(msg.from_user.id,
			"Я не знаю этой команды, попробуй /start")

def get_city(msg):
	conn = sqlite3.connect('FoodShare.db', check_same_thread = False)
	cursor = conn.cursor()
	dt=[]
	dt.append(msg.from_user.id)
	dt.append("")
	dt.append("Msc")
	sql="""
		INSERT INTO users VALUES(?,?,?)
		"""
		
	cursor.execute(sql, dt)
	a=cursor.fetchall()
	conn.commit()
	bot.send_message(msg.from_user.id,
	"Выбери интересующие тебя категории. Если интересует все, напише 'Все'. Список доступных категорий: \n Животные продукты \n Хлопья \n Какао \n Кофе \n Фрукты \n Овощи \n Травы и специи \n Орехи \n Бобы \n Соя \n Чай \n Овощи")
	conn.close()
	bot.register_next_step_handler(msg, get_cat)

def get_cat(msg):
	conn = sqlite3.connect('FoodShare.db', check_same_thread = False)
	cursor = conn.cursor()
	dt=[]
	dt.append(msg.text)
	dt.append(msg.from_user.id)
	sql="""
		UPDATE users SET category = ? WHERE user_id=?
		"""
	cursor.execute(sql, dt)
	a=cursor.fetchall()
	conn.commit()
	bot.send_message(msg.from_user.id, "Готово, жди уведомлений, а пока можешь посмотреть свежие объявления")
	
	sql="""
		SELECT * FROM posts
		"""
	cursor.execute(sql)
	a=cursor.fetchall()
	for i in a:
		#print(i)

		for url in i[4].split():
			response = requests.get(url, stream=True)
			with open('img.png', 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)
			del response
			bot.send_chat_action(message.chat.id, 'upload_photo')
			img = open('out.jpg', 'rb')
			bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
			img.close()
	conn.close()

bot.polling(none_stop=True, interval=0)