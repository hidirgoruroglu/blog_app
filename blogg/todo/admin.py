from django.contrib import admin

from .models import Todo,TodoCategory,TodoTag


# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'title',
        'is_active',
        'created_at',
        'updated_at',
        'id',
    ] 

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'is_active'
    ]


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'is_active'
    ] 

admin.site.register(Todo,TodoAdmin)
admin.site.register(TodoCategory,CategoryAdmin)
admin.site.register(TodoTag,TagAdmin)