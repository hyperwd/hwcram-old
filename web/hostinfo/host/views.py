from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def help(request):
    title = '使用帮助'
    return render(request,'help.html',{'title':title})

def update(request):
    title = '更新记录'
    return render(request,'update.html',{'title':title})
