from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm, EditForm
from .models import Exercise
from django.utils import timezone
from django.contrib.auth.decorators import login_required



def blank(request):
    return render(request,'base.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = RegisterForm()
        return render(request,'guide/register.html',{'form':form})


@login_required
def profile(request):
    return render(request,'guide/profile.html',{'user':request.user})



@login_required
def editprofile(request):
    if request.method == 'POST':
        form   = EditForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
        return redirect('/profile')
    else:
        form = EditForm(instance = request.user)
        return render(request,'guide/edit.html',{'form':form})


@login_required
def schedule(request):
    exercises = Exercise.objects.filter(start_date__lte = timezone.now()).order_by('start_date')
    return render(request,'guide/schedule.html',{'exercises':exercises})
