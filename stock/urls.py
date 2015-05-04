from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'stock.views.index', name='home'),
	url(r'^msft/$', 'stock.views.msft'),
	url(r'^msft_update/(?P<param>\d+)/$', 'stock.views.msft_update', name='home'),
)
