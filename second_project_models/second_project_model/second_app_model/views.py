from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "HELLO I'M FROM FIRSTAPP!"}
    return render(request, 'second_app_model/index.html',context=my_dict)