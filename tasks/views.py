"""
Views relating to the management of :class:`Task`s and :class:`Project`s.
"""

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import forms, models

class TaskCreateView(CreateView):
    """
    View for creation of new :class:`Task`s.
    """
    model = models.Task
    template_name = 'tasks/create.html'
    form_class = forms.TaskUpdateForm


class TaskListView(ListView):
    """
    View to render multiple :class:`Task`s.
    """
    model = models.Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    """
    View to render a single :class:`Task`.
    """
    model = models.Task
    template_name = 'tasks/detail.html'


class TaskUpdateView(UpdateView):
    """
    View to update a :class:`Task`.
    """
    model = models.Task
    template_name = 'tasks/update.html'
    form_class = forms.TaskUpdateForm


class TaskCompleteView(UpdateView):
    """
    View to mark a :class:`Task` as completed.
    """
    model = models.Task
    template_name = 'tasks/complete.html'
    form_class = forms.TaskCompleteForm


class TaskDeleteView(DeleteView):
    """
    View to delete a :class:`Task`.
    """
    model = models.Task
    template_name = 'tasks/confirm_delete.html'
    success_url = reverse_lazy('tasks:task.list')
