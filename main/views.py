from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post


def index(request):
    last_post = Post.objects.order_by('-id')[0]
    info = Post.objects.all().order_by('-id')[1:9]
    return render(request, 'main.html', {'info': info, 'last_post': last_post})


def blog_detail(request, id):
    main = get_object_or_404(Post, id=id)
    return render(request, 'blog_detail.html', {'news': main})


def add_article(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, 'add_article.html', {"form": form})
        else:
            form = PostForm(request.POST)
            print("else")
            return render(request, 'add_article.html', {"form": form})
    else:
        form = PostForm(request.POST)
        print("else")
        return render(request, 'add_article.html', {"form": form})
