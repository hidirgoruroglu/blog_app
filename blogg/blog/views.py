from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404

from .models import BlogCategory,BlogTag,Post

# Create your views here.
def all_posts_view(request):
    all_posts = Post.objects.filter(is_active = True).order_by("-created_at") # oluşturulma tarihine göre sırala en son yazılan ilk gözüksün
    categories = BlogCategory.objects.filter(is_active = True).order_by("title")
    tags = BlogTag.objects.filter(is_active = True).order_by("title")

    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = dict(categories = categories, tags = tags,posts = posts)
    return render(request,"blog/all_posts.html",context)


def category_view(request,category_slug):
    category = get_object_or_404(BlogCategory,slug=category_slug)
    posts = Post.objects.filter(is_active = True,category=category).order_by("-created_at") # oluşturulma tarihine göre sırala en son yazılan ilk gözüksün
    categories = BlogCategory.objects.filter(is_active = True).order_by("title")
    tags = BlogTag.objects.filter(is_active = True).order_by("title")

    context = dict(
        posts = posts,
        categories = categories,
        tags = tags,
        category = category,
          )
    return render(request,"blog/all_posts.html",context)

def tag_view(request,tag_slug):
    tag = get_object_or_404(BlogTag,slug=tag_slug)
    posts = Post.objects.filter(is_active = True,tag = tag).order_by("-created_at") # oluşturulma tarihine göre sırala en son yazılan ilk gözüksün
    categories = BlogCategory.objects.filter(is_active = True).order_by("title")
    tags = BlogTag.objects.filter(is_active = True).order_by("title")

    context = dict(
        posts = posts,
        categories = categories,
        tags = tags,
        tag = tag
          )
    return render(request,"blog/all_posts.html",context)

def post_detail_view(request,category_slug,post_slug):
    post = get_object_or_404(Post,slug = post_slug)
    post.view_count +=1
    post.save()
    categories = BlogCategory.objects.filter(is_active = True).order_by("title")
    tags = BlogTag.objects.filter(is_active = True).order_by("title")

    context = dict(
        post = post,
        categories = categories,
        tags = tags,
          )
    return render(request,"blog/post_detail.html",context)
