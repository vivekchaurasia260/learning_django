from django.conf import urls
from django.urls import path
from learning_app import views

#TEMPLATE TAGGING
app_name = 'learning_app'

urlpatterns = [
    path('relative/',views.relative, name="relative"),
    path('other/',views.other,name="other"),
]

