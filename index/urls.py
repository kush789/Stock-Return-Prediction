from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'index.views.index', name='home'),
	url(r'^nasdaq', 'index.views.nasdaq', name='home'),
)
