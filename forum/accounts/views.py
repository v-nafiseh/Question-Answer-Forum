from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
        return redirect('/accounts/login/')    

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form':form})    

    
def profile(request):
    # user = User.objects.get(username=username, password=password)
    # context = {
    #     user : user
    # }
    return render(request, 'accounts/profile.html')



# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('/questions')
#         else:
#             messages.info(request, 'username or password is incorrect')    

#     return render(request, 'accounts/login.html')        



# def logoutUser(request):
#     logout(request)
#     return redirect('/questions')
