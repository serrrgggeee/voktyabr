from bs4 import BeautifulSoup
import os
from .views import BaseParser, BaseParserMix


class OlanMix(object):
	def get_html_from_file(self, file):
		file = os.path.join(os.path.dirname(__file__), f'parsing/{file}.html')
		with open(file) as f:
			return f.read()

	def get_values(self):
		page_source = self.get_html_from_file('olan')
		soup = BeautifulSoup(page_source, features="html.parser")
		results = soup.find_all(class_='object')
		for result in results:
			try:
				link = result.find(class_='header_adv_short')
				try:
					text = link.text
				except TypeError:
					text= ''
				try:
					image = result.find(class_='fotorama__img')['src']
				except TypeError:
					image = ''
				try:
					link = link['href']
				except TypeError:
					link = ''	
				self.save_to_model(text, image, link, 'olan_avito')
			except Exception:
				pass


class OlanView(BaseParser, OlanMix):
	pass


class OktOlanTask(OlanMix, BaseParserMix):
	type_page = 1 # Новости
	count_news = 11 # количество
	