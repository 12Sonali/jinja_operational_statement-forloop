from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'Sonali'}
    return render(request,'forloop.html',context=d)