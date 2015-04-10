from django.conf.urls import patterns, url
from jobs_dash import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	)