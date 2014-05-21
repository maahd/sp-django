from django.conf.urls import patterns, url
from django.contrib.auth import authenticate, login
from meddy1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^signup/$', views.signup_user, name="signup"),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'meddy1/login.html'}, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),

)