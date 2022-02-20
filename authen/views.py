from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from.forms import signupform, editprofileform

# Create your views here.
def changepassword(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed')
            return redirect('home')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request, 'authen/changepassword.html', {'form':form})

def editprofile(request):
    if request.method=='POST':
        form=editprofileform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes Saved')
            return redirect('home')
    else:
        form=editprofileform(instance=request.user)
    return render(request, 'authen/editprofile.html', {'form':form})

def registeruser(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password=password)            
            login(request, user)
            messages.success(request, 'User Created Successfully')
            return redirect('home')
    else:
        form=signupform()
    return render(request, 'authen/register.html', {'form':form})

def logoutuser(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('login')

def loginuser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            messages.error(request, 'Please enter correct credentials')
            return redirect('login')
    else:           
        return render(request, 'authen/login.html')

def home(request):
    return render(request, 'authen/home.html')