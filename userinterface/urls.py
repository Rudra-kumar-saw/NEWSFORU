from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('category/<str:category>/', views.category_news, name='category_news'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register_view, name='register'),
     path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
]
