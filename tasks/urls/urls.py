from django.urls import path
from tasks.views import TaskUpdateView, TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView

app_name = "tasks"

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('list_view/', TaskListView.as_view(), name='list_view'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
]