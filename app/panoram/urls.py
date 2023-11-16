from django.urls import path
from panoram import views


urlpatterns = [
    path('', views.PanoramView.as_view(), name='panoram'),
]

