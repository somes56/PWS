from django.shortcuts import render, HttpResponse
from BusinessLogic.MasterBL import mstBL
from DataAccess.PWSRepo import pwsRepo

def Customer(request):
    return render(request, 'Customer.html')

def UpsertMstCountry(request):
    rtn = False
    rtn = pwsRepo.UpsertMstCountry()
    return HttpResponse(rtn)

