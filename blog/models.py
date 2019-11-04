# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
STATUS = (
	(0, "Draft"),
	(1, "Publish")
)

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
	updated_on = models.DateTimeField(auto_now= True)
	content = RichTextUploadingField()
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS, default=0)
	post_image = models.ImageField(upload_to='img/', default='img/noimage/noimage.jpg', blank=True, null=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
	
