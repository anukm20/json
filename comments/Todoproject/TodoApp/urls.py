from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('click/<int:id>',views.Click,name='click'),


    
]
