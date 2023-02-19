from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Todo,TodoCategory,TodoTag

# Create your views here.
@login_required(login_url='/admin/login/')
def all_todos_view(request):
    todos = Todo.objects.filter(is_active = True,user = request.user)
    # todos = Todo.objects.filter(title__icontains = "Django")
    context = {
        "todos":todos,
    }
    return render(request,'todo/todo_list.html',context)

@login_required(login_url='/admin/login/')
def todo_detail(request,category_slug,id):
    # try:
    #     todo = Todo.objects.get(id = id)
    #     context = {
    #         "todo": todo
    #     }
    #     return render(request, "todo/todo_detail.html",context)
    # except Todo.DoesNotExist:
    #     raise Http404
    todo = get_object_or_404(Todo,category__slug = category_slug,id = id, user = request.user)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_detail.html",context)

@login_required(login_url='/admin/login/')
def category_detail(request,category_slug):
    category = get_object_or_404(TodoCategory,slug = category_slug)
    todos = Todo.objects.filter(is_active = True, category = category,user = request.user)
    context = dict(todos = todos)
    return render(request, 'category/category_detail.html',context)

@login_required(login_url='/admin/login/')
def tag_view(request,tag_slug):
    tag = get_object_or_404(TodoTag,slug = tag_slug)
    context = {
        'tag':tag,
        'todos':tag.todo_set.filter(user = request.user)
    }
    return render(request,'todo/todo_list.html',context)