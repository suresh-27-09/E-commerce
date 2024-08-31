from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    if 'email' in request.session:
        ca=Category.objects.all()
        return render(request,'index.html',{'session':request.session['email'],'category':ca})
    else:
        return render(request,'index.html',{'session':None})
def register(request):
    if request.method=="POST":
        name=request.POST.get('uname')
        email=request.POST.get('uemail')
        number=request.POST.get('unumber')
        password=request.POST.get('upwd')
        obj=Register(uname=name,uemail=email,unumber=number,password=password)
        obj.save()
        return redirect('login')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=="POST":
        email=request.POST.get('uemail')
        password=request.POST.get('upwd')
        d=Register.objects.get(uemail=email)
        if d.password==password:
            request.session['email']=email
            return redirect('index')
    return render(request,'login.html')
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('index')

def blog(request):
    return render(request,'blog.html')
def blog_details(request):
    return render(request,'blog-details.html')
def shop(request):
    pro=Products.objects.all()
    ca=Category.objects.all()
   




    return render(request,'shop-grid.html',{'product':pro,'category':ca})
def shopcat(request,id):
    pro=Products.objects.all()
    ca=Category.objects.all()
    cat_pro=Products.objects.filter(category_id=id)
    print(cat_pro)
    print("here working")
    return render(request,'shop-grid.html',{'product':pro,'category':ca,'catpro':cat_pro})

def shop_details(request):
    return render(request,'shop-details.html')
def shop_cart(request):
    return render(request,'shoping-cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')