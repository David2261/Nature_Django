from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def index_eng(request):
	return HttpResponseRedirect("home_eng")

def home_eng(request):
	return render(request, 'eng/home.html')

def blog_eng(request):
	return render(request, 'eng/blog.html')

def about_eng(request):
	return render(request, 'eng/about.html')

def source_eng(request):
	return render(request, 'eng/source.html')