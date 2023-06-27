from django.shortcuts import render

# Create your views here.

def IndexBlog(request):
    return render(request, 'blog/IndexBlog.html')
