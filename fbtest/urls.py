from django.conf.urls import patterns, include, url
from django.contrib import admin 
admin.autodiscover()
from main  import views

urlpatterns = patterns('',
    url('', include('social_auth.urls')),
    url(r'', include('main.urls')),
    url(r'^logged-in/$', views.logged_in),
    url(r'^admin/', include(admin.site.urls)),
)
