from django.conf.urls import url, include
from rockclimb.views import *
from django.contrib.auth.views import logout, login

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^climb/(?P<pk>\d+)/$', ClimbView.as_view(), name='climb'),

    

    url(r'^create_climb/$', ClimbCreateView.as_view(), name='create_climb'),
    url(r'^(?P<climb>\d+)/delete_climb/$', ClimbDeleteView.as_view(), name='delete_climb'),


    # Account login, logout, register account
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': "/"}, name="logout"),
    url(r'^user/accounts/register/$', RegisterView.as_view(), name='user'),
]