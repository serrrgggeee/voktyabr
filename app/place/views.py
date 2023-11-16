from django.views.generic import TemplateView
from place.models import Place


class SinglePlaceView(TemplateView):
    template_name = 'place/single_place.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = kwargs.get('id', '')
        place = Place.objects.prefetch_related('photo').get(id=id, show=True)
        data['single_place']=place
        data['seo']=place.seo
        return data
    
