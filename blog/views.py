from django.shortcuts import render, get_object_or_404
from .models import Perfil, Post

def index(request):
    perfil = Perfil.objects.first()
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {
        'perfil': perfil,
        'posts': posts,
    })

def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    perfil = Perfil.objects.first()
    return render(request, 'blog/post.html', {
        'post': post,
        'perfil': perfil,
    })
