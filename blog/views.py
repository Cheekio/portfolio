# Create your views here.
from django.views.generic import ListView, FormView
from blog.models import BlogPost

class BlogIndex(ListView):
	template_name="index.html"
	model = BlogPost

class NewBlog(FormView):
	form = BlogPostForm