from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from .models import *


def home(request):
    queryset = request.GET.get("busqueda")
    posts = Post.objects.filter(estado = True).order_by("id")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
        ).distinct()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')                  
    posts = paginator.get_page(page_number)
    return render(request, "index.html", {"posts": posts})


def detalle_post(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        return render(request, "detalle_post.html", {"post": post})
    except ObjectDoesNotExist as e:
        return render(request, "no_encontrado.html", {"error": e})


def generales(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = "Generales")).order_by("id")
    queryset = request.GET.get("busqueda")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "Generales")
        ).distinct()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')                  
    posts = paginator.get_page(page_number)
    return render(request, "generales.html", {"posts": posts})


def programacion(request):
    posts = Post.objects.filter(estado = True, categoria__nombre = Categoria.objects.get(nombre__iexact = "Programacion")).order_by("id")
    queryset = request.GET.get("busqueda")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "programacion")
        ).distinct()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')                  
    posts = paginator.get_page(page_number)
    return render(request, "programacion.html", {"posts": posts})


def videojuegos(request):
    posts = Post.objects.filter(estado = True, categoria__nombre = Categoria.objects.get(nombre__iexact = "Videojuegos")).order_by("id")
    queryset = request.GET.get("busqueda")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "videojuegos")
        ).distinct()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')                  
    posts = paginator.get_page(page_number)
    return render(request, "videojuegos.html", {"posts": posts})


def tecnologia(request):
    posts = Post.objects.filter(estado = True, categoria__nombre = Categoria.objects.get(nombre__iexact = "Tecnologia")).order_by("id")
    queryset = request.GET.get("busqueda")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "tecnologia")
        ).distinct()
    
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')                  
    posts = paginator.get_page(page_number)
    return render(request, "tecnologia.html", {"posts": posts})


def tutoriales(request):
    posts = Post.objects.filter(estado = True, categoria__nombre = Categoria.objects.get(nombre__iexact = "Tutoriales")).order_by("id")
    queryset = request.GET.get("busqueda")
    if queryset:    
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = "tutoriales")
        ).distinct()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')                  
    posts = paginator.get_page(page_number)
    return render(request, "tutoriales.html", {"posts": posts})
