from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


from rockclimb.forms import *


# Create your views here.
class HomePageView(TemplateView):
    """
    TemplateView for Home Page

    Attributes:
        template_name (str): Template to be rendered
    """
    template_name = 'rockclimb/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    TemplateView for Dashboard Page

    Attributes:
        template_name (str): Template to be rendered
    """
    template_name = 'rockclimb/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data()
        climb = Climb.objects.all()
        context['climb'] = climb

        return context


class ClimbView(LoginRequiredMixin, TemplateView):
    """
    TemplateView for Climb Page

    Attributes:
        template_name (str): Template to be rendered
    """
    template_name = 'rockclimb/climb.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data()
        climb = Climb.objects.filter(user=self.request.user)
        context['climb'] = climb

        return context

class ClimbCreateView(LoginRequiredMixin, CreateView):
    template_name = 'rockclimb/create_climb.html'
    form_class = ClimbCreateForm
    model = Climb

    def get_success_url(self):
       return reverse_lazy('dashboard')

    def form_valid(self, form):
        # Select the logged in user to be associated with the climb
        form.instance.user = self.request.user
        response = super(ClimbCreateView, self).form_valid(form)
        return response


class ClimbDeleteView(LoginRequiredMixin, DeleteView):
    model = Climb
    template_name_suffix = 'rockclimb/delete_climb.html'

    def get_object(self):
        return Climb.objects.get(pk=self.kwargs['climb'])

    def get_success_url(self):
        return reverse_lazy('dashboard')


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