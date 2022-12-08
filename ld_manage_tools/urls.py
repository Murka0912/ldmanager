"""untitled10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers, serializers, viewsets
#from .apps.ld_monitor import models
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from django.conf.urls import include, url
"""class Medo_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Medo2_2
        fields = ['PacketType','Addr','Ndoc','DateDoc']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.disks
        fields = ['srvaddr','namedisk','freespace','allspace']

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.disks.objects.all()
    serializer_class = UserSerializer

class MedoView(viewsets.ModelViewSet):
    queryset = models.Medo2_2.objects.all()
    serializer_class = Medo_serializer
router = routers.DefaultRouter()
router.register(r'connections', UserViewSet)

router.register(r'medo',MedoView)"""

urlpatterns = [
    path('', auth_views.LoginView.as_view()),
    path('home/',include('ld_manage_tools.apps.ld_monitor.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('grappelli/', include('grappelli.urls')),
    #path('1/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls',  namespace='rest_framework')),# grappelli URLS




    path("admin/", admin.site.urls),
]+staticfiles_urlpatterns()
