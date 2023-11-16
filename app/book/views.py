from django.db.models import Q
from django.views.generic import TemplateView
from .models import Book


class BooksView(TemplateView):
    template_name = 'book/books.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data


class BookView(TemplateView):
    template_name = 'book/book.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = kwargs.get('id', '')
        data['pages'] = Book.objects.filter(
            Q(parent_id=id) | Q(parent__parent_id=id) | Q(parent__parent__parent_id=id), show=True).order_by('order')
        return data


class BookAjaxView(TemplateView):
    template_name = 'book/ajax/book_ajax.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = kwargs.get('id', '')
        data['pages'] = Book.objects.filter(
            Q(parent_id=id) | Q(parent__parent_id=id) | Q(parent__parent__parent_id=id), show=True
        ).order_by('order')
        return data


class PageView(TemplateView):
    template_name = 'book/page.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = kwargs.get('id', '')
        book = Book.objects.get(pk=id, show=True)
        data['page'] = book
        data['seo'] = book.seo
        return data

