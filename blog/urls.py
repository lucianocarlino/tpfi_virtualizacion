from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detalle, name='post_detalle'),
]
