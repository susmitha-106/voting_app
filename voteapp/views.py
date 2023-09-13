from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html",context)

def detail(request):
    context ={}
    return(request,"detail.html", context)

def result(request):
    context = {}
    return(request,"result.html", context)

def signin(request):
    context = {}
    return(request,"signin.html", context)

def signup(request):
    context = {}
    return(request,"signup.html", context)
