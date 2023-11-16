from bs4 import BeautifulSoup
import requests

from .models import CountParse, Parsing
from .views import BaseParser, BaseParserMix


class PikabuViewMix(object):
	def get_values(self):
			url_pages = Parsing.objects.filter(type_page=self.type_page, site_sighn='pikabu_link')
			for url_page in url_pages:
				page = requests.get(url_page.url)
				soup = BeautifulSoup(page.text)
				results = soup.find_all(class_='story')

				for result in results:
					text_link = result.find(class_='story__title-link')
					try:
						text = text_link.get_text()
						link = text_link['href']
						image = result.find(class_="story-image__image")['src']
						self.save_to_model(text, image, link, 'pikabu')
					except (AttributeError, KeyError, TypeError):
						continue	


class PikabuView(BaseParser, PikabuViewMix):
	pass


class PikabuTask(PikabuViewMix, BaseParserMix):
	type_page = 1 # Новости
	count_news = 11 # количество