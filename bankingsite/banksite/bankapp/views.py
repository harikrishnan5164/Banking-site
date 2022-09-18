from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,'base.html')


def newpage(request):
    return render(request,'main.html')

