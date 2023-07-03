from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def userform(request):
    details=0
    data={}
    try:
        if request.method== "POST":
            n1=request.POST.get('Name')
            n2=request.POST.get('Phone')
            n3=request.POST.get('Address')
            details=(n1+n2+n3)
            data={
                'n1':n1,
                'n2':n2,
                'n3':n3
            }
            url="/about-us/?output={}".format(details)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"form.html",data)

    

def aboutpage(request):
    return render(request,"form2.html")
