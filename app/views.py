from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hai(request):
    if request.method=='POST':
        name=request.POST['un']
        pw=request.POST['pw']
        print(name)
        print(pw)
        return HttpResponse('Data Submitted Successfully ')
    return render(request,'hai.html')