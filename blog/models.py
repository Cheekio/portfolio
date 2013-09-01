from django.db import models
from django.forms import ModelForm

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=20)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	
class BlogPostForm(ModelForm):
	class Meta:
		model = BlogPost