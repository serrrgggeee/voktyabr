from django import forms

from .widgets import BootstrapCharInput, BootstrapPasswordInput, BootstrapSelect

from base.models import TypePage

class ParserPvestiForm(forms.Form):
	COUNT_NEWS = (
   		(1,'Одна'),
   		(10,'Десять'),
   		(20,'Двадцать'),
   		(30,'Тридцать'),
   		(40,'Сорок'),
   		(50,'Пятьдесят'),
    	('', '-------------')		
	)

	type_page = forms.ModelChoiceField(queryset=TypePage.objects.all())
	count_news = forms.ChoiceField(required=False, choices=COUNT_NEWS)