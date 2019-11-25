from django.urls import path, re_path
from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
	# /blog/
	path('', views.PostList.as_view(), name='home'),
	# /blog/<slug:slug>/
	path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
	# /blog/category/
	path('categories/', views.CategoryList.as_view(), name='categories'),
	# blog/category/<slug:slug>/
	url(r'^categories/(?P<category_slug>[-\w]+)/$', views.CategoryDetail, name='category_detail')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
