"""
URL configuration for hospital_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital_app.urls')),
    # path('view_files/', views.view_files, name='view_files'),
    # path('upload_file/', views.upload_file, name='upload_file'),
    # path('send_file/<int:file_id>/', views.send_file, name='send_file'),
    # path('request_file/<int:file_id>/', views.request_file, name='request_file'),
    # path('decrypt_file/<int:file_id>/', views.decrypt_file_view, name='decrypt_file')
]
