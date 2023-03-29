from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'practice': "Excercise is to practice the render function"}
    return render(request,'index.html', context=my_dict)
