import yfinance as yf
import pandas as pd
from tldr_python import TLDR
from core.models import Stock
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth.decorators import login_required


stock_map = {
}
def home(request):
    stocks = Stock.objects.all()
    tldr = TLDR("ca311ddc08msh3530fb8fa9aa773p178701jsne53b8b9a2d65")
    if request.method == 'POST':
        stock = request.POST['stock']

        # If the stock is already in the map, then just use that data
        if stock in stock_map:
            data = stock_map[stock]['data']
            return render(request, "home/home.html", data)
        
        ticker = yf.Ticker(stock)

        # Find summaries for each news article
        summaries = []
        for news in ticker.news:
            summaries.append(tldr.summarize(news['link'], max_sentences=2).text)
            
        # Save the stock data
        data = {
            "news":ticker.news,  
            "summary": summaries,
            "stocknames": stocks
        }
        save_stock(stock, data)
    else:
        data={"stocknames":stocks}
    
    return render(request, "home/home.html", data)


def save_stock(stock, data):
    # Make things faster by saving the stock data
    stock_map[stock] = {
        "data": data
    }



def help(request):
    return render(request, "help/help.html", {})


def logout_view(request):
    logout(request)
    return redirect("/login/")


def signup(request):
    print("signuped")
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'signup/signup.html', {'form': form})


@login_required()
def profile(request):
    return render(request, "profile/profile.html", {})


def favorites(request):
    return render(request, 'profile/favorites.html', {})