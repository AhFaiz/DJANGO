from django.urls import path

from .views import index,recent


urlpatterns= [
    path('recent/',recent),
    path('', index)
]