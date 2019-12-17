from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def pricing(request):
    return render(request,'pricing.html')
def service(request):
    return render(request,'service.html')

def trainer(request):
    return render(request,'trainer.html')
def contact(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        name=request.POST.get("contact_name")
        email=request.POST.get("contact_email")
        content=request.POST.get("content")

        subject="Hello from Gym"
        from_email=settings.EMAIL_HOST_USER
        user_email=email
        to_list=[user_email,from_email]
        send_mail(subject,content,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('sendmail')
    return render(request,'contact.html',{'form',form})
def blog(request):
    return render(request,'blog.html')

def blog_sidebar(request):
    return render(request,'blog_sidebar.html')

def blog_single(request):
    return render(request,'blog_single.html')

def course_single(request):
    lst1=Course_Single.objects.all()
    return render(request,'course_single.html',{'lst1',lst1})

def course(request):
    lst=Course.objects.all()
    return render(request,'course.html',{'lst',lst})
def sendmail(request):
    return render(request,'sendmail.html')

