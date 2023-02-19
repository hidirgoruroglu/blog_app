from django.db import models

from django.contrib.auth.models import User

#Third party apps
from autoslug import AutoSlugField
from django.urls import reverse


# Create your models here.

class TodoCategory(models.Model):
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from = 'title',unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("todo:category_detail", kwargs={"category_slug": self.slug})


class TodoTag(models.Model):
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from = 'title',unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("todo:tag_view", kwargs={"tag_slug": self.slug})


class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(TodoCategory,on_delete=models.SET_NULL,null=True)
    tag = models.ManyToManyField(TodoTag)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True,null=True) # doldurmak zorunda değiliz.
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("todo:todo_detail", kwargs={"category_slug": self.slug,id : self.pk})