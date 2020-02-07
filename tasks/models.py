from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField


class Project(models.Model):
    """
    A project holds a set of related tasks.
    """

    #: Name of the project
    name = models.CharField(max_length=255,
                            blank=False, null=False)

    def get_absolute_url(self):
        return reverse('tasks:project.detail', kwargs={'pk': self.pk})
    


class Task(models.Model):
    """
    Model representing a single task to be completed.
    """

    #: Brief description of the task - serves as name / title
    description = models.CharField(max_length=255,
                                   blank=False, null=False)

    #: Project to which this task belongs - optional
    project = models.ForeignKey(Project, on_delete=models.PROTECT,
                                blank=True, null=True)

    #: Notes about this task - using a rich text editor
    notes = RichTextField()

    #: Expected time required to complete this task - deliberately abstract units
    expected_time = models.SmallIntegerField(blank=False, null=False)

    #: How the actual time once completed compared to the expected time
    time_difference = models.SmallIntegerField(blank=True, null=True)

    #: Datetime at which the task was added
    added_at = models.DateTimeField(auto_now_add=True,
                                    blank=True, null=False)

    #: Datetime at which the task was completed
    completed_at = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('tasks:task.detail', kwargs={'pk': self.pk})
