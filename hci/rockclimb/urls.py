from django.conf.urls import url, include
from rockclimb.views import *
from django.contrib.auth.views import logout, login

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),

    # Account login, logout, register account
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': "/"}, name="logout"),
    url(r'^user/accounts/register/$', RegisterView.as_view(), name='user'),
]