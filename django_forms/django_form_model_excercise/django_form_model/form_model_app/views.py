# Create your views here.
from django.shortcuts import render
#from django.http import HttpResponse
#from form_model_app.models import User
from form_model_app.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'formModel/index.html')

def users(request):
    form = NewUserForm()
    print("******************INSIDE USERS FUNC")
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
        
    return render(request, 'formModel/users.html', {'form':form})

