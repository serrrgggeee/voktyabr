from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from django.conf.urls import handler404
from config.sitemap import BookSitemap, PlaceSitemap

from main.views import error404

admin.site.index_template = 'admin/my_custom_index.html'
admin.autodiscover()

sitemaps = settings.BASE_DIR
sitemaps = {'book': BookSitemap, 'place': PlaceSitemap}

handler404 = error404

urlpatterns = [
    path('parser/', include('main.urls')),  
    path('admin/', admin.site.urls),

    path('years/', include('main.urls')),
    

    path('add-article/', include('article.urls')),
    path('article/', include('article.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('book/', include('book.urls')),
    path('panoram/', include('panoram.urls')),
    path('organisation/', include('organisations.urls')),
    path('enumeration/', include('enumeration.urls')),
    path('<int:id>/', include('place.urls')),
    path('photos/', include('photo.urls')),
    path('sitemap.xml',  sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    path('', include('main.urls')),
    path('', include('bot.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


