from bs4 import BeautifulSoup
import requests
import urllib.parse

from .models import CountParse, Parsing
from .views import BaseParser, BaseParserMix


class PvestiMixin(object):
	"""docstring for PvestiMixin"""
	def get_values(self):
		url_pages = Parsing.objects.filter(type_page=self.type_page, site_sighn='okt_pvesti_link')
		for url_page in url_pages:
			defaults = {}
			defaults['name'] = 'pvesti'
			counter, status = CountParse.objects.get_or_create(name=defaults['name'])
			if counter.count:
				i = counter.count
			else:
				i = 0

			parse = True
			while parse:
				url = '{0}&page={1}/'.format(url_page.url, i)
				page = requests.get(url)
				soup = BeautifulSoup(page.text)
				counter.count = i = counter.count + 1
				counter.save()
				results = soup.find_all(class_='post-item')
				s = urllib.parse.quote_plus('Сайт')
				if results == []:
					parse = False
					counter.count = 0
					counter.save()
					break


				for result in results: 
					text = result.get_text()
					image = result.find('img')['src'].split('/')
					image = urllib.parse.quote_plus(image[-1])
					link = 'http://www.pvesti.ru/{}'.format(result.find('a')['href'])
					link = link.replace("–", "%E2%80%93")
					image = 'http://www.pvesti.ru/{}'.format(image)
					image = image.replace("+", "%20")
					result = "{} \n {} \n {} \n\n\n\n\n".format(image, text, link)	
					try:
						self.save_to_product(result, 'pvesti')
					except  Exception as e:
						pass
					self.save_to_model(text, image, link, 'pvesti')
					
				
				if int(self.count_news) < i:
					parse = False
					counter.count = 0
					counter.save()
					break
	

class PvestiView(BaseParser, PvestiMixin):
	pass


class PvestiTask(PvestiMixin, BaseParserMix):
	type_page = 1 # Новости
	count_news = 11 # количество

	