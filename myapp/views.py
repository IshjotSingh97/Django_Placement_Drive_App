from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse,JsonResponse

# Create your views here.
def server(request):
    return HttpResponse("Server has started")

def index(request):
    return render(request,'index.html')

def userfeedbackform(request):
    if request.method == "POST":
        form = UserfeedbackForm(request.POST)
        if form.is_valid():
            mydictionary = {
                "var1" : form.cleaned_data['title'] ,
                "var2" : form.cleaned_data['subject']
            }
        return JsonResponse(mydictionary)
        
    elif request.method == "GET":
        mydictionary = {
            "form" :UserfeedbackForm()
        }
        return render(request,'userfeedbackform.html',context=mydictionary)

