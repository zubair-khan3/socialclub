
from django.urls import path
from . import views

urlpatterns = [
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    #path('sign_up', views.signup, name="sign_up"), 
    ]