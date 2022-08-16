# views.py
import requests
from django.shortcuts import render


def home(request):
    url = "https://api.stagingeb.com/v1/properties?"
    headers = {
        'X-Authorization': "l7u502p8v46ba3ppgvj5y2aad50lb9",
    }
    params = {
        'page': '1',
        'limit': '20',
        'search[statuses][]': '-',
    }
    response = requests.get(url, headers=headers, params=params) # enviamos headers y params
    todos = response.json()
    print(todos)
    return render(request, "main_app/home.html", {"todos": todos})   





