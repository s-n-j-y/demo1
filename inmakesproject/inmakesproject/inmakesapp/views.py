from django.shortcuts import render
from .models import Place
from .models import team

# Create your views here.
from django.http import HttpResponse
def demo(request):
    #name="india"
    obj=Place.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

#def about(request):
#    return  render(request,"about.html")
#def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res1=x+y
#    res2=x-y
#    res3=x*y
#    res4=x/y
#    return render(request,"about.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})
