from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')

def resume(request):
    return render(request,'resume.html')