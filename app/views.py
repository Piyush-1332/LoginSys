from django.shortcuts import render,redirect
from app.forms import RegisterationForm, Edit_Profile_Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


def home(request):
    return redirect('login')

def login_redirect(request):
    return redirect('login')

def register(request):
    if request.method=="POST":
        form=RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myapp')
    else:
        form=RegisterationForm()

        args={'form':form}
        return render(request,'folder/register.html',args)

def profile(request):
    args={'user':request.user}
    return render(request,'folder/profile.html',args)

def profile_edit(request):
    if request.method=="POST":
        form = Edit_Profile_Form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=Edit_Profile_Form(instance=request.user)
        args={'form':form}
        return render(request,'folder/edit_profile.html',args)
