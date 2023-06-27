from django.contrib import admin
from django.urls import path

from .views import about,home,index
from blog import views as blogViews
from love import views as loveViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('blog/', blogViews.index),
    path('love/', loveViews.index),
    path('home/', home),
    path('', index),
]
