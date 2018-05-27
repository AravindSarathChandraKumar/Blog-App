
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
     url(r'^$', include('post.urls')),
     url(r'^admin/', admin.site.urls),
     url(r'^post/', include('post.urls')),
    
]
