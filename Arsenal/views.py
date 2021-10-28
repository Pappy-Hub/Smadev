from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from Gooner.forms import CreateUserForm



def home(request):
    return render(request, 'index.html')



def login_user(request):
    if request.user.is_authenticated:
        print(request.user)
        return redirect ('/')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)

            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                messages.info(request, 'username OR password is incorrect')                



        # print('No User')   

    return render(request, 'login.html') 


def logout_user(request):
    logout(request)
    return redirect('/')


def reg_page(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('/')
    else:
       form = CreateUserForm(request.POST)  
       if form.is_valid():
           form.save() 
           username = form.cleaned_data.get('username')
           messages.success(request, 'Account was created for ' + username)

           return redirect('login')

    context = {'form' :form}
    return render(request, 'reg.html', context)    


