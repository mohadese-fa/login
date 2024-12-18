from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.

def login_view(request):
    return render(request, 'main_app/login.html')

def login_or_register_view(request):
    if request.method == 'POST':
        if 'singin-email' in request.POST:  
            username = request.POST.get['singin-email']
            password = request.POST.get['singin-password']
            user = authenticate( username=username, password=password)
            if user is not None:
                return redirect("/account/")  
            else:
                return render(request,"main_app/login.html",context={'msg': 'نام کاربری یا رمز عبور اشتباه است.'})

        elif 'register-email' in request.POST:  
            username = request.POST.get['register-email']
            password = request.POST.get['register-password']
            User.objects.create_user(username=username ,email=username, password=password, is_staff=False)
            return redirect("/login/")
    return render(request,"main_app/login.html")

def account(request):
    return render(request,"main_app/account.html")

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
    pv=productVariantClass.objects.filter(id=num)
    return render(request,"main_app/shop.html",context={"pv":pv})

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
