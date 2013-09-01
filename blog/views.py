# Create your views here.
from django.views.generic import ListView, FormView
from blog.models import BlogPost, BlogPostForm

class IndexBlog(ListView):
	template_name = 'blog/index.html'
	#context_object_name = 'bposts'
	model = BlogPost

class NewBlog(FormView):
	template_name = 'blog/new.html'
	form_class = BlogPostForm
	success_url = '/'