from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('meddy1.urls')),
    # url(r'^meddy2/', include('meddy2.urls')),
    # url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)