from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    """
    TemplateView for Home Page

    Attributes:
        template_name (str): Template to be rendered
    """
    template_name = 'rockclimb/home.html'
