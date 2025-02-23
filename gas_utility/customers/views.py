from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomerSignupForm

def signup(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomerSignupForm()
    return render(request, 'customers/signup.html', {'form': form})

from django.shortcuts import render

def home(request):
    return render(request, 'customers/home.html')

