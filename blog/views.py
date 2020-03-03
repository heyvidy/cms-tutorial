from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import BlogPost
from django.utils import timezone


def home(request):
    return render(request, "home.html")


def blog_catalog(request):
    all_posts = BlogPost.objects.all()
    return render(request, "all_posts.html", {"all_posts": all_posts})


def post_page(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    return render(request, "post_page.html", {"post": post})


def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')

        blog = BlogPost.objects.create(title=title, 
                                        content=content, 
                                        author=author, 
                                        timestamp=timezone.now())

        return redirect(f"/blog/{blog.id}/")

    return render(request, "create_post.html")
