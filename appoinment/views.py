from django.shortcuts import render
from django.core.mail import send_mass_mail

# Create your views here.

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
        msg=message+"\n" "from email id :"+ emails
        msg1="Dear"+mname+ ",\n" "We will respond to your request as early as possible for immediate response you may directly call us.\n" "Your message \n"+message
        mes1=('Recived Web request FMML',msg1,'kcjrsop@gmail.com',[emails])
        mes2=('Web request from '+mname,'Request:'+msg,'kcjrsop@gmail.com',['andrewsjoseph120@gmail.com'])
        send_mass_mail( (mes1,mes2),fail_silently=False)
            
    
        return render(request,'contact.html',{'messenger':mname})
    else:    
        return render(request,'contact.html')
def index(request):
            if request.method=='POST':
                mname= request.POST['messenger']
                emails=request.POST['emails']
                message=request.POST['message']
                msg=message+"\n" "from email id :"+ emails
                msg1="Dear"+mname+ ",\n" "We will respond to your request as early as possible for immediate response you may directly call us.\n" "Your message \n"+message
                mes1=('Recived Web request FMML',msg1,'kcjrsop@gmail.com',[emails])
                mes2=('Web request from '+mname,'Request:'+msg,'kcjrsop@gmail.com',['andrewsjoseph120@gmail.com'])
                send_mass_mail( (mes1,mes2),fail_silently=False)
                return render(request,'contact.html',{'messenger':mname})
            else:
                return render(request,"index.html")