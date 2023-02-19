from django.urls import path
from page.views import (
    page_view,
)
app_name = "page"
urlpatterns = [
    path('<slug:slug>/', page_view,name="page_view"),
]