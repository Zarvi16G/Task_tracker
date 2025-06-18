from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.views import View
from .models import Task
from .forms import TaskForm, TaskUpdateForm, TaskDeleteForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.http import Http404
from django.contrib import messages

#Decorators login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
# View to list tasks and handle actions

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/listed_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user).order_by('-created_at')

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'

    # Sobreescribimos get_queryset para que solo el propietario pueda ver los detalles
    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):  
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    context_object_name = 'create_task'
    success_url = reverse_lazy('tasks:list_view')

    # Sobreescribimos form_valid para asignar el usuario actual a la tarea
    def form_valid(self, form):
        form.instance.created_by = self.request.user # Asigna el usuario logueado a la tarea
        return super().form_valid(form) # Llama al método original para guardar la instancia

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/update.html'
    context_object_name = 'update_task'
    success_url = reverse_lazy('tasks:list_view')

    def get_queryset(self):
        # Filtra el queryset para incluir solo las tareas del usuario logueado
        return Task.objects.filter(created_by=self.request.user)
    

class TaskDeleteView(LoginRequiredMixin, View):
    success_url = reverse_lazy('tasks:list_view')

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        
        try:
            task.delete()
            messages.success(request, f'La tarea "{task.title}" ha sido eliminada exitosamente.')
        except Exception as e:
            messages.error(request, f'Ocurrió un error al intentar eliminar la tarea: {e}')
        return redirect(self.success_url)

    