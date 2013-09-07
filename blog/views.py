# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import BlogPost, BlogPostForm
from django.http import HttpRequest

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexBlog(ListView):
	template_name = 'blog/index.html'
	queryset = BlogPost.objects.all().order_by('-created')

class ReadBlog(DetailView):
	template_name = 'blog/read.html'
	model = BlogPost

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ReadBlog, self).dispatch(*args, **kwargs)

class CreateBlog(CreateView):
	template_name = 'blog/create.html'
	model = BlogPost
	success_url = '/'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(CreateBlog, self).dispatch(*args, **kwargs)

class UpdateBlog(UpdateView):
	template_name = 'blog/update.html'
	model = BlogPost
	success_url = '/'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(UpdateBlog, self).dispatch(*args, **kwargs)

class DeleteBlog(DeleteView):
	model = BlogPost
	template_name = 'blog/delete.html'
	success_url = '/'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DeleteBlog, self).dispatch(*args, **kwargs)