from django.urls import include, path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('create',
         views.TaskCreateView.as_view(),
         name='task.create'),

    path('',
         views.TaskListView.as_view(),
         name='task.list'),

    path(
        '<int:pk>',
        include([
            path('',
                views.TaskDetailView.as_view(),
                name='task.detail'),

            path('update',
                views.TaskUpdateView.as_view(),
                name='task.update'),

            path('complete',
                views.TaskCompleteView.as_view(),
                name='task.complete'),

            path('delete',
                views.TaskDeleteView.as_view(),
                name='task.delete'),
        ])
    ),
]
