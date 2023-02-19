from django.contrib import admin

from .models import BlogCategory, BlogTag ,Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_active',
        'slug',
        'view_count',
    ]
    
@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    pass
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass