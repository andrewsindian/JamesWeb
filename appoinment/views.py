from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,"index.html")
def openings(request):
    return render(request,"openings.html")
def photos(request):
    return render(request,"Photos.html")
def oldsite(request):
    return render(request,"Publications.html",{'pagename':"publication",'imga':"lib"})
def CIL(request):
    return render(request,"CentralFacilities.html",{'pagename':"CIL",'imga':"CIL"})


#def contact(request):
 #   return render(request,"contact.html")

def enquiry(request):
    return render(request,"report.html")
def Thinfilm(request):
    return render(request,"Thinfilm.html",{'pagename':"Thinfilms facility",'imga':"fulllab"})
def microwave(request):
    return render(request,"Microwave.html",{'pagename':"Microwave facility",'imga':"vna"})
def Members(request):
    return render(request,"Members.html",{'pagename':"Members",'imga':"gphoto"})
def Alumni(request):
    return render(request,"Alumni.html",{'pagename':"Alumni",'imga':"alu"})
def material(request):
    return render(request,"Materials.html",{'pagename':"Material Preparations ",'imga':"material"})
def contact(request):
    if request.method=='POST':
        mname= request.POST['messenger']
        emails=request.POST['emails']
        message=request.POST['message']
        
        send_mail(
            'web request - '+ mname,
            message,
            emails,
            ['andrewsjoseph120@gmail.com',emails],

        )
        return render(request,'contact.html',{'messenger':mname})
    else:    
        return render(request,'contact.html')
    