from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

#Third party apps
from autoslug import AutoSlugField
from django.urls import reverse
from tinymce import models as tinymce_models

# Create your models here.

class BlogCategory(models.Model):
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from = 'title',unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:category_view", kwargs={"category_slug": self.slug})


class BlogTag(models.Model):
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from = 'title',unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:tag_view", kwargs={"tag_slug": self.slug})


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory,on_delete=models.SET_NULL,null=True)
    tag = models.ManyToManyField(BlogTag)
    slug = AutoSlugField(populate_from = 'title',unique=True)
    cover_image = models.ImageField(upload_to='post')
    title = models.CharField(max_length=30)
    content = tinymce_models.HTMLField(blank=True,null=True) # doldurmak zorunda değiliz.
    is_active = models.BooleanField(default=False)
    view_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:post_detail_view", kwargs={"category_slug": self.category.slug,"post_slug": self.slug})