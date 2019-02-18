from django.db import models
from home.views import HomeView
from django.urls import path
from home import views
# Create your models here.

app_name='home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('change/<action>/<int:f_id>/', views.change_friend, name='change_friend'),
]