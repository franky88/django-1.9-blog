from django.shortcuts import render
from .models import Post, Author, Category, Tag

# Create your views here.
def index(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
	}
	return render(request, 'blog/index.html', context)

def create(request):
	return render(request, 'blog/create.html')

def detail(request):
	return render(request, 'blog/detail.html')

def delete(request):
	return render(request, 'blog/delete.html')

def update(request):
	return render(request, 'blog/update.html')