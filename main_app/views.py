from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as li , logout as lo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def pop_login(request):
    return render(request,'main_app/pop_login.html')

@login_required
def account(request):
    return render(request,"main_app/account.html")

def logout(request):
    lo(request)
    return redirect("/login/")

def login(request):
    if (request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")  
        u=authenticate(username=username,password=password)  
        if u is not None:
            li(request,u)
            if(u.role=="customer"):
                return redirect("/account/")
            else:
                return redirect("/admin/")
        else:
            return render(request,"main_app/login.html",context={"msg":"رمز یا نام کاربری اشتباه است"})
    else:
            return render(request,"main_app/login.html")

def register(request):
    if (request.method=="POST"):
        firstname=request.POST.get("first-name")
        lastname=request.POST.get("last-name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        CustomUserClass.objects.create_user(username,email,password,first_name=firstname,last_name=lastname,is_staff=False)
        return redirect("/login/")    
    return render(request,"main_app/register.html")

def index(request):
    stc=staticContentClass.objects.filter(key='home')
    stp=staticPhotoClass.objects.filter(key='home')
    return render(request,"main_app/index.html",context={"cnt":stc,"img":stp})

def product_category(request):
    pt=categoryClass.objects.all()
    return render(request,"main_app/product_category.html",context={"pt":pt})

def products(request,num):
    pc=productVariantClass.objects.filter(category_id=num)
    return render(request,"main_app/products.html",context={"pc":pc})

def shop(request,num):
    pv = productVariantClass.objects.filter(id=num)
    sizes = list({variant.size.name for variant in pv}) 
    colors = list({variant.color for variant in pv})
        
    return render(request,"main_app/shop.html",context={"pv":pv,"sizes":sizes,"colors": colors})

def agency(request):
    ag=agencyClass.objects.all()
    c=cityClass.objects.all()
    return render(request,"main_app/agency.html",context={"ag":ag,"c":c})

def agencyCity(request,num):
    ag=agencyClass.objects.filter(city_id=num)
    c=cityClass.objects.all()
    return render(request,"main_app/agency.html",context={"ag":ag,"c":c})

def about(request):
    stc=staticContentClass.objects.filter(key='about')
    stp=staticPhotoClass.objects.filter(key='about')
    return render(request,"main_app/about.html",context={"cnt":stc,"img":stp})

def contact_us(request):
    if (request.method=="POST"):
        s=""
        f=contactForm(request.POST)
        if (f.is_valid):
            f.save()
            s=request.POST.get("username")+" "+"عزیز پیام شما ثبت گردید"
            f=contactForm()
            return render(request,"main_app/contact_us.html",context={"username":s,"f":f})
    else:
        f=contactForm()
        return render(request,"main_app/contact_us.html",context={"f":f})

def question(request):
    stc=staticContentClass.objects.filter(key='question')
    faq=questionClass.objects.all()
    faqB=questionBClass.objects.all()
    faqC=questionCClass.objects.all()
    faqD=questionDClass.objects.all()
    return render(request,"main_app/question.html",context={"cnt":stc,"faq":faq,"faqB":faqB,"faqC":faqC,"faqD":faqD})
