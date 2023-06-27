from django.urls import path

from .views import IndexBlog

urlpatterns = [
    path('', IndexBlog),
]