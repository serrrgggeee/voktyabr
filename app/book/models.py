from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey

from main.models import Seo


class Book(MPTTModel):
    name = models.CharField('Название книги',  max_length=128)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)
    type_book = models.CharField('Тип книги',  max_length=128, blank=True, null=True)
    show = models.BooleanField(default=False,  verbose_name='Отображать на сайте')
    order = models.IntegerField(verbose_name='номер цтраницы')
    description = models.TextField(verbose_name='Описание')
    pub_date = models.DateTimeField('Срок размещения в днях', default=now)
    image_book = models.ImageField(upload_to='enumeration', verbose_name='image_book', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    seo = models.OneToOneField(Seo, on_delete=models.CASCADE, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('page', kwargs={'id': self.pk})

