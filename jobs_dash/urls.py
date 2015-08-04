from django.conf.urls import patterns, url
from jobs_dash import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^add_job/$', views.add_job, name='add_job'),
	url(r'^(?P<job_address_slug>[\w\-]+)/$', views.job_detail, name='job_detail'),


	)