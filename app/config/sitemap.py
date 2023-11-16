from django.contrib.sitemaps import Sitemap
from book.models import Book
from place.models import Place


class BookSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return Book.objects.all()

    def lastmod(self, obj):
        return obj.pub_date


class PlaceSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return Place.objects.all()

    def lastmod(self, obj):
        return obj.pub_date