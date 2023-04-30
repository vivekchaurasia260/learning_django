from django.urls import path
from form_model_app import views

urlpatterns = [
    path('',views.users, name='user')
]