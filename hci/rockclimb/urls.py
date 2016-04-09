from django.conf.urls import url, include
from rockclimb.views import *
from django.contrib.auth.views import logout, login

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),

    # Account
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': "/"}, name="logout"),
]