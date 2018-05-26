from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   # return HttpResponse("This is Post Page")
    return render(request,'post/index.html')