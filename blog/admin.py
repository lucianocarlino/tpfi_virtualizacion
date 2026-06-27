from django.contrib import admin
from .models import Perfil, Post

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'legajo', 'email']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'actualizado']
    search_fields = ['titulo', 'contenido']
