from django.db import models


class Seo(models.Model):
    title = models.TextField('наименование', max_length=68, blank=True, null=True)
    description = models.TextField('описание', max_length=128, blank=True, null=True)
    keywords = models.TextField('ключевые слова', max_length=128, blank=True, null=True)
    h1 = models.TextField('h1', max_length=68, blank=True, null=True)

    def __str__(self):
        return '{}---{}---{}'.format(self.title, self.description, self.keywords)