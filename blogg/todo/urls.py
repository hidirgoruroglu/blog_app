from django.urls import path

from todo.views import (
    all_todos_view,
    category_detail,
    tag_view,
    todo_detail)

app_name = "todo"
urlpatterns = [
    path('',all_todos_view,name='all_todos_view'),
    path('category/<slug:category_slug>/',category_detail,name='category_detail'),
    path('tag/<slug:tag_slug>/',tag_view,name='tag_view'),
    path('category/<slug:category_slug>/todo/<int:id>/',todo_detail,name='todo_detail'),
]