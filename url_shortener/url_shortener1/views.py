from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LongToShort
# Create your views here.

def helloWorld(request):
    return HttpResponse("Hello i am great i am learning django")

def homepage(request):
    context={"error":False,
        "submitted":False,
    }
    if request.method=="POST":
        data=request.POST
        #print(data)
        longurl=data['longurl']
        customname=data['custom_name']
        #print(longurl,customname)
        
        try:
            obj=LongToShort(long_url=longurl,custom_name=customname)
            context["custom_name"]=request.build_absolute_uri()+customname
            obj.save()
            context["submitted"]=True
            context["long_url"]=longurl
            context["date"]=obj.created_date
            context["visited"]=obj.visit_count
        except:
            context["error"]=True
    else:
        print("User didn't submit yet")
    return render(request,"index.html",context)

def redirect_url(request,customname):
    print(customname)
    row=LongToShort.objects.filter(custom_name=customname)
    print(row)
    if len(row)==0:
        return HttpResponse("This endpoint dosen't exist Error!!")
    obj=row[0]
    long_url=obj.long_url
    obj.visit_count+=1
    obj.save()
    return redirect(long_url)

def task(request):
    context={
        'name':['Aditya Sharma','Rishabh Rathi'],
        'company':'Akamai'
    }
    return render(request,'task.html',context)

def analytics(request):
    rows=LongToShort.objects.all()
    context={
        "rows":rows
    }
    return render(request,"all-analytics.html",context)