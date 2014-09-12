from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProtoDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'databasemodels.views.home'),
    #url(r'^about/$', 'databasemodels.views.about'),
    url(r'^register/$', 'databasemodels.views.register'),
    url(r'^login/$', 'databasemodels.views.user_login'),
    url(r'^restricted/$', 'databasemodels.views.restricted'),
    url(r'^logout/$', 'databasemodels.views.user_logout'),
    url(r'^create_protocol/$', 'databasemodels.views.create_protocol'),
)
