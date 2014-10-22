from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'databasemodels.views.home'),
    url(r'^register/$', 'databasemodels.views.register'),
    url(r'^login/$', 'databasemodels.views.user_login'),
    url(r'^restricted/$', 'databasemodels.views.restricted'),
    url(r'^logout/$', 'databasemodels.views.user_logout'),
    url(r'^create_protocol/$', 'databasemodels.views.create_protocol'),
    url(r'^protocol_list/$', 'databasemodels.views.protocol_list'),
    url(r'^view/(?P<slug>[^\.]+).html', 'databasemodels.views.protocol',name='protocol'),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
)
