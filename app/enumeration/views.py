from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Enumeration


class EnumerationsView(TemplateView):
    template_name = 'enumeration/enumerations.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        slug = kwargs.get('slug', '')
        data['enumerations'] = Enumeration.objects.filter(show=True, parent__main=True, parent__slug=slug).order_by('name')
        if data['enumerations']:
            return data
        else:
            return data


class EnumerationAjaxView(TemplateView):
    template_name = 'enumeration/ajax/enumeration_ajax.html'

    def get_context_data(self, **kwargs):
        name_tmpl = self.request.GET.get('name_tmpl', None)
        if name_tmpl:
            self.template_name = 'enumeration/{0}.html'.format(name_tmpl)
        slug_key = kwargs.get('slug_key', '')
        data = super().get_context_data(**kwargs)
        data['enumerations'] = Enumeration.objects.filter(show=True, parent__slug=slug_key).order_by('name')
        return data


class PageView(TemplateView):
    template_name = 'enumeration/page.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = kwargs.get('id', '')
        data['page'] = Enumeration.objects.get(pk=id, show=True)
        return data
