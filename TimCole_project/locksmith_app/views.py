from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'locksmith_app/index.html')

def contact(request):
    return render(request,'locksmith_app/contact.html')

def services(request):
    return render(request,'locksmith_app/services.html')

def about(request):
    return render(request,'locksmith_app/about.html')

def base(request):
    return render(request,'locksmith_app/base.html')
