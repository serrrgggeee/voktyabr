from bs4 import BeautifulSoup
import requests
from .models import CountParse, Parsing
from .views import BaseParser


class YoulaView(BaseParser):

	def get_values(self):
		url_pages = Parsing.objects.filter(type_page=self.type_page, site_sighn='youla_link')
		for url_page in url_pages:
			defaults = {}
			defaults['name'] = 'okt_youla'
			counter, _ = CountParse.objects.get_or_create(name=defaults['name'])
			if counter.count:
				i = counter.count
			else:
				i = 1
			parse = True
			while parse:
				url = '{0}&page={1}'.format(url_page.url, i)
				page = requests.get(url)
				soup = BeautifulSoup(page.text)
				counter.count = i = counter.count + 1
				counter.save()
				results = soup.find_all(class_='product_item')
				if results == []:
					parse = False
					counter.count = 1
					counter.save()
					break

				if int(self.count_news) < i:
					parse = False
					counter.count = 0
					counter.save()
					break

				for result in results: 
					text = ''
					image = ''
					link = ''
					try:
						source = result.find('img')
					except TypeError:
						image = 'image'
					else:
						image = source['src']
						text = source['alt']
					try:
						link = 'https://youla.io{}'.format(result.find("a")['href'])
					except TypeError:
						link = 'link'	
					text = "{} \n {} \n подробнее:{} \n\n\n\n\n".format(image, text, link)	
					self.save_to_product(text, 'youla')
