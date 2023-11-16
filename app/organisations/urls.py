from django.urls import path
from organisations import views


urlpatterns = [
    path('<str:slug>/<int:id>/', views.OrganisationPageView.as_view(), name='organisations'),
    path('<str:slug>/', views.OrganisationView.as_view(), name='organisations'),
]

