from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company


def signup_user(request):
    """Sign Up users."""
    return render(request, 'users/signup.html')

def register_applicant(request):
    """Register applicant only."""
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been created. Please login')
            return redirect('login')
        else:
            messages.warning(request, 'Something wenr wrong')
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_applicant.html', context)


def register_recruiter(request):
    """Register recruiter only."""
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your account has been created. Please login')
            return redirect('login')
        else:
            messages.warning(request, 'Something wenr wrong')
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_recruiter.html', context)



def login_user(request):
    """Login user."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong.')
            return redirect('login')
    else:
        return render(request, 'users/login.html')


def logout_user(request):
    """Logout user."""
    logout(request)
    messages.info(request, 'Your session has ended.')
    return redirect('login')