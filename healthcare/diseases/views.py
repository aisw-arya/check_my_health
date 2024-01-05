from django.shortcuts import render
from diseases.models import Diseases,CustomUser,Booking,Routine
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from diseases.forms import Form
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def diagnose(request):
    if (request.method=='POST'):
        s1=request.POST['s1']
        s2=request.POST['s2']
        s3=request.POST['s3']
        d=Diseases.objects.filter(Q(symptoms__icontains=s1) & Q(symptoms__icontains=s2) &Q(symptoms__icontains=s3))
        if d:
            return render(request,'disease.html',{'d':d})
    return render(request,'diagnose.html')
# def disease(request):
#     d=Diseases.objects.all()
#     return render(request,'disease.html',{'d':d})

def patient_register(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        p1=request.POST['p1']
        f=request.POST['f']
        s=request.POST['s']
        e=request.POST['e']
        ph=request.POST['ph']
        if (p==p1):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=s,email=e,phone_number=ph)
            u.is_patient=True
            u.save()
            return user_login(request)
    return render(request,'register.html')

def doctor_register(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        p1=request.POST['p1']
        f=request.POST['f']
        s=request.POST['s']
        e=request.POST['e']
        ph=request.POST['ph']
        i=request.FILES['pi']
        if (p==p1):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=s,email=e,phone_number=ph,image=i)
            u.is_doctor=True
            u.save()
            return user_login(request)
    return render(request,'doctor_register.html')

def user_login(request):
    if request.method=='POST':
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user and user.is_doctor==True:
            login(request,user)
            return render(request,'home.html')
        elif user and user.is_patient==True:
            login(request,user)
            return render(request,'home.html')
        else:
            messages.error(request,'invalid credentials')

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)

@login_required
def consultation(request,d):
    u=CustomUser.objects.get(username=d)
    if request.method=="POST":
        n=request.POST['n']
        a=request.POST['a']
        p=request.POST['p']
        d=request.POST['d']
        b=request.POST['b']
        da=request.POST['da']
        b=Booking.objects.create(name=n,age=a,address=d,phone=p,booking_date=b,date_added=da)
        b.save()
        return booking(request,b)
    return render(request,'consultation.html',{'user':u})
@login_required
def booking(request,b):
    t=b.date_added
    return render(request,'booking.html',{'b':b,'t':t})
@login_required
def checkup(request):
    user=request.user
    if user.is_doctor == True:
        c=Routine.objects.filter(name=user)
    else:
        c=Routine.objects.filter(user=user)
    return render(request,'checkup.html',{'c':c,'user':user})
@login_required
def adddata(request):
    if request.method=="POST":
        user=request.user
        c=request.POST['c']
        s=request.POST['s']
        b=request.POST['b']
        d=request.POST['d']
        a=Routine.objects.create(cholesterol=c,sugar=s,pressure=b,user=user,name=d)
        a.save()
        return checkup(request)
    return render(request,'adddata.html')

@login_required
def suggestion(request,p):
    b=Routine.objects.get(id=p)
    if request.method=="POST":
       f=Form(request.POST,instance=b)
       f.save()
       return checkup(request)
    f=Form(instance=b)
    return render(request,'suggestion.html',{'f':f})

@login_required
def delete(request,p):
    b=Routine.objects.get(id=p)
    b.delete()
    return checkup(request)