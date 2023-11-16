from bs4 import BeautifulSoup

from base.views import BaseParser, BaseParserMix


class PinterestMix(object):
	def get_values(self):
		for i in [1, 2]:
			page_source = self.get_html_from_file('pinterest', 'okt', i)
			soup = BeautifulSoup(page_source, features="html.parser")
			results = soup.find_all(class_='MIw')
			for result in results:
				try:
					image = result.find('img')
					link = result.find('a')
					# try:
					# 	text = image['alt']
					# except TypeError:
					# 	text= ''
					try:
						image = image['src']
					except TypeError:
						image = ''
					try:
						link = f"https://ru.pinterest.com{link['href']}"
					except TypeError:
						link = ''	
					if image or link:
						self.save_to_model('', image, link, 'pinterest_okt')
				except Exception:
					pass


class PinterestView(BaseParser, PinterestMix):
	pass


class OktPinterestTask(PinterestMix, BaseParserMix):
	type_page = 1 # Новости
	count_news = 11 # количество
	