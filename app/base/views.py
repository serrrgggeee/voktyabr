from article.models import Article
import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils import timezone
import os
from .custom_proxy import Proxy
from .forms.parserform import ParserPvestiForm


now = timezone.now()
time_now = datetime.datetime.now()


class BaseParserMix(object):
	"""docstring for BaseParserMix"""
	def get_html_from_file(self, file, folder, n):
		file = os.path.join(os.path.dirname(__file__), f'parsing/{folder}/{file}{n}.html')
		with open(file) as f:
			return f.read()

	def save_to_product(self, text, name):
		file = '{}.txt'.format(name, now)
		with open(file, 'a') as file:
			file.write(text)

	def save_to_model(self, text, image, link, name):
		article = Article.objects.filter(url=link).first()
		result = "{} \n {} \n {} \n\n\n\n\n".format(image, text, link)
		if not article:
			article = Article(
				name=text[:127], 
				url=link, 
				description=result,
				image=image,
				site_sighn=name,
				category='pew'
			)
			article.save()
		else:
			article.image=image
			article.pub_date=time_now
			article.name=text[:127]
			article.description=result
			article.category='pew'
			article.save()

	def get_values(self):
		pass


class BaseParser(TemplateView, BaseParserMix):
	template_name = 'admin/import/pvestiparser.html'
	form_class = ParserPvestiForm

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():

			self.new_proxy = False
			self.get_proxy()
			self.get_header()
			self.get_values()
			self.set_succeess()
			return redirect('/admin/')
		else:
			self.set_not_exist('wrong')
			return redirect('/admin/')

	def set_not_exist(self, thing):
		messages.success(self.request, thing)

	def set_succeess(self):
		messages.success(self.request, 'ok')
		return redirect('/admin/')

	def get_header(self, file=None):
		self.type_page = self.request.POST.get('type_page')
		self.count_news = self.request.POST.get('count_news')

	def get_proxy(self):
		while self.new_proxy: 
			try:
				proxy = self.get_proxy()
			except ConnectionError:
				continue
			else:
				self.new_proxy = False
			proxy = Proxy()
			return proxy.get_proxy()

	def get_context_data(self, **kwargs):
		context = super(self.__class__, self).get_context_data(**kwargs)
		return context
