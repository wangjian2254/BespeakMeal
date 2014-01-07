from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from bespeak.views_user import clientLogin

admin.autodiscover()

urlpatterns = patterns('',
                        url(r'^meal/', include('bespeak.urls')),
    # Examples:
    # url(r'^$', 'BespeakMeal.views.home', name='home'),
    # url(r'^BespeakMeal/', include('BespeakMeal.foo.urls')),
     url(r'^clientLogin/$',clientLogin),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
