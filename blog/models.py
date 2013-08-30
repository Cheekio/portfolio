from django.db import models
from django.contrib.forms import ModelForm

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=20)
	body = models.Textfield()
	created = models.DateTimeField(auto_now_add=True)
	
class BlogPostForm(ModelForm):
	model = BlogPost