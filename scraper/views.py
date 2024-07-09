from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product,Review,Wishlist,Images, Prices
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from datetime import datetime,timedelta
from decimal import Decimal
from django.contrib.auth.hashers import make_password
from datetime import datetime
from .scraping import ScrapeFL
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from itertools import zip_longest

def welcome(request):
    if request.method == 'POST':
        action = request.POST.get('')
        if action == 'signup':
            return redirect('signup')
        elif action == 'login':
            return redirect('login')
    return render(request, 'welcome.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists() :
           return render(request, 'signup.html', {'error_message': 'Username '})

        new_user = User.objects.create(username=username, email=email)
        hashed_password = make_password(password)

        new_user.password = hashed_password
        new_user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

        return redirect('home')  # Redirect to the desired page after signup (e.g., home page)

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        print("Request method is POST") 
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user with the provided username and password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If authentication is successful, log in the user
            login(request, user)
            return redirect('home')  
        else:
            # If authentication fails, render the login page again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password\n try again'})
    
    # If the request method is not POST, render the login page
    return render(request, 'login.html')


def reset(request):
    return render(request, 'reset.html')

@login_required
def home(request):
    scraper=ScrapeFL()
    if request.method == "POST":
        search_text = request.POST.get('search')
        if search_text:
            # Scrape the product from the website
            search_result=str(search_text)
            scraper.scrapeProduct(search_result)
            
        return redirect('search')
        
    return render(request, 'home.html')


@login_required
def search(request):
    products=[]
    product_list = Product.objects.all().order_by('predicted_rating').reverse()[:24]
    for product in product_list:
        prod_ID=product.PID
        prod_name=product.title
        # Get the product image
        product_image = [product_images.image1 for product_images in Images.objects.filter(product=prod_ID)]
        # Get the product price
        product_price = [product_prices.price for product_prices in Images.objects.filter(product=prod_ID)]
        # Update product in products
        product_dic={PID:prod_ID,name:prod_name,image:product_image,price:product_price}
        products.append(product_dic)
    return render(request, 'search.html', {'products': products})

@login_required
def logout_view(request):
    logout(request)
    return redirect('welcome')

@login_required
def product(request):
    return render(request, 'product.html')

@login_required
def wishlist(request):
    return render(request, 'wishlist.html')