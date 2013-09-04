# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import BlogPost, BlogPostForm
from django.http import HttpRequest

class IndexBlog(ListView):
	template_name = 'blog/index.html'
	model = BlogPost

class DetailBlog(DetailView):
	template_name = 'blog/detail.html'
	model = BlogPost

class CreateBlog(CreateView):
	template_name = 'blog/create.html'
	model = BlogPost
	success_url = '/'

class UpdateBlog(UpdateView):
	template_name = 'blog/update.html'
	model = BlogPost
	success_url = '/'

class DeleteBlog(DeleteView):
	model = BlogPost
	success_url = '/'
