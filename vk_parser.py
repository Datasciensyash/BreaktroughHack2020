import vk_api
from googletrans import Translator
import pickle
import re

class VkParser():
	
	def __init__(self,
	token:str='b5aabf68b5aabf68b5aabf68c3b5d80c6dbb5aab5aabf68eb47462d91a717d9f99c55a2',
	encoder_path='./models/encoder.pkl',
	vectorizer_path='./models/vectorizer.pkl',
	model_path='./models/model.pkl',
	group_id='-109125816',
		) -> None:

		self.api = vk_api.VkApi(token=token)
		self.translator = Translator()
		self.gid = group_id

		with open(vectorizer_path, 'rb') as f:
			self.vectorizer = pickle.load(f)

		with open(encoder_path, 'rb') as f:
			self.encoder = pickle.load(f)

		with open(model_path, 'rb') as f:
			self.model = pickle.load(f)

	def get_photos(self, item):

		imgs = []

		if 'attachments' in item.keys():
			attachments = item['attachments']
			for attachment in attachments:
				if attachment['type'] == 'photo':
					imgs.append(attachment['photo']['sizes'][-1]['url'])
		return imgs

	def get_location(self, item):
		txt = re.sub(r'[^\w\s]','',item['text'].lower())
		location = 'Moscow'

		with open('spb.txt', 'r', encoding='utf-8') as f:
			spbkw = eval(f.read())

		for word in txt:
			if word in spbkw:
				location = 'Saint-Petersburg'
				break

		return location

	def get_category(self, item):
		text = self.translator.translate(item['text'])
		features = self.vectorizer.transform(text)
		prediction = self.model.predict(features)
		class_ = self.encoder.classes_[prediction]

		return class_

	def get_posts(self, count:int=10):

		response = self.api.method('wall.get', {'owner_id': self.gid})['items']

		out = []
		for item in response:
			imgs = self.get_photos(item)
			location = self.get_location(item)
			category = self.get_category(item)
			uid = item['id']
			url = f'https://vk.com/sharingfood?w=wall{self.gid}_{uid}'

			out.append({
				'id': uid,
				'text': item['text'],
				'category': category,
				'location': location,
				'url': url,
				'imgs': imgs,
				})

		return out



