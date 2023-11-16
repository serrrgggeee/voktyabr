from base.views import BaseParser, BaseParserMix
from bs4 import BeautifulSoup
import re


class KuplusrazuMix(object):
	def get_values(self):
		for i in (1,):
			page_source = self.get_html_from_file('kuplusrazu', 'okt', i)
			soup = BeautifulSoup(page_source, features="html.parser")
			results = soup.find_all(class_='j-item')
			for result in results:
				try:
					image = result.find('img')
					link = result.find('a')
					try:
						text = result.text
						text = re.sub(r"\s+", " ", text, flags=re.UNICODE)
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
						self.save_to_model(text, image, link, 'kuplusrazu_okt')
				except Exception:
					pass


class KuplusrazuView(BaseParser, KuplusrazuMix):
	pass


class OktKuplusrazuTask(KuplusrazuMix, BaseParserMix):
	type_page = 1 # Новости
	count_news = 11 # количество
