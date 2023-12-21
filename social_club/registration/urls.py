
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('user_signup', views.user_signup, name="user_signup"), 

    ########### Password Reset ###################
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    ##############################################

    ########### Change password ##################
    path('change_password/', views.change_password, name='change_password'),
    path('password_change_done/', views.password_change_done, name='password_change_done')
    ]