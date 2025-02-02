"""
URL configuration for bjdzliu_site1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import helloworld.views
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from  django.views.generic.base import RedirectView 
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', helloworld.views.index),
    path('blog/<int:id>', helloworld.views.blog),
    path('blog/<int:year>/<int:month>/<int:day>/<int:id>', helloworld.views.blog2),
    path('redirectTo',RedirectView.as_view(url='/index/')),
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT},name='media'),
    path('user/',include(('user.urls','user'),namespace="user")),
    path('download/file1',helloworld.views.download_file1),
    path('getinfo',helloworld.views.get_info),
    path('submitinfo',helloworld.views.update_info),
    path('to_login',helloworld.views.tologin),
    path('login',helloworld.views.login),
    path('upload',helloworld.views.upload),
]
