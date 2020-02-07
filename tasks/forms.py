"""
Forms for creating or updating :class:`Task`s and :class:`Project`s.
"""


from django import forms

from . import models


class TaskUpdateForm(forms.ModelForm):
    """
    Form class for creating or updating an instance of :class:`Task`.
    """
    class Meta:
        model = models.Task
        exclude = [
            'completed_at',
            'time_difference',
        ]
    

class TaskCompleteForm(forms.ModelForm):
    """
    Form class for marking a :class:`Task` as complete.
    """
    class Meta:
        model = models.Task
        fields = [
            'notes',
            'time_difference'
        ]
    