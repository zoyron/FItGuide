from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^guide/',include('guide.urls')),
    url(r'',include('guide.urls')),
]
