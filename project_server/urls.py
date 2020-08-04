from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/user/', include('main.urls')),
    path('core/', include('core.urls')),
    path('rest-auth/', include('rest_auth.urls')),

]
