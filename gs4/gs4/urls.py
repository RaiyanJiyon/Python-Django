"""
URL configuration for gs4 project.

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
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('learndj/', views.learn_django),
    path('learnaltdj/', views.learn_django),
    path('learnpy/', views.learn_python),
    path('learnvar/', views.learn_var),
    path('learnmath/', views.learn_math),
    path('learnfrmt/', views.learn_format),
]