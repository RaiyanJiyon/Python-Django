from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.showuserdata),
    path('success/', views.thankyou)
]
