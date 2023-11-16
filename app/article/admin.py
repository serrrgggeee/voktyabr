from django.contrib import admin
from django.db import models
from django.utils.html import mark_safe # Newer versions

from .models import Article

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FlatPageAdminRichText(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }

    @admin.display(description='TgUser')
    def get_tg_users(self, obj):
        print(dir(obj))
        if obj.user is None: return
        tg_user = obj.user.tguser_set.first()
        url = f'/admin/bot/tguser/{tg_user.id}/change/'
        link = f"<a target='_blank' href='{url}'>{tg_user.user.username}</a>"
        tg_link = f"<a target='_blank' href='https://t.me/{tg_user.user.username}'>{tg_user.user.username}</a>"
        return mark_safe(f'{link} {tg_link}')

    list_display = ("site_sighn", "name", 'user', 'get_tg_users')
    search_fields = ['site_sighn','name', 'user__username']
admin.site.register(Article, FlatPageAdminRichText)

