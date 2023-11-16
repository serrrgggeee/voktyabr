from article.models import Article
from base.translite import translit1
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import now
from main.models import Seo
from mptt.models import MPTTModel, TreeForeignKey
from place.models import Place


class Organisation(MPTTModel):
    slug = models.CharField('Slug организации', max_length=128, unique=True, null=True, blank=True,)
    name = models.CharField('Название', max_length=128)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)
    type_organisation = models.CharField('Тип организации', max_length=128, blank=True, null=True)
    show = models.BooleanField(default=False, verbose_name='Отображать на сайте')
    order = models.IntegerField(verbose_name='порядок в списке', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    pub_date = models.DateTimeField('Срок размещения в днях', default=now)
    image_organisation = models.ImageField(upload_to='organisation', verbose_name='image_organisation', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, related_name="place", verbose_name='Местро расположения', default='', blank=True, null=True)
    menu_level = models.BooleanField(default=False, verbose_name='Верхний уровень')
    seo = models.OneToOneField(Seo, on_delete=models.CASCADE, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Organisation.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def _get_unique_order(self):
        order = Organisation.objects.count()
        return order + 1

    def clean(self):
        self.slug = self._get_unique_slug()
        self.order = self._get_unique_order()
    def save(self, *args, **kwargs):
        self.slug = translit1(slugify(self.name))
        super(Organisation, self).save(*args, **kwargs)


class Photo(models.Model):
    name = models.CharField('Название фотографии', max_length=128, default='')
    image = models.ImageField(upload_to='description',
                              verbose_name='Image', default='')
    show = models.BooleanField(default=False, verbose_name='Отображать на сайте')
    pub_date = models.DateTimeField('Дата размещения', default=now)
    description = models.TextField(verbose_name='Описание', default='', blank=True, null=True)
    comment = models.TextField(verbose_name='коментарии к фотографии', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="user_organisation", blank=True, null=True)
    photo = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True, related_name="photo_organisation", verbose_name='Фотография к статье')
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name="article_organisation", verbose_name='Привязанная статья', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "фотографии"
