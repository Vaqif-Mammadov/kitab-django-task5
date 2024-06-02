
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import book_list, register, add_book

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='catalog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='catalog/logout.html'), name='logout'),
    path('add_book/', add_book, name='add_book'),
    path('', book_list, name='book_list'),
]
