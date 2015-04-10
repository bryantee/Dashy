from django.conf.urls import patterns, url
from jobs_dash import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<job_address_slug>[\w\-]+)/$', views.job_detail, name='job_detail'),

	)