from django.shortcuts import render
from django.http import  HttpResponse
from .models import *
# Create your views here.
def home(request):
    cdata=cities.objects.all()
    pdata=addplace.objects.all().order_by('-id')[0:8]
    mydict={"city":cdata,"place":pdata}
    return render(request,"user/index.html",mydict)

def contactus(request):
    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Mobile=request.POST.get("mobile","")
        Email=request.POST.get("email","")
        Message=request.POST.get("msg","")
        x=contact(name=Name,email=Email,mobile=Mobile,message=Message)
        x.save()
        status=True
    return render(request,"user/contactus.html",{'s':status})
def aboutus(request):
    return render(request,"user/aboutus.html")

def newplaces(request):
    city=cities.objects.all().order_by('-id')
    a=request.GET.get('abc')
    place=""

    if a is None:
        place = addplace.objects.all().order_by('-id')
    else:
        place = addplace.objects.all().filter(city=a)


    mydict = {"city": city, "place": place}


    return render(request,"user/newplaces.html",mydict)

def signin(request):
    return render(request,"user/signin.html")

def gudier(request):
    return render(request,"user/gudier.html")

def signin(request):
    return render(request,"user/signin.html")

def viewdetails(request):
    a=request.GET.get('msg')
    data=addplace.objects.filter(id=a)

    return render(request,"user/viewdetails.html",{"d":data})

def guiderdetails(request):
    city = cities.objects.all().order_by('-id')
    a = request.GET.get('abc')
    gd = ""

    if a is None:
        gd = guider.objects.all().order_by('-id')
    else:
        gd = guider.objects.all().filter(city=a)

    mydict = {"city": city, "guider": gd}

    return render(request,"user/guider.html",mydict)

def imagegallery(request):
    gdata=gallery.objects.all().order_by('-id')

    return render(request,"user/gallery.html",{"gallery":gdata})


def videogallery(request):
    vdata=video.objects.all().order_by('-id')

    return render(request,'user/videos.html',{'video':vdata})