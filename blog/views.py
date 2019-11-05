# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'blog/index.html'
	paginate_by = 5

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class CategoryList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-tag')
	template_name= 'blog/category.html'