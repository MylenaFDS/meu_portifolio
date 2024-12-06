from django.shortcuts import render, get_object_or_404
from .models import Portfolio  # ou Post, dependendo do modelo

# View para listar todos os posts
def post_list(request):
    posts = Portfolio.objects.all()  # Substitua Portfolio por Post, se for esse o seu modelo
    return render(request, 'portfolio/post_list.html', {'posts': posts})

# View para detalhes de um post
def post_detail(request, pk):
    post = get_object_or_404(Portfolio, pk=pk)  # Substitua Portfolio por Post, se for esse o seu modelo
    return render(request, 'portfolio/post_detail.html', {'post': post})

