from django.shortcuts import render
from django.views.generic import TemplateView


class PanoramView(TemplateView):
    template_name = 'panoram/panoram.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data
