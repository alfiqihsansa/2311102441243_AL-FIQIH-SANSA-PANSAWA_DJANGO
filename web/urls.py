from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.urls import path, include


from web.views import home, about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about', about, name="about"),
    path('dashboard/', include('berita.urls'))
]

