from django.conf.urls import patterns, url

from blog import views


urlpatterns = patterns('',
	url(r'^$', views.IndexBlog.as_view(), name='index'),
	url(r'^new/$', views.NewBlog.as_view(), name='new'),
	)