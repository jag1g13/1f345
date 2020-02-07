"""
Views belonging to the core of the site which do not relate to a person, project or task.
"""

from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    View for site index page.
    """
    template_name = 'index.html'
