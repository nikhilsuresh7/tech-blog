from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .models import BlogPost
from .forms import BlogPostModelForm

def blog_post_list_view(request):
	# View all posts
	obj = BlogPost.objects.all()
	template_name = "blog/list.html"
	context = {"objects":obj}
	return render(request, template_name, context)

@login_required
def blog_post_create_view(request):
	# Create new post
	form = BlogPostModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		# To alter cleaned data
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()

		form = BlogPostModelForm()

	template_name = "form.html"
	context = {
	"title": "Create Post",
	"form": form
	}
	return render(request, template_name, context)

def blog_post_detail_view(request, id):
	# Detail page of post
	obj = get_object_or_404(BlogPost, id=id)
	template_name = "blog/detail.html"
	context = {"object":obj}
	return render(request, template_name, context)

@login_required
def blog_post_update_view(request, id):
	# Update existing post
	obj = get_object_or_404(BlogPost, id=id)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		# To alter cleaned data
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		form = BlogPostModelForm()

	template_name = "form.html"
	context = {
	"title": f"Edit: {obj.title}",
	"form": form
	}
	return render(request, template_name, context)

@login_required
def blog_post_delete_view(request, id):
	# Delete a post
	obj = get_object_or_404(BlogPost, id=id)
	template_name = "blog/delete.html"
	if request.method == "POST":
		obj.delete()
		return redirect("/blog")
	context = {"object": obj}
	return render(request, template_name, context)


