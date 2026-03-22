from django.urls import path
from .views import ListaTarefas, CriarTarefa, EditarTarefa, DeletarTarefa
from django.contrib.auth import views as auth_views
from django.views.generic.edit import UpdateView

urlpatterns = [
    path('', ListaTarefas.as_view(), name='tarefas'),
    path('criar-tarefa/', CriarTarefa.as_view(), name='criar'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('editar-tarefa/<int:pk>/', EditarTarefa.as_view(), name='editar'),
    path('deletar-tarefa/<int:pk>/', DeletarTarefa.as_view(), name='deletar'),
]

