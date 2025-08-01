from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
import msal
import requests
from django.shortcuts import render
from .models import predict_sales



def register(request):
    if request.user.is_authenticated:
        return redirect('home')  

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, 'register.html')

        
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        messages.success(request, "User registered successfully. Please login.")
        return redirect('login')  

    return render(request, 'register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def predictions(request):
    return render(request, 'predictions.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def insights(request):
    return render(request, 'insights.html')

def contact(request):
    return render(request, 'contact')

from .models import Prediction

def predictions_view(request):
    prediction = None
    if request.method == "POST":
        product = request.POST.get("product")
        region = request.POST.get("region")
        date = request.POST.get("date")

        # call your prediction function
        prediction_value = predict_sales(product, region, date)

        # Save to database
        new_prediction = Prediction.objects.create(
            product=product,
            region=region,
            date=date,
            predicted_value=prediction_value
        )

        prediction = prediction_value

    return render(request, "predictions.html", {"prediction": prediction})


