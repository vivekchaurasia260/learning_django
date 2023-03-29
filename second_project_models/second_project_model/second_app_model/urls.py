from django.urls import path
from second_app_model import views

urlpatterns = [
    path('', views.index, name="index")
]
