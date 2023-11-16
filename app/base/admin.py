from django.contrib import admin

from .models import CountParse, TypePage, Parsing


class ParsingAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(CountParse)
admin.site.register(TypePage)
admin.site.register(Parsing, ParsingAdmin)
