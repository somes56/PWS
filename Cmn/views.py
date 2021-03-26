from django.shortcuts import render
from DataAccess.MasterRepo import masterRepo


def AdvSearchState(request, SearchBy=""):
    States = []
    States = masterRepo.AdvSearchState(SearchBy)
    return render(request, "PartialAdvSearchState.html", {"States": States})


def AdvSearchCountry(request, SearchBy=""):
    Countries = []
    Countries = masterRepo.AdvSearchCountry(SearchBy)
    return render(request, "PartialAdvSearchCountry.html", {"Countries": Countries})


def AdvSearchTerm(request, SearchBy=""):
    Terms = []
    Terms = masterRepo.AdvSearchTerm(SearchBy)
    return render(request, "PartialAdvSearchTerm.html", {"Terms": Terms})


def AdvSearchCustomer(request, SearchBy=""):
    Customers = []
    Customers = masterRepo.AdvSearchCustomer(SearchBy)
    return render(request, "PartialAdvSearchCustomer.html", {"Customers": Customers})


def AdvSearchVessel(request, SearchBy=""):
    Vessels = []
    Vessels = masterRepo.AdvSearchVessel(SearchBy)
    return render(request, "PartialAdvSearchVessel.html", {"Vessels": Vessels})
