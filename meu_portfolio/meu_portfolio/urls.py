# meu_portfolio/urls.py (principal)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Incluir as URLs do app portfolio
]

