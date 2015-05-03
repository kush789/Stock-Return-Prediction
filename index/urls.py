from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'index.views.index', name='home'),
	url(r'^nasdaq/$', 'index.views.nasdaq', name='home'),
	url(r'^nasdaq_update/(?P<param>\d+)/$', 'index.views.nasdaq_update', name='home'),
)
