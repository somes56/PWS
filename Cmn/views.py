from django.shortcuts import render
from DataAccess.PWSRepo import pwsRepo

def AdvSearchState(request, SearchBy=''):
    States = []
    States = pwsRepo.AdvSearchState(SearchBy)
    return render(request, 'PartialAdvSearchState.html', { 'States' : States })

def AdvSearchCountry(request, SearchBy=''):
    Countries = []
    Countries = pwsRepo.AdvSearchCountry(SearchBy)
    return render(request, 'PartialAdvSearchCountry.html', { 'Countries' : Countries })

def AdvSearchTerm(request, SearchBy=''):
    Terms = []
    Terms = pwsRepo.AdvSearchTerm(SearchBy)
    return render(request, 'PartialAdvSearchTerm.html', { 'Terms' : Terms })

def AdvSearchCustomer(request, SearchBy=''):
    Customers = []
    Customers = pwsRepo.AdvSearchCustomer(SearchBy)
    return render(request, 'PartialAdvSearchCustomer.html', { 'Customers' : Customers })

def AdvSearchVessel(request, SearchBy=''):
    Vessels = []
    Vessels = pwsRepo.AdvSearchVessel(SearchBy)
    return render(request, 'PartialAdvSearchVessel.html', { 'Vessels' : Vessels })

