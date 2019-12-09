from django.shortcuts import render,get_object_or_404
from Garments.models import FormalShirt,CasualShirt,Jeans,Shorts,FormalShirt_W,CasualShirt_W,Jeans_W,Shorts_W
from django.contrib import messages
from django.db.models import Q
from Garments.forms import ContactForm
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        name=request.POST.get('contact_name')
        email=request.POST.get('contact_email')
        content=request.POST.get('content')

        subject="Hello From MyGarments.com"
        from_email =settings.EMAIL_HOST_USER
        user_email=email
        to_list=[user_email,from_email]
        send_mail(subject,content,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request,'contactus.html',{'form':form})

def formalshirts(request):
    lst=FormalShirt.objects.all()
    return render(request,'formalshirts.html',{'lst':lst})

def casualshirts(request):
    lst1=CasualShirt.objects.all()
    return render(request,'casualshirts.html',{'lst1':lst1})

def jeans(request):
    lst2=Jeans.objects.all()
    return render(request,'jeans.html',{'lst2':lst2})

def shorts(request):
    lst3=Shorts.objects.all()
    return render(request,'shorts.html',{'lst3':lst3})

def formalshirts_w(request):
    lst4=FormalShirt_W.objects.all()
    return render(request,'formalshirts_w.html',{'lst4':lst4})

def casualshirts_w(request):
    lst5=CasualShirt_W.objects.all()
    return render(request,'casualshirts_w.html',{'lst5':lst5})

def jeans_w(request):
    lst6=Jeans_W.objects.all()
    return render(request,'jeans_w.html',{'lst6':lst6})

def shorts_w(request):
    lst7=Shorts_W.objects.all()
    return render(request,'shorts_w.html',{'lst7':lst7})

def search_list(request):
    q=request.GET.get('query')
    if q:
        match1=FormalShirt.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
    if q:
        match2=CasualShirt.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
    if q:
        match3=Jeans.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
    if q:
        match4=Shorts.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
    if q:
        match5=FormalShirt_W.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
    if q:
        match6=CasualShirt_W.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
    if q:
        match7=Jeans_W.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
    if q:
        match8=Shorts_W.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
    

    if match1:
        return render(request,'search_list.html',{'match1':match1})
    if match2:
        return render(request,'search_list.html',{'match2':match2})
    if match3:
        return render(request,'search_list.html',{'match3':match3})
    if match4:
        return render(request,'search_list.html',{'match4':match4})
    if match5:
        return render(request,'search_list.html',{'match5':match5})
    if match6:
        return render(request,'search_list.html',{'match6':match6})
    if match7:
        return render(request,'search_list.html',{'match7':match7})
    if match8:
        return render(request,'search_list.html',{'match8':match8})
    

    else:
        messages.error(request,'No page found')
        return render(request,'search_list1.html')
    return render(request,'search_list.html')

def wishlist(request):
    q=request.GET.get('query')
    if q:
        match1=FormalShirt.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
        match2=CasualShirt.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
        match3=Jeans.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))
        match4=Shorts.objects.filter(Q(name__icontains=q)| Q(desc__icontains=q))

    if match1:
        return render(request,'search_list.html',{'match1':match1},{'match2':match2},{'match3':match3},{'match4':match4})
    

    else:
        messages.error(request,'No page found')
        return render(request,'search_list1.html')
    return render(request,'search_list.html')

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')

def thankyou(request):
    return render(request,'thankyou.html')

lst=[]
price=[]
'''def cart(request,x):
    item=get_object_or_404(FormalShirt,id=x)
    
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'price':price,'no_items':len(lst),'tot_price':sum(price)})
'''
def setsession(request):
    item=request.session.set_object_or_404(FormalShirt,id=x)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'price':price,'no_items':len(lst),'tot_price':sum(price)})

def getsession(request):
    price=request.session.get_object_or_404(FormalShirt,id=x)
    request.session.lst.append(item)
    request.session.price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'price':price,'no_items':len(lst),'tot_price':sum(price)})
    
    
