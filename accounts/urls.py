from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.account_list, name='post_list'),
    path('accounts/<int:id>', views.account_detail, name='post_detail'),
]