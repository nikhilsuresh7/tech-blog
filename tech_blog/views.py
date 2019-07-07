from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogPost

def home_page(request):
	obj = BlogPost.objects.all()[:3]
	context = {
		"objects": obj,
	}
	return render(request, "home.html", context)