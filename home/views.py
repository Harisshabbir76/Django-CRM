from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Register

def Home(request):
    users=Register.objects.all()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request,"You are logged in")
            return redirect('Home')
    else:
        form=AuthenticationForm
        context = {
        'form': form,
        'users': users
        }   
        return render(request, 'home/home.html',context)
    
def logout_user(request):
    logout(request)
    messages.success(request,"You are logged out")
    return redirect('Home')

@login_required(login_url="/")
def register(request):
    if request.method=='POST':
        form=forms.Register_user(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration has been added")
            return redirect('Home')
    else:
        form=forms.Register_user()
        return render(request,'home/registration.html',{'form':form})


def record(request,pk):
    if request.user.is_authenticated:
        record=Register.objects.get(id=pk)
        return render(request, 'home/record.html',{'record':record})
    else:
        messages.success(request,"You must be logged in")
        return redirect('Home')
    

def delete_rec(request,pk):
    if request.user.is_authenticated:
        record=Register.objects.get(id=pk)
        record.delete()
        messages.success(request,"Record has been deleted")
        return redirect('Home')
    else:
        messages.success(request,"You need to logged in")
        return redirect('Home')


def edit_rec(request,pk):
    if request.user.is_authenticated:
        record=Register.objects.get(id=pk)
        form=forms.Register_user(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,"Data has been updated")
            return redirect('record',pk=pk)
        context = {
        'form': form,
        'record': record
        } 
        return render(request,'home/edit.html',context)
    else:
        messages.success(request,"You must be logged in")
        return redirect('Home')


def search_rec(request):
    users = None
    query=request.GET.get('query')
    if query:
        users=Register.objects.filter(first_name__icontains=query) | Register.objects.filter(last_name__icontains=query )
        if not users.exists():
            messages.warning(request,"No data found")
    context = {
        'query': query,
        'record': record
        } 
    return render(request, 'home/search.html',context)