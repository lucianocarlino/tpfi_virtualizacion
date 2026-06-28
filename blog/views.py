import base64
from django.shortcuts import render, get_object_or_404
from .models import Perfil, Post


def index(request):
    perfil = Perfil.objects.first()
    posts = Post.objects.all()

    foto_base64 = None
    if perfil and perfil.foto:
        with open(perfil.foto.path, 'rb') as f:
            foto_base64 = base64.b64encode(f.read()).decode('utf-8')

    return render(request, 'blog/index.html', {
        'perfil': perfil,
        'posts': posts,
        'foto_base64': foto_base64,
    })