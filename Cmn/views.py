from django.http.response import HttpResponse
from django.core import serializers
from django.shortcuts import render
from DataAccess.MasterRepo import masterRepo
from DataAccess.ImportRepo import importRepo


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


def AdvSearchVoyage(request, SearchBy=""):
    Voyages = []
    Voyages = masterRepo.AdvSearchVoyage(SearchBy)
    return render(request, "PartialAdvSearchVoyage.html", {"Voyages": Voyages})


def AdvSearchPort(request, SearchBy=""):
    Ports = []
    Ports = masterRepo.AdvSearchPort(SearchBy)
    return render(request, "PartialAdvSearchPort.html", {"Ports": Ports})


def AdvSearchContainerSize(request, SearchBy=""):
    ContainerSizes = []
    ContainerSizes = masterRepo.AdvSearchContainerSize(SearchBy)
    return render(
        request,
        "PartialAdvSearchContainerSize.html",
        {"ContainerSizes": ContainerSizes},
    )


def AdvSearchClass(request, SearchBy=""):
    Classes = []
    Classes = masterRepo.AdvSearchClass(SearchBy)
    return render(request, "PartialAdvSearchClass.html", {"Classes": Classes})


def AdvSearchUnit(request, SearchBy=""):
    Units = []
    Units = masterRepo.AdvSearchUnit(SearchBy)
    return render(request, "PartialAdvSearchUnit.html", {"Units": Units})


def AdvSearchObl(request, SearchBy=""):
    Obls = []
    Obls = importRepo.AdvSearchObl(SearchBy)
    return render(request, "PartialAdvSearchObl.html", {"Obls": Obls})


def AdvSearchContainerByObl(request, OblID=None, SearchBy=""):
    Containers = []
    Containers = importRepo.AdvSearchContainerByObl(OblID, SearchBy)
    return render(
        request, "PartialAdvSearchContainerByObl.html", {"Containers": Containers}
    )


def AdvSearchHblByContainer(request, ContainerID=None, SearchBy=""):
    Hbls = []
    Hbls = importRepo.AdvSearchHblByContainer(ContainerID, SearchBy)
    return render(request, "PartialAdvSearchHblByContainer.html", {"Hbls": Hbls})


def AdvSearchHblHist(request, SearchBy=""):
    Hbls = []
    Hbls = importRepo.AdvSearchHblHist(SearchBy)
    return render(request, "PartialAdvSearchHblHist.html", {"Hbls": Hbls})


def AdvSearchItem(request, SearchBy=""):
    Items = []
    Items = masterRepo.AdvSearchItem(SearchBy)
    return render(request, "PartialAdvSearchItem.html", {"Items": Items})


def AdvSearchCreditInvoice(request, SearchBy=""):
    Invoices = []
    Invoices = importRepo.AdvSearchCreditInvoice(SearchBy)
    return render(request, "PartialAdvSearchCreditInvoice.html", {"Invoices": Invoices})


def DefaultItemByAccountTypeCode(request, AccountType, Code):
    DefaultItems = []

    DefaultItems = masterRepo.AdvSearchDefaultItemByAccountTypeCode(AccountType, Code)

    rtn = serializers.serialize("json", DefaultItems)

    return HttpResponse(rtn, content_type="application/json")