from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict ={'text':'hello world','number':100,}
    return render(request,'basic_app/index.html',context_dict)

def page1(request):
    return render(request,'basic_app/page1.html')

def page2(request):
    return render(request,'basic_app/page2.html')
