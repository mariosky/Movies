from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from WebApp.views import movie

urlpatterns = patterns('',
    url(r'^movie/(\d+)/$', movie),

    # Examples:
    # url(r'^$', 'Movies.views.home', name='home'),
    # url(r'^Movies/', include('Movies.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
