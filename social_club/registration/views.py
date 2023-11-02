from django.shortcuts import render, redirect
from  django.contrib.auth import authenticate, login, logout
from django.contrib import messages



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