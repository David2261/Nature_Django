from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
	return HttpResponseRedirect("home")

def home(request):
	return render(request, 'rus/home.html')

def blog(request):
	return render(request, 'rus/blog.html')

def about(request):
	return render(request, 'rus/about.html')

def contact(request):
	return render(request, 'contact.html')

def source(request):
	return render(request, 'rus/source.html')