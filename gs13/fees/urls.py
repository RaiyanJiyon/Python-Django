from django.urls import path , include
from. import views

urlpatterns = [
    path('feesdj/', views.fees_django), 
    path('feesfor/', views.nestedfor), 
]
