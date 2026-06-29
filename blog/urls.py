from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detalle, name='post_detalle'),
    path('adminblog/posts/', views.adminblog_posts, name='adminblog_posts'),
    path('adminblog/perfil/', views.adminblog_perfil, name='adminblog_perfil'),
    path('adminblog/intentos/', views.adminblog_intentos, name='adminblog_intentos'),
]
