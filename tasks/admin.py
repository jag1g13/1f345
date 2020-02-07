from django.contrib import admin

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin page for :class:`Project`.
    """
    pass


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin page for :class:`Task`.
    """
    pass
