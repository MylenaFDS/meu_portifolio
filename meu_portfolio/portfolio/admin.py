from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Mostra título e data de criação na lista de objetos
    search_fields = ('title',)  # Adiciona uma barra de busca para títulos
    list_filter = ('created_at',)  # Filtro lateral por data de criação

