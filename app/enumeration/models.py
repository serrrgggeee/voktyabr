from base.translite import translit1
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
from main.models import Seo
from meta.models import ModelMeta
from mptt.models import MPTTModel, TreeForeignKey
from place.models import Place


class Enumeration(MPTTModel, ModelMeta):
    name = models.CharField('Ф.И.О или название', max_length=128)
    slug = models.CharField('Slug имени', max_length=128, blank=True, null=True, default='slug')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)
    link = models.URLField('link', max_length=255, null=True, blank=True)
    type_enumeration = models.CharField('Тип книги', max_length=128, blank=True, null=True)
    show = models.BooleanField(default=False, verbose_name='Отображать на сайте')
    main = models.BooleanField(default=False, verbose_name='Главная страница')
    menu_level = models.BooleanField(default=False, verbose_name='Верхний уровень')
    order = models.IntegerField(verbose_name='номер перечисления', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    pub_date = models.DateTimeField('Срок размещения в днях', default=now)
    image_enumeration = models.ImageField(upload_to='enumeration', verbose_name='image_enumeration', blank=True,
                                          null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, related_name="place_enumerate", verbose_name='Местро расположения', default='',
                              blank=True, null=True)
    seo = models.OneToOneField(Seo, on_delete=models.CASCADE, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('enumeration', kwargs={'id': self.pk})

    _metadata = {
        # в шаблоне если use_title_tag возвращает True, то генерируется title
        'use_title_tag': 'seo_title',
        'title': 'seo_title',
        'description': 'seo_description',
    }

    def save(self, *args, **kwargs):
        self.slug = translit1(slugify(self.name, allow_unicode=True))
        super(Enumeration, self).save(*args, **kwargs)
