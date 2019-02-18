from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


app_name='accounts'
urlpatterns = [
    path('registration/', views.getregistration, name='registration'),
    path('profile/', views.getprofile, name='profile'),
    path('profile/<int:p_id>/', views.getprofile, name='profile_pk'),
    path('profile/edit/', views.geteditprofile, name='edit_profile'),
    path('profile/password/', views.getchangepassword, name='change_password'),
    path('', views.index, name='index'),
    path('logout/', views.getlogout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/llogin.html'), name='login'),


    # path('login/', views.getlogin, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
    # path('password-change/', auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html'), name='password_change'),
    # path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/profile.html'), name='password_change_done'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    # path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
]
