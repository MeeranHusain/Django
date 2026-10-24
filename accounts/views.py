from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth, messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "You have logged in successfully!", extra_tags="login-notification")
            return redirect('home')
    else:
        form = AuthenticationForm()
    # print("Login form:", form)  # Debugging statement to check the form instance
    context = {'form': form}
    
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.warning(request,"You have been logged out successfully!",extra_tags="logout-notification")
        return redirect('login')

    return redirect('home')