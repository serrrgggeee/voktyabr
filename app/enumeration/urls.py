from django.urls import  path
from .import views


urlpatterns = [
    path('page/<int:id>/', views.PageView.as_view(), name='enumeration_page'),
    path('<str:slug>/<str:slug_key>/', views.EnumerationAjaxView.as_view(), name='enumeration_by_slug'),
    path('<str:slug>/', views.EnumerationsView.as_view(), name='enumeration'),
]


