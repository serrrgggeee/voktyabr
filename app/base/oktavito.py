from bs4 import BeautifulSoup

import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from stem import Signal
from stem.control import Controller

import time


from .views import BaseParser, BaseParserMix

from .models import CountParse, Parsing
from base.constant import OKT_AVITO_FROM_ADMIN


class AvitoMix(object):
	def get_tor_session_ip(self, url):
		proxies = {'http':  'socks5://127.0.0.1:9050',
						   'https': 'socks5://127.0.0.1:9050'}
		return requests.get(url, proxies=proxies)


	def get_tor_session(self):
		session = requests.session()
		session.proxies = {'http':  'socks5://127.0.0.1:9050',
						   'https': 'socks5://127.0.0.1:9050'}
		return session
	
	def renew_connection(self):
		with Controller.from_port(port = 9051) as controller:
			controller.authenticate(password="111")
			controller.signal(Signal.NEWNYM)

	def set_driver(self):
		PROXY = "socks5://127.0.0.1:9050"
		options = Options()
		options.add_argument('--headless')
		options.add_argument('--no-sandbox')

		options.add_argument('--proxy-server=%s' % PROXY)
		
		driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)
		return driver

	def get_values(self):
		self.parsing_from_admin()
		self.parsing_from_site()
		
	def parsing_from_admin(self):
		htmls = Parsing.objects.filter(parsing_for_choices=OKT_AVITO_FROM_ADMIN)
		for item in htmls:
			soup = BeautifulSoup(item.html, features="html.parser")
			results = soup.find('div', attrs={'data-marker' : 'catalog-serp'}).find_all('div', attrs={'data-marker' : 'item'})
			self.save_search_results(results)	

	def parsing_from_site(self):
		url_pages = Parsing.objects.filter(type_page=self.type_page, site_sighn='okt_avito_link')
		for url_page in url_pages:
			try:
				results = []
				while len(results) == 0:
					time.sleep(600)
					self.get_tor_session()
					self.renew_connection()
					time.sleep(10)
					session = self.get_tor_session()
					page_source = session.get(url_page.url).text
					soup = BeautifulSoup(page_source, features="html.parser")
					results = soup.find_all(class_='styles-item-W5Z4K')
			except Exception as ex:
				pass
			self.save_results(results)

	def save_search_results(self, results):
		for result in results:
			header = result.find('a', attrs={'data-marker' : 'item-title'})
			try:
				text=header.text
			except TypeError:
				text= ''
			try:
				photo = result.find('div', attrs={'data-marker' : 'item-photo'})
				image = photo.find('img')['src']
			except (TypeError, AttributeError) as er:
				image = ''
			try:
				link = 'https://www.avito.ru{}'.format(header['href'])
			except (TypeError, AttributeError):
				link = ''	
			self.save_to_model(text, image, link, 'avito')

	def save_results(self, results):
		for result in results:
			header = result.find('header')
			try:
				text = result.text
			except TypeError:
				text= ''
			try:
				image = header.find('img')['src']
			except (TypeError, AttributeError):
				image = ''
			try:
				link = 'https://www.avito.ru{}'.format(header.find("a")['href'])
			except (TypeError, AttributeError):
				link = ''	
			self.save_to_model(text, image, link, 'avito')


class AvitoView(BaseParser, AvitoMix):
	pass


class OktAvitoTask(AvitoMix, BaseParserMix):
	type_page = 1 # Новости
	count_news = 11 # количество
	