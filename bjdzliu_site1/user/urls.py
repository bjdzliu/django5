from django.urls import re_path
from django.urls import path
from .import views
from django.contrib import admin

urlpatterns = [
re_path(r'^$',views.index,name='index'),    
path(r'list/<int:year>/<int:month>/<int:day>/',views.index2,name='list'),  
path('admin',admin.site.urls),
] 