from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.contrib import messages
from django.db import models
from django.forms import ModelForm
from django_mptt_admin.admin import DjangoMpttAdmin
from place.models import Place, Photo


class CKEditorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }


class PageForm(ModelForm):
    class Meta:
        pass


class PhotoAdmin(admin.StackedInline):
    model = Photo
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }


class PlaceAdmin(DjangoMpttAdmin):
    form = PageForm

    class Meta:
        verbose_name_plural = 'place'
        app_label = 'места'
    tree_auto_open = 0
    list_display = ('name',)
    ordering = ('name',)
    inlines = [PhotoAdmin]

    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }

    def get_form(self, request, obj=None, **kwargs):

        if not request.user.is_superuser:
            self.exclude = ['user']
        return super(PlaceAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            if obj.user and obj.user != request.user:
                obj.user = request.user
                messages.info(request, 'Статья пренадлежит другому пользователю, вы не  можете ее править!!!')
            else:
                obj.user = request.user
                obj.save()
        else:
            obj.save()


admin.site.register(Place, PlaceAdmin)
admin.site.register(Photo)
