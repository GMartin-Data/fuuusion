import json
import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from .forms import CryptoApiForm, FlowerFeaturesForm


@login_required
def predict_api_page(request):
    url = "http://localhost:8000/predict"
    session = Session()

    # If this is a POST request we need to process the form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = FlowerFeaturesForm(request.POST)
        # Check whether it's valid or not
        if form.is_valid():
            form.save()
            payload= json.dumps(form.cleaned_data)
            try:
                json_response = session.post(url, data=payload).json()
                print(json_response)
                return render(request, "main/predict_api_page.html",
                              context={"form": form, "data": json_response})
            except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
                return render(request, "main/predict_api_page.html",
                            context={"form": form, "error": f"{type(e)}: {e}"})
    else:
        form = FlowerFeaturesForm()
    return render(request, "main/predict_api_page.html", context={"form": form})

@login_required
def api_page(request):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv("API_KEY"),
    }

    session = Session()
    session.headers.update(headers)

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CryptoApiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            params_dict = form.cleaned_data
            try:
                json_response = session.get(url, params=params_dict).json()
                devise = params_dict["convert"]
                id_ = list(json_response["data"].keys())[0]
                data = json_response["data"][id_]["quote"][devise]
                return render(request, "main/api_page.html", context={"form": form, "data": data})
            except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
                return render(request, "main/api_page.html", context={"form": form, "error": f"{type(e)}: {e}"})
            
            
    else:
        form = CryptoApiForm()
    return render(request, "main/api_page.html", context={"form": form})
    

# Create your views here.
def home_page(request):
    return render(request, 'main/home_page.html')

def about_page(request):
    return render(request, 'main/about_page.html')

def contact_page(request, test):
    context = {'test': test}
    return render(request, 'main/contact_page.html', context=context)

@login_required
def special_page(request):
    return render(request, "main/special_page.html")
