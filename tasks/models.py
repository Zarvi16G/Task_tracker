from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='tasks_created', null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        indexes = [
            models.Index(fields=['completed']),
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(completed__in=[True, False]),
                name='completed_boolean_check'
            ),
        ]
    def save(self, *args, **kwargs):
        if not self.title:
            raise ValueError("Title cannot be empty")
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('task_detail', args=[str(self.id)])
    def get_update_url(self):
        from django.urls import reverse
        return reverse('task_update', args=[str(self.id)])
    def get_delete_url(self):
        from django.urls import reverse
        return reverse('task_delete', args=[str(self.id)])
    def get_create_url(self):
        from django.urls import reverse
        return reverse('task_create')
    def get_list_url(self):
        from django.urls import reverse
        return reverse('task_list')
    def get_completed_tasks(self):
        return Task.objects.filter(completed=True)
    def get_incomplete_tasks(self):
        return Task.objects.filter(completed=False)
    def get_task_count(self):
        return Task.objects.count()
    def get_completed_task_count(self):
        return Task.objects.filter(completed=True).count()
    def get_incomplete_task_count(self):
        return Task.objects.filter(completed=False).count()
    def get_task_by_id(self, task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None
    def get_tasks_by_completion_status(self, completed):
        return Task.objects.filter(completed=completed)
    def get_tasks_by_title(self, title):
        return Task.objects.filter(title__icontains=title)
    def get_tasks_by_description(self, description):
        return Task.objects.filter(description__icontains=description)
    def get_tasks_by_date_range(self, start_date, end_date):
        return Task.objects.filter(created_at__range=(start_date, end_date))
    def get_tasks_by_created_at(self, created_at):
        return Task.objects.filter(created_at=created_at)
    def get_tasks_by_updated_at(self, updated_at):
        return Task.objects.filter(updated_at=updated_at)

    