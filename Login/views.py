from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from Login.models import Country, CountryForm

@csrf_exempt
def Login(request):
    if request.method == 'POST':
        return redirect('Login')
    else:
        countryForm = CountryForm()
        return render(request, 'Login.html', { 'countryForm' : countryForm })

