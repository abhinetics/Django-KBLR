from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def page1(request):
    return render(request, 'page1.html')

def page3(request):
    return render(request, 'page3.html')

def page4(request):
    return render(request,'page4.html')

