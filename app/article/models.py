from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from main.models import Seo
from django.contrib.postgres.fields import ArrayField


class Article(models.Model):
    AD = 'ad'
    CHOICES = (
        ('new', 'Новости'),
        ('pew', 'Спарсиная новость'),
        ('act', 'Мероприятия'),
        ('nat', 'Природа'),
        ('vid', 'Видео'),
        (AD, 'Объявление'),
    )

    name = models.CharField('Название статьи',  max_length=128, default='')
    image = models.ImageField(upload_to='article', max_length=256,
                              verbose_name='Article', null=True, blank=True)
    show = models.BooleanField(default=False,  verbose_name='Отображать')
    pub_date = models.DateTimeField('Дата размещения',default=now)
    chronology_date = models.DateTimeField('Хронологическая дата',null=True, blank=True)
    comment = models.TextField(verbose_name='коментарии к фотографии', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.CharField('тип статьи', max_length=3, choices=CHOICES, null=True, blank=True)
    site_sighn = models.CharField('название сайта', max_length=256,  default=None, null=True, blank=True)
    url = models.CharField('ссылка на статью', max_length=256, null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    seo = models.OneToOneField(Seo, on_delete=models.CASCADE, blank=True, null=True)
    send_to = ArrayField(models.CharField(max_length=200), blank=True, default=[])


    
    def __str__(self):
        return f'{self.name} {self.url}' or (self.image and self.image.path)  or self.description or "nothing"

