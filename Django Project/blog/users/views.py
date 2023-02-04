from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UserRegisterForm
#info about this page
#as we know that this page holds the controls of showing the content that needs to be shown
#so when the user will be filling the form then he/she will be clicking on sign up 
#and as a backend developer its our responsibility to save all that data and tell 
#django that yeah now u can go and save it in the users group
# now when we have success created a new user give the user a green message of acc created successfully
# if not created a user then now just give a empty form and redirect the user in the same page



def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username} successfully. Lets login now ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')