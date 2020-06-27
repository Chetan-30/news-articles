from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'internship4.html')

def getstarted(request):
    return render(request,'getstarted.html')

def newpage(request):
    return render(request,'newpage.html')