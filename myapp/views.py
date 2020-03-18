from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def error_404_view(request, exception):
    return render(request,'404.html')

def server(request):
    return HttpResponse("Server has started")

def index(request):
    mydictionary = {
        "posts" : Post.objects.all(),
        "message" : "Hey check out this amazing post at Placement Drive\nStay tuned for more...\n"
    }
    return render(request,'index.html',context=mydictionary)

def search(request):
    query = request.GET['query']
    mydictionary = {
        "posts" : Post.objects.all().filter(Q(title__icontains=query)
        ).order_by('-date'),
        "message" : "Hey check out this amazing post at Placement Drive\nStay tuned for more...\n"
    }
    return render(request,'index.html',context=mydictionary)

def about(request):
    return render(request,'about.html')

def userfeedbackform(request):
    if request.method == "POST":
        form = UserfeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            mydictionary = {
                "feedback":True,
                "form" : UserfeedbackForm()
            }
            return render(request,'userfeedbackform.html',context=mydictionary)
    elif request.method == "GET":
        mydictionary = {
            "form" :UserfeedbackForm()
        }
        return render(request,'userfeedbackform.html',context=mydictionary)

@login_required
def addtofavourite(request,uid,pid):
    try:
        obj = Favourite()
        obj.uid = uid
        obj.pid = pid
        obj.posttitle = Post.objects.get(id=pid).title
        obj.postlink = Post.objects.get(id=pid).link
        obj.save()
        mydictionary ={
            "add" : True,
            "favourites" : Favourite.objects.filter(uid=uid)
        }
        return render(request,'favourite.html',context=mydictionary)
    except:
        return redirect('account_login')

@login_required
def getfavourite(request,uid):
    mydictionary ={
        "favourites" : Favourite.objects.filter(uid=uid)
    }
    return render(request,'favourite.html',context=mydictionary)

