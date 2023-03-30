from django.urls import path
from pro_two_app import views

urlpatterns = [
    path('',views.users, name='user')
]
