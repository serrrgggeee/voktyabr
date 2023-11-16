from bs4 import BeautifulSoup
import cssutils
import requests
from .models import CountParse, Parsing
from .views import BaseParser


class VolgogradView(BaseParser):

	def get_values(self):
		url_pages = Parsing.objects.filter(type_page=self.type_page, site_sighn='volgograd')
		for url_page in url_pages:
			defaults = {}
			defaults['name'] = 'volgograd'
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
				results = soup.find_all(class_='news-item')
				if results == []:
					parse = False
					counter.count = 1
					counter.save()
					break


				for result in results:
					name = result.find('h2').get_text()
					desc = result.find(class_="desc").get_text()
					text = '{}\n{}'.format(name, desc)
					div_style = result.find(class_="pic")['style']
					style = cssutils.parseStyle(div_style) 
					img_url = style['background']
					img_url = img_url.split('(')[1].split(')')[0]
					link = 'http://www.volgograd.ru{}'.format(result.find('a')['href'])
					image = 'http://www.volgograd.ru{}'.format(img_url)
					text = "{} \n {} \n {} \n\n\n\n\n".format(image, text, link)	
					self.save_to_product(text, 'volgograd')
				
				if int(self.count_news) < i:
					parse = False
					counter.count = 1
					counter.save()
					break

