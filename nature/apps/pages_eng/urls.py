from django.urls import path, include
from . import views

app_name = 'pages_eng'
urlpatterns = [
	path('', views.index_eng),
	path('home/', views.home_eng, name="home_eng"),
	path('blog/', views.blog_eng, name="blog_eng"),
	path('about/', views.about_eng, name="about_eng"),
	path('source/', views.source_eng, name="source_eng"),
]