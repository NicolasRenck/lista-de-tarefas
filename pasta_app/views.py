from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Tarefa
from django.views.generic.edit import UpdateView


class ListaTarefas(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name = 'tarefas'
    template_name = 'pasta_app/lista.html'
    
    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user)


class CriarTarefa(LoginRequiredMixin, CreateView): 
    model = Tarefa 
    fields = ['titulo', 'descricao', 'concluida'] 
    success_url = reverse_lazy('tarefas') 

    def form_valid(self, form): 
        form.instance.usuario = self.request.user 
        return super().form_valid(form)


class EditarTarefa(LoginRequiredMixin, UpdateView): 
    model = Tarefa 
    fields = ['titulo', 'descricao', 'concluida'] 
    success_url = reverse_lazy('tarefas') 
    template_name = 'pasta_app/tarefa_form.html'  


class DeletarTarefa(LoginRequiredMixin, DeleteView):
    model = Tarefa 
    context_object_name = 'tarefa' 
    success_url = reverse_lazy('tarefas') 
    template_name = 'pasta_app/tarefa_confirm_delete.html' 
