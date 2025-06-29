from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserSignupForm, ProfileForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserSignupForm()
        profile_form = ProfileForm()
    return render(request, 'users/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.profile.user_type == 'doctor':
                return redirect('dashboard_doctor')
            else:
                return redirect('dashboard_patient')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

@login_required
def dashboard_doctor(request):
    return render(request, 'users/dashboard_doctor.html', {'user': request.user})

@login_required
def dashboard_patient(request):
    return render(request, 'users/dashboard_patient.html', {'user': request.user})
