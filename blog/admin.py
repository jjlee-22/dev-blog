# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'status', 'created_on')
	list_filter = ("status",)
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'parent', 'created_on')
	search_fields = ['name']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
