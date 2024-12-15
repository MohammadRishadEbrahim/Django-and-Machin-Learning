from django.shortcuts import render , redirect
from .models import Camera , Security , Contact
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse 
from .forms import contactModelForm
from django.conf import settings
# Create your views here.

def loginView(request):
    return render(request,"Accounts/Login.html")

def VarifyView(request):
    if request.method == "POST":
        if request.POST["Username"][0:2] == "CM":
            getName = request.POST["Username"]
            GetPassword = request.POST["Password"]
            User = Camera.objects.get(Name=getName)
            
            camera_name = str(User.Name)
            getActive = str(User.Active)
            strActive = "Active"
            strNoActive = "No Active"
            
            if User.Name == getName and User.Password == GetPassword:

                return render(request,"identify/Camera.html",{ "user" : User ,
                                                               "getActive" : getActive ,
                                                                 "strActive" : strActive , 
                                                                 "strNoActive" : strNoActive,
                                                                  "camera_name" : camera_name
                                                                    })
            
        elif request.POST["Username"][0:2] == "SC":
            getName = request.POST["Username"]
            GetPassword = request.POST["Password"]
            User  = Security.objects.get(Name=getName)
            camera_name = str(User.Camera_Name)
            getActive = str(User.Status)
            strActive = "Active"
            strNoActive = "No Active"
            media = settings.MEDIA_URL

            if User.Name == getName and User.Password == GetPassword:

                return render(request,"identify/Security.html",{ "user" : User ,
                                                               "getActive" : getActive ,
                                                                 "strActive" : strActive , 
                                                                 "strNoActive" : strNoActive ,
                                                                 "camera_name" : camera_name,
                                                                 "media" :media
                                                                 })
            
        else:

            return render(request,"Accounts/Login.html",{"data" : "Try Agian!!!"})
        
    return render(request,"Accounts/Login.html")
        

def saveContactView(request):
    if request.method == "POST":
        saveContact = Contact.objects.create(Name = request.POST["name"],
                            Email = request.POST["email"],
                            Subject = request.POST["subject"],
                            Message = request.POST["message"]
                            )
        
        saveContact.save()
        return redirect("/")
    else:
        return redirect("/")

