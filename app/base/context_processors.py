from django.conf import settings
from place.models import Place
from book.models import Book
from organisations.models import Organisation
from enumeration.models import Enumeration
from article.models import Article
class Menu():
    def _get_menu(self):
        return Place.objects.all()


def common(request, **kwargs):
    try:
        slug = request.path.split('/')[2]
    except IndexError:
        slug = ''
    return {
        'DEBUG': settings.DEBUG,
        'categories': Place.objects.filter(show=True),
        'BOOKS': Book.objects.filter(show=True),
        'ORGANISATIONS': Organisation.objects.filter(show=True, menu_level=True).order_by('order'),
        'ORGANISATION': Organisation.objects.filter(show=True, parent__slug=slug).order_by('order'),
        'ENUMERATION': Enumeration.objects.filter(show=True, parent=None),
        'LAST_NEWS' : Article.objects.filter(category='new'),
        'LAST_PARS_NEWS' : Article.objects.filter(category='pew').order_by('-pub_date').order_by('?')[:16],
        'VIDEO' : Article.objects.filter(category='vid')

    }