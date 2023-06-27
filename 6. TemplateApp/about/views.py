from django.shortcuts import render

# Create your views here.
def IndexAbout(request):
    return render(request, 'about/IndexAbout.html')
