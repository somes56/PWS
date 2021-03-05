from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from Login.models import Country, CountryForm

@csrf_exempt
def Login(request):
    SysBadMsg = ''

    if request.method == 'POST':
        return redirect('Login/Dashboard')
    else:
        return render(request, 'Login.html', { 'SysBadMsg' : SysBadMsg })

def Dashboard(request):
    return render(request, 'Dashboard.html')
