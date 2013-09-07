from django.conf.urls import patterns, url

from blog import views


urlpatterns = patterns('',
	url(r'^$', views.IndexBlog.as_view(), name='index'),
	url(r'^new/$', views.CreateBlog.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$', views.ReadBlog.as_view(), name='read'),
	url(r'^(?P<pk>\d+)/update/$', views.UpdateBlog.as_view(), name='update'),
	url(r'^(?P<pk>\d+)/delete/$', views.DeleteBlog.as_view(), name='delete'),
	)