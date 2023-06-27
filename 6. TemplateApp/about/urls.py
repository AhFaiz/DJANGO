from django.urls import path

#from .views import IndexAbout
from .views import IndexAbout

urlpatterns = [
    path('', IndexAbout),
]