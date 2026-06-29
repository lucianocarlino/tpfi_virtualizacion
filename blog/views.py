import base64
from django.shortcuts import render, get_object_or_404, redirect
from .models import Perfil, Post, LoginIntento
from django.contrib.auth.decorators import login_required
from .forms import PostForm, PerfilForm


def index(request):
    perfil = Perfil.objects.first()
    posts = Post.objects.all()

    foto_base64 = None
    pdf_base64 = None
    if perfil and perfil.pdf_informe:
        with open(perfil.pdf_informe.path, 'rb') as f:
            pdf_base64 = base64.b64encode(f.read()).decode('utf-8')
    if perfil and perfil.foto:
        with open(perfil.foto.path, 'rb') as f:
            foto_base64 = base64.b64encode(f.read()).decode('utf-8')

    return render(request, 'blog/index.html', {
        'perfil': perfil,
        'posts': posts,
        'foto_base64': foto_base64,
        'pdf_base64': pdf_base64,
    })


def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    perfil = Perfil.objects.first()
    return render(request, 'blog/post.html', {
        'post': post,
        'perfil': perfil,
    })

@login_required(login_url='/43708688/admin/login/')
def adminblog_posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/43708688/adminblog/posts/')
    else:
        form = PostForm()
    posts = Post.objects.all()
    return render(request, 'blog/adminblog_posts.html', {
        'form': form,
        'posts': posts,
    })

@login_required(login_url='/43708688/admin/login/')
def adminblog_perfil(request):
    perfil = Perfil.objects.first()
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('/43708688/adminblog/perfil/')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'blog/adminblog_perfil.html', {
        'form': form,
        'perfil': perfil,
    })

@login_required(login_url='/43708688/admin/login/')
def adminblog_intentos(request):
    intentos = LoginIntento.objects.all()
    return render(request, 'blog/adminblog_intentos.html', {
        'intentos': intentos,
    })
