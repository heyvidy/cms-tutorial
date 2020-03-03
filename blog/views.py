from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import BlogPost
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "home.html")


def blog_catalog(request):
    print("Current User:", request.user)
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


def signup_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(
            first_name=fname,
            last_name=lname,
            email=email,
            username=username,
            password=password,
        )
        print(user)

        return redirect(f"/{user.username}")

    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return HttpResponse("Invalid Credentials. <a href='/login'>Login again here</a>")

    return render(request, "signin.html")


def signout(request):
    logout(request)
    return redirect("/")
