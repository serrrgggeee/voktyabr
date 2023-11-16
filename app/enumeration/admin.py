from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.contrib import messages
from django.db import models
from django.forms import ModelForm
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Enumeration


class EnumerationAdmin(DjangoMpttAdmin):
    class Meta:
        verbose_name_plural = 'Перечисление'
        app_label = 'Перечисления'
    tree_auto_open = 0
    list_display = ('name',)
    ordering = ('name',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ['user']
        return super(EnumerationAdmin, self).get_form(request, obj, **kwargs)

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

admin.site.register(Enumeration, EnumerationAdmin)