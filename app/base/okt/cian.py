from base.views import BaseParser, BaseParserMix
from bs4 import BeautifulSoup
import re


class CianMix(object):
	def get_values(self):
		for i in (1,2):
			page_source = self.get_html_from_file('cian', 'okt', i)
			soup = BeautifulSoup(page_source, features="html.parser")
			articles = soup.find_all('article')
			for article in articles:
				try:
					image = article.find('img')
					link = article.find('a')
					try:
						text = article.text
					except TypeError:
						text= ''
					try:
						image = image['src']
					except TypeError:
						image = ''
					try:
						link = link['href']
					except TypeError:
						link = ''
					if image or link or text:
						self.save_to_model(text, image, link, 'cian_okt')
				except Exception:
					pass


class CianView(BaseParser, CianMix):
	pass


class OktCianTask(CianMix, BaseParserMix):
	type_page = 1 # Новости
	count_news = 11 # количество
