from django.http import Http404

from django.views.generic import TemplateView
from .models import Article


class ArticleView(TemplateView):
    template_name = 'article/article.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = kwargs.get('id', '')
        try:
            article = Article.objects.get(id=id, show=True)
            data['article'] = article
            data['seo'] = article.seo
        except Article.DoesNotExist:
            raise Http404
        return data


class ArticleAddView(TemplateView):
    template_name = 'article/article_add.html'


# шаблон объявлений пользователя
class UserAdListView(TemplateView):
    template_name = 'article/users_ads_list.html'
