from django.conf.urls import patterns, include, url
from main import views

urlpatterns = patterns('',
    url('', include('social_auth.urls')),
    url(r'^main/$', views.index),
    url(r'^main/logout/$', views.logout_process),
)
