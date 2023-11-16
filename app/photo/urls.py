from django.urls import path
from photo import views


urlpatterns = [
	path(r'<str:slug>/', views.PhotoByView.as_view(), name='photo_by'),
    path(r'', views.PhotosView.as_view(), name='photos'),
    
]

