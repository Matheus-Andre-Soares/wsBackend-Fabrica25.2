from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('categorias/', views.categoria_list, name='categoria_list'),  # Lista de categorias
    path('categorias/nova/', views.categoria_create, name='categoria_create'),  # Criar nova categoria
    path('categorias/<int:pk>/editar/', views.categoria_update, name='categoria_update'),  # Editar categoria
    path('categorias/<int:pk>/excluir/', views.categoria_delete, name='categoria_delete'),  # Excluir categoria
    path('despesas/', views.despesa_list, name='despesa_list'),  # Lista de despesas
    path('despesas/nova/', views.despesa_create, name='despesa_create'),  # Criar nova despesa
    path('despesas/<int:pk>/editar/', views.despesa_update, name='despesa_update'),  # Editar despesa
    path('despesas/<int:pk>/excluir/', views.despesa_delete, name='despesa_delete'),  # Excluir despesa
    path('importar_taxas/', views.importar_taxas, name='importar_taxas'),  # Importar taxas de câmbio de API
]