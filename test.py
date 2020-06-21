from vk_parser import VkParser 
import vk_api
from googletrans import Translator
import pickle
import re
import module
import time
import sqlite3

with open('token.txt', 'r') as f:
	code = f.read()

while True:
	conn = sqlite3.connect('FoodShare.db', check_same_thread = False)
	cursor = conn.cursor()

	sql = """
		SELECT * FROM posts
		"""
	cursor.execute(sql)
	pst=(cursor.fetchall())

	for i in reversed(pst[:-2]):
		if time.time()-i[-1]>3600 and i[0]!="519471":
			sql="""
				DELETE FROM posts WHERE id = ?
				"""
			cursor.execute(sql, (i[0],))
			conn.commit()

	parser = VkParser(token=code) 
	count=7
	a=parser.get_posts(count=count)	
	for i in reversed(a[1:]):
		sql = """
			SELECT id FROM posts
			"""
		cursor.execute(sql)
		pst_id_ls=cursor.fetchall()
		flag=False

		for j in pst_id_ls:
			if i["id"]==j[0]:
				flag=True
		if flag:
			break	
		#print(pst_id_ls)
		posts=[]
		for j in i.values():
			if type(j) == list:
				j=" ".join(map(str,j))
			elif j == "Морепродукты":
				j="Не определено"
			posts.append(j)
		posts.append(time.time())
		sql = """
			INSERT INTO posts VALUES (?, ?, ?, ?, ?, ? ,?)
			"""
		cursor.execute(sql, posts)
		conn.commit()
	conn.close()
	time.sleep(60) 