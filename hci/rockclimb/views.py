from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login

from rockclimb.forms import *


# Create your views here.
class HomePageView(TemplateView):
    """
    TemplateView for Home Page

    Attributes:
        template_name (str): Template to be rendered
    """
    template_name = 'rockclimb/home.html'


class RegisterView(CreateView):
    """CreateView for User

    Attributes:
        form_class (UserCreateForm) = form class that creates a User
        model (User) = User object to create
        success_message (str) = Message upon form valid
        success_url (str) = Reverse to FeedView
        template_name (str): Generic template to be rendered
    """
    form_class = UserCreateForm
    model = User
    success_message = "Account created successfully!"
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.

        This function also creates the user then logs them in
        """
        response =  super(RegisterView, self).form_valid(form)

        # Get the username and password created, log the user
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return response