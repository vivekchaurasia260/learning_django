from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Hello World!")
    
    #create a dictionary
    my_dict = {'insert_me': "Now I modified the index html path!"}
    return render(request,'first_app/index.html',context=my_dict)