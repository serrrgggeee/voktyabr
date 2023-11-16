from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.contrib import messages
from django.db import models
from django.forms import ModelForm
from django_mptt_admin.admin import DjangoMpttAdmin
from organisations.models import Organisation, Photo


class PageForm(ModelForm):
    class Meta:
        pass


class PhotoAdmin(admin.StackedInline):
    model = Photo
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }


class OrganisationAdmin(DjangoMpttAdmin):
    form = PageForm
    exclude = ('slug',)
    class Meta:
        verbose_name_plural = 'организация'
        app_label = 'организации'
    tree_auto_open = 0
    list_display = ('name',)
    ordering = ('name',)
    inlines = [PhotoAdmin]

    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }

    def get_form(self, request, obj=None, **kwargs):

        if not request.user.is_superuser:
            self.exclude = ['user', 'order', 'slug']
        return super(OrganisationAdmin, self).get_form(request, obj, **kwargs)

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

admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Photo)
