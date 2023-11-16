from bs4 import BeautifulSoup
import requests

from .models import CountParse, Parsing
from .views import BaseParser, BaseParserMix


class Rica34ViewMix(object):
	def get_values(self):
			url_pages = Parsing.objects.filter(type_page=self.type_page, site_sighn='riac34_link')
			for url_page in url_pages:
				defaults = {}
				defaults['name'] = 'riac34'
				counter, _ = CountParse.objects.get_or_create(name=defaults['name'])
				if counter.count:
					i = counter.count
				else:
					i = 0

				parse = True
				while parse:
					url = '{0}?PAGEN_1={1}/'.format(url_page.url, i)
					page = requests.get(url)
					soup = BeautifulSoup(page.text)
					counter.count = i = counter.count + 1
					counter.save()
					results = soup.find_all(class_='new-block')
					if results == []:
						parse = False
						counter.count = 1
						counter.save()
						break


					for result in results:
						text = result.find(class_='caption').get_text()
						img_url = result.find(class_="preview").find('img')['src']
						link = 'http://riac34.ru{}'.format(result.find('a')['href'])
						image = 'http://riac34.ru{}'.format(img_url)
						result = "{} \n {} \n {} \n\n\n\n\n".format(image, text, link)	
						self.save_to_model(text, image, link, 'riac34')
					
					if int(self.count_news) <= i:
						parse = False
						counter.count = 1
						counter.save()
						break

class Rica34View(BaseParser, Rica34ViewMix):
	pass


class Rica32Task(Rica34ViewMix, BaseParserMix):
	type_page = 1 # Новости
	count_news = 11 # количество