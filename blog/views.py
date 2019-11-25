# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Post, Category

# Create your views here.
class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'blog/index.html'
	paginate_by = 5

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class CategoryList(generic.ListView):
	context_object_name = 'category_list'
	queryset = Category.objects.order_by('-created_on')
	template_name= 'blog/category.html'

def CategoryDetail(request, category_slug):
	categories = Category.objects.all()
	post = Post.objects.filter(status=1)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		post = post.filter(category=category)
	template = 'blog/category_detail.html'
	context = {'categories': categories, 'post': post, 'category': category}
	return render(request, template, context)