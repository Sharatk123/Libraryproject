from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('',views.home,name="home"),
    path('Add_Book/',views.Add_Book,name="Add_Book"),
    path('View_Order/',views.View_Order,name="View_Order"),
    path('delete_Order/<int:pk>',views.delete_Order,name="delete_Order"),
    path('contact/',views.contact,name="contact"),
    path('update_book/<int:pk>',views.update_book,name="update_book"),
    path('about/',views.about,name="about"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),


    
    
]
