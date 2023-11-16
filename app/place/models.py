from article.models import Article
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from main.models import Seo
from mptt.models import MPTTModel, TreeForeignKey


class Place(MPTTModel):
    name = models.CharField('Название населенного пункта',  max_length=128)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)
    type_place = models.CharField('Тип населенного пункта',  max_length=128)
    show = models.BooleanField(default=False,  verbose_name='Отображать на сайте')
    first_order = models.BooleanField(default=False,  verbose_name='Первые в списке')
    pub_date = models.DateTimeField('Срок размещения в днях', default=now)
    image_description = models.ImageField(upload_to='main_page', verbose_name='Image', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    seo = models.OneToOneField(Seo, on_delete=models.CASCADE, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name or self.code or ''

    def get_absolute_url(self):
        return reverse('single_place', kwargs={'id': self.pk})


class Photo(models.Model):
    TYPE_CHOICES = (
        ('', '------'),
        ('nature', 'Природа'),
        ('soc', 'Общество'),
        ('info', 'Информация'),
    )

    photo_type = models.CharField('Тип фотографии',choices=TYPE_CHOICES,  max_length=128,  null=True, blank=True)
    name = models.CharField('Название фотографии',  max_length=128, default='',  null=True, blank=True)
    image = models.ImageField(upload_to='description',
                              verbose_name='Image', default='')
    show = models.BooleanField(default=False,  verbose_name='Отображать на сайте')
    pub_date = models.DateTimeField('Дата размещения',default=now)
    description = models.TextField(verbose_name='Описание',  null=True, blank=True)
    comment = models.TextField(verbose_name='коментарии к фотографии', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    photo = models.ForeignKey(Place, on_delete=models.SET_NULL, related_name="photo", verbose_name='Местро расположения', null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name="article", verbose_name='Привязанная статья', null=True, blank=True)

    def __str__(self):
        return str(self.name) + "---" + str(self.photo)

