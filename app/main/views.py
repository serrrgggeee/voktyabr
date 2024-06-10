from base.translite import translit1
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, loader
from django.views.generic import TemplateView
from django.utils.text import slugify
from enumeration.models import Enumeration
from main.forms import PhotoAploadForm, FileAploadForm
from organisations.models import Photo as Photoorg
import os
from pathlib import Path
from place.models import Photo


class ListOktMainView(TemplateView):
    template_name = 'main.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ListOktMainView, self).get_context_data(**kwargs)
    #     print(context['view'])
    #     return context


class ImportView(TemplateView):
    template_name = 'admin/import/prefimport.html'

    def get(self, request):
        form = PhotoAploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PhotoAploadForm(request.POST, request.FILES)
        if form.is_valid():
            place = form.cleaned_data['place']
            user = form.cleaned_data['user']
            photo_type = form.cleaned_data['photo_type']
            organisation = form.cleaned_data['organisation']
            type_photo = form.cleaned_data['type_photo']
            for count, x in  enumerate(request.FILES.getlist("file")):
                image_photo = str(x).rsplit('.')[-2]
                if type_photo == 'place':
                    p = Photo(image='description/file_' +str(translit1(slugify(image_photo, allow_unicode=True)) + '.jpg'), photo=place, user=user)
                    p.save()
                elif type_photo == 'organisation':
                    p = Photoorg(image='description/file_' +translit1(slugify(image_photo, allow_unicode=True) + '.jpg'), photo=organisation, user=user)
                    p.save()
                elif photo_type:
                    p = Photo(image='description/file_' +str(translit1(slugify(image_photo, allow_unicode=True)) + '.jpg'), user=user, photo_type=photo_type)
                    p.save()
                self.process(x, count)
        return redirect('/admin/')

    def process(self, f, count):
        image_photo = str(f).rsplit('.')[-2]
        media_path = os.path.join(settings.MEDIA_ROOT, 'description/')
        with open(media_path+'file_' +str(translit1(slugify(image_photo, allow_unicode=True)) + '.jpg'), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


class FileImportView(TemplateView):
    template_name = 'admin/import/file_import.html'

    def get(self, request):
        form = FileAploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FileAploadForm(request.POST, request.FILES)
        filename = request.FILES.get("file").readlines()
        if form.is_valid():
            place = form.cleaned_data['place']
            parent = form.cleaned_data['parent']

            for line in filename:
                description = ''
                line = line.decode('utf-8').split('-----')
                try:
                    description = line[1]
                except IndexError:
                    pass
                name = line[0][0].upper()
                try:
                    enum = Enumeration.objects.get(name=name, parent=parent)
                except Enumeration.DoesNotExist:
                    enum = Enumeration(name=name, parent=parent, show=True)
                    enum.save()
                en = Enumeration.objects.get_or_create(name=line[0], description=description,
                 place=place, parent=enum, show=True)
        return redirect('/admin/')

    def process(self, f, count):
        pass


def error404(self, request):
    template = loader.get_template('404.htm')

    context = {
    }
    return HttpResponse(template.render(context, request))
