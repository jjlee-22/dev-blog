# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
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
	updated_on = models.DateTimeField('date updated')
	content = RichTextUploadingField()
	created_on = models.DateTimeField('data published')
	status = models.IntegerField(choices=STATUS, default=0)
	post_image = models.ImageField(upload_to='img/', default='noimage.jpg', blank=True, null=True)
	category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
	tag = models.CharField(max_length=200, default='misc')

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
	
class Category(models.Model):
	name = models.CharField(max_length=200, unique=True)
	desc = models.TextField(default="")
	category_image = models.ImageField(upload_to='c_img/', default='noimage.jpg', blank=True, null=True)
	slug = models.SlugField(max_length=200, unique=True)
	created_on = models.DateTimeField('data published', default=datetime.now)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('slug', 'parent',)
		verbose_name_plural = "categories"

	def __str__(self):
		return self.name
