from django.urls import path
from place import views


urlpatterns = [
    path('', views.SinglePlaceView.as_view(), name='single_place'),

]

