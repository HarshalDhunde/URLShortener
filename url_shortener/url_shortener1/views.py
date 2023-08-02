from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LongToShort
# Create your views here.

def helloWorld(request):
    return HttpResponse("Hello i am great i am learning django")

def homepage(request):
    #to pass data to html page
    context={"error":False,
        "submitted":False,
    }
    # sending data to backend
    if request.method=="POST":
        data=request.POST
        #print(data)
        #storing the input fields in diff var
        longurl=data['longurl']
        customname=data['custom_name']
        #print(longurl,customname)
        
        try:
            #to make obj of class and passing the input data
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
# the main logic to redirect to long url form short url
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
        'name':['Harshal Dhunde','Anuj Pophali'],
        'company':'Accenture'
    }
    return render(request,'task.html',context)

def analytics(request):
    rows=LongToShort.objects.all()
    context={
        "rows":rows
    }
    return render(request,"all-analytics.html",context)