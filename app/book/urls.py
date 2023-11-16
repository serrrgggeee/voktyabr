from django.urls import path

from .import views


urlpatterns = [
    path('ajax/<int:id>/', views.BookAjaxView.as_view(), name='book_ajax'),
    path('page/<int:id>/', views.PageView.as_view(), name='page'),
    path('<int:id>/', views.BookView.as_view(), name='enumeration'),
    path('', views.BooksView.as_view(), name='books'),


]