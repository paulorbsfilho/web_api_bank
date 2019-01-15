from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_list, name='post_list'),
    path('post/<int:pk>/', views.account_detail, name='post_detail'),

]