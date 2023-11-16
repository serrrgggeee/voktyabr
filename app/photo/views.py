from django.shortcuts import redirect
from django.views.generic import TemplateView
from place.models import Photo


class PhotosView(TemplateView):
    template_name = 'photo/photos.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['photos']=Photo.objects.all()
        return data

class PhotoByView(TemplateView):
    template_name = 'photo/photos.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        slug = kwargs.get('slug', '')
        if slug:
            if Photo.objects.filter(photo_type=slug).exists():
                data['photos']=Photo.objects.filter(photo_type=slug)
            else:
                data['photos']=Photo.objects.all()
        return data

     