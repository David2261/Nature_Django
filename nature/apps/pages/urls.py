from django.urls import path, include
from . import views

app_name = 'pages'
urlpatterns = [
	path('', views.index),
	path('home/', views.home, name="home"),
	path('blog/', views.blog, name="blog"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
	path('source/', views.source, name="source"),
]