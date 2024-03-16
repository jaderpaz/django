from django.urls import path
from estoque import views

urlpatterns = [
    path('', views.indexEstoque, name='index_estoque'),
    path('cadastro/', views.cadastroEstoque, name='cadastro_estoque'),
    path('criar_produto/', views.criarProduto, name='criar_produto'),
    # path('lista_produto/', views.listar_produto, name='lista_produto')
]