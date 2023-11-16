from django.urls import path

from .import views
from  .api.views import (
    ArticleAPIView, 
    ArticleAPIAddView, 
    UsersAdAPIView,
    UsersAdShowAPIView,
    UsersAdHideAPIView
)


urlpatterns = [
    path('api/list/', ArticleAPIView.as_view(), name='list_api'),
    path('api/add/', ArticleAPIAddView.as_view(), name='add_api'),
    path('add/', views.ArticleAddView.as_view(), name='add'),
    path('<int:id>', views.ArticleView.as_view(), name='single_place'),

    
    path('api/user_ads_list/', UsersAdAPIView.as_view(), name='user_ads_list_api'),
    path('user_ads_list/', views.UserAdListView.as_view(), name='user_ads_list'),
    path('api/user_ad_show_api/<int:id>/', UsersAdShowAPIView.as_view(), name='user_ad_show_api'),
    path('api/user_ad_hide_api/<int:id>/', UsersAdHideAPIView.as_view(), name='user_ad_hide_api'),

]