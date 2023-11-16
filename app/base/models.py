from django.db import models
from django.utils import timezone
from base.constant import PARSING_FOR_CHOICES, DEFAULT

# from article.models import Article

class CountParse(models.Model):
  count = models.IntegerField('число обходов', default=0)
  name = models.CharField('имя парсера', max_length=128)

  def __str__(self):
    return 'name: {}; count: {}'.format(
            self.name, self.count)


class TypePage(models.Model):
    name = models.CharField('тип', max_length=128)
    type_sighn = models.CharField(max_length=64, default='')
    description = models.TextField('Описание типа')
    created = models.DateTimeField('Время для архива типов', default=timezone.now())
    show = models.BooleanField(default=True)

    def __str__(self):
        return 'name: {}'.format(self.name)


class Parsing(models.Model):
    name = models.TextField('Наименование')
    site_sighn = models.CharField(max_length=64, default='',  blank=True, null=True)
    url = models.URLField('адрес парсинга', max_length=500, default=None, blank=True, null=True)
    created = models.DateTimeField('Время для архива', default=timezone.now())
    show = models.BooleanField(default=True)
    # news = models.ForeignKey(Article, on_delete=models.SET_NULL, blank=True, null=True)
    type_page = models.ForeignKey(TypePage, on_delete=models.SET_NULL, blank=True, null=True)

    parsing_for_choices = models.CharField('от куда и для чего парсим', max_length=30, choices=PARSING_FOR_CHOICES, default=DEFAULT)
    html = models.TextField(verbose_name='html для парсинга', null=True, blank=True)
    def __str__(self):
        return '{}---{}---{}'.format(self.type_page, self.name, self.site_sighn)
