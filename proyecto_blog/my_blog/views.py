from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
from django.db.models import Q

def home(request):
    return render(request, 'blog/home.html')

def listar_post(request):
    query = request.GET.get('q','')
    categoria = request.GET.get('categoria','')
    fecha_publicacion = request.GET.get('fecha_publicacion','')

    posts = Post.objects.all()

    if query:
        posts = posts.filter(Q(titulo__icontains=query)) | posts.filter(Q(contenido__icontains=query))
    if categoria:
        posts = posts.filter(categoria__icontains=categoria)
    if fecha_publicacion:
        posts = posts.filter(fecha_publicacion=fecha_publicacion)

    paginator = Paginator(posts, 10)  
    pagina_numero = request.GET.get('pagina')
    pagina_obj = paginator.get_page(pagina_numero)

    return render(request, 'blog/listar_post.html', {'pagina_obj': pagina_obj})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_post')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editar_post.html', {'form': form, 'post':post})

# Create your views here.
