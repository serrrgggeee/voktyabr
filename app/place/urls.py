from django.urls import path
from place import views
from place.api.views import places


urlpatterns = [
    path('<int:id>/', views.SinglePlaceView.as_view(), name='single_place'),
    path('places/', places, name='places')

]

