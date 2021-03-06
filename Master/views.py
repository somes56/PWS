from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from BusinessLogic.MasterBL import mstBL
from DataAccess.PWSRepo import pwsRepo
from Master.formModels import CustomerFormModel
from Master.models import Country

def Customer(request):
    return render(request, 'Customer.html')

@csrf_exempt
def CustomerForm(request):
    SysGoodMsg = ''
    SysBadMsg = ''

    if request.method == 'GET' : 
        customerFormModel = CustomerFormModel()
        return render(request, 'CustomerForm.html', { 'SysGoodMsg' : SysGoodMsg, 'SysBadMsg' : SysBadMsg,  'Form' : customerFormModel })
    else:
        customerFormModel = CustomerFormModel(request.POST)
        if customerFormModel.is_valid():
            c = customerFormModel.cleaned_data
        return HttpResponse('ok')

def UpsertCountry(request):
    rtn = False
    rtn = pwsRepo.UpsertCountry()
    return HttpResponse(rtn)

