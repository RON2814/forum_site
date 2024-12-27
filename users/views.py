from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            remember_me = request.POST.get('remember_me')
            if not remember_me:
                request.session.set_expiry(0)  # Session ends on browser close
            else:
                request.session.set_expiry(1209600)  # 2 weeks
            return redirect('index')
        else:
            error_message = "Wrong credentials, Please try again."
            return render(request, 'auth/login.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')