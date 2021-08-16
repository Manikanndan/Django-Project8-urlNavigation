from django.shortcuts import render

# Create your views here.
def fun_app1(request):
    return render(request,'first.html',context={'name':'First'})

def fun_app2(request):
    return render(request,'second.html',context={'name':'Second'})