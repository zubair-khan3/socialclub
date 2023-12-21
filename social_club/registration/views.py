from django.shortcuts import render, redirect
from  django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ClubUserForm, MyPasswordChangeForm

from events.models import UserDetails

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            messages.success(request,'logged in..!')
            return redirect('index')
        else:
            messages.success(request,'try again')
            return redirect('user_login')
    return render(request,'registration/user_login.html',{})

def user_logout(request):
    logout(request)
    messages.success(request,'logged out.!')
    return redirect('index')


def user_signup(request):
    if request.method == 'POST':
        form = ClubUserForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #after authenticate we need to sign in automatically 
            user = authenticate(username=username, password=password) 
            login(request,user)
            messages.success(request,"sign up sucessfull")
            UserDetails.objects.create(user_info=request.user) #creating a new model for users additional details.  
            return redirect('index')
    else:
        form = ClubUserForm()
    return render(request, 'registration/user_signup.html',{'form':form})



def change_password(request):
    if request.method == 'POST':
        form = MyPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            messages.success(request,"Password changed..")
            return redirect('index')
    else:
        form = MyPasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

def password_change_done(request):
    return render(request, 'registration/password_change_done.html')