
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.homepage)
    path('coun/', views.count, name='count')
    path('admin/', admin.site.urls),
]
