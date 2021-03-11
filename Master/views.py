from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.utils import timezone
from BusinessLogic.MasterBL import mstBL
from DataAccess.PWSRepo import pwsRepo
from Master.formModels import CustomerFormModel, PortFormModel, UnitFormModel
from Master.models import Country, Customer, State, Term

def CustomerList(request):
    return render(request, 'Customer.html')

def PartialCustomerList(request, SearchBy=''):
    Customers = []
    Customers = pwsRepo.PartialCustomerList(SearchBy)

    Page = request.GET.get('page', 1)
    _Paginator = Paginator(Customers, 50)
    
    try:
        CustomerPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        CustomerPaginator = _Paginator.page(1)
    except EmptyPage:
        CustomerPaginator = _Paginator.page(paginator.num_pages)

    return render(request, 'PartialCustomerList.html', { 'Customers' : CustomerPaginator })

@csrf_exempt
def CustomerForm(request, CustomerID=None):
    SysGoodMsg = ''
    SysBadMsg = ''

    if request.method == 'GET' : 
        customerFormModel = CustomerFormModel()
        
        if CustomerID == None:
            customerFormModel = mstBL.InitialiseCustomerFormModel(None)
        else:
            customerFormModel = mstBL.InitialiseCustomerFormModel(CustomerID)
            
        return render(request, 'CustomerForm.html', { 'SysGoodMsg' : SysGoodMsg, 'SysBadMsg' : SysBadMsg,  'Form' : customerFormModel })

    else:
        IsUpdate = False
        UpsertResult = {}
        customerFormModel = CustomerFormModel()
        _post = CustomerFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertCustomer(_Form)
            
            if _Form['CustomerID'] != None:
                IsUpdate = True

            if UpsertResult['rtn'] == True:
                customerFormModel = mstBL.InitialiseCustomerFormModel(UpsertResult['CustomerID'])

                if IsUpdate == False:
                    SysGoodMsg = 'Inserted Successfully'
                else:
                    SysGoodMsg = 'Updated Successfully'

            else:
                customerFormModel = mstBL.InitialiseErrorCustomerFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = 'Insert Fail'
                else:
                    SysBadMsg = 'Update Fail'

        else:
            SysBadMsg = 'Invalid Input'

        return render(request, 'CustomerForm.html', { 'SysGoodMsg' : SysGoodMsg, 'SysBadMsg' : SysBadMsg,  'Form' : customerFormModel })

@csrf_exempt
def DeleteCustomer(request, CustomerID=None):
    rtn = False

    if request.method == 'POST':
        rtn = pwsRepo.DeleteCustomer(CustomerID)
    else:
        rtn = False
    return HttpResponse(rtn)

def PortList(request):
    return render(request, 'Port.html')
    
def PartialPortList(request, SearchBy=''):
    Ports = []
    Ports = pwsRepo.PartialPortList(SearchBy)

    Page = request.GET.get('page', 1)
    _Paginator = Paginator(Ports, 50)
    
    try:
        PortPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        PortPaginator = _Paginator.page(1)
    except EmptyPage:
        PortPaginator = _Paginator.page(paginator.num_pages)

    return render(request, 'PartialPortList.html', { 'Ports' : PortPaginator })
    
@csrf_exempt
def PortForm(request, PortID=None):
    SysGoodMsg = ''
    SysBadMsg = ''
    
    if request.method == 'GET' : 
        portFormModel = PortFormModel()
        
        if PortID == None:
            portFormModel = mstBL.InitialisePortFormModel(None)
        else:
            portFormModel = mstBL.InitialisePortFormModel(PortID)
            
        return render(request, 'PortForm.html', { 'SysGoodMsg' : SysGoodMsg, 'SysBadMsg' : SysBadMsg,  'Form' : portFormModel })
    
    else:
        IsUpdate = False
        UpsertResult = {}
        portFormModel = PortFormModel()
        _post = PortFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertPort(_Form)
            
            if _Form['PortID'] != None:
                IsUpdate = True

            if UpsertResult['rtn'] == True:
                portFormModel = mstBL.InitialisePortFormModel(UpsertResult['PortID'])
                
                if IsUpdate == False:
                    SysGoodMsg = 'Inserted Successfully'
                else:
                    SysGoodMsg = 'Updated Successfully'

            else:
                portFormModel = mstBL.InitialiseErrorPortFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = 'Insert Fail'
                else:
                    SysBadMsg = 'Update Fail'

        else:
            SysBadMsg = 'Invalid Input'

        return render(request, 'PortForm.html', { 'SysGoodMsg' : SysGoodMsg, 'SysBadMsg' : SysBadMsg,  'Form' : portFormModel })

@csrf_exempt
def DeletePort(request, PortID=None):
    rtn = False

    if request.method == 'POST':
        rtn = pwsRepo.DeletePort(PortID)
    else:
        rtn = False
    return HttpResponse(rtn)


def UnitList(request):
    return render(request, 'Unit.html')
    
def PartialUnitList(request, SearchBy=''):
    Units = []
    Units = pwsRepo.PartialUnitList(SearchBy)

    Page = request.GET.get('page', 1)
    _Paginator = Paginator(Units, 50)
    
    try:
        UnitPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        UnitPaginator = _Paginator.page(1)
    except EmptyPage:
        UnitPaginator = _Paginator.page(paginator.num_pages)

    return render(request, 'PartialUnitList.html', { 'Units' : UnitPaginator })
    
@csrf_exempt
def UnitForm(request, UnitID=None):
    SysGoodMsg = ''
    SysBadMsg = ''
    
    if request.method == 'GET' : 
        unitFormModel = UnitFormModel()
        
        if UnitID == None:
            unitFormModel = mstBL.InitialiseUnitFormModel(None)
        else:
            unitFormModel = mstBL.InitialiseUnitFormModel(UnitID)
            
        return render(request, 'UnitForm.html', { 'SysGoodMsg' : SysGoodMsg, 'SysBadMsg' : SysBadMsg,  'Form' : unitFormModel })
    
    else:
        IsUpdate = False
        UpsertResult = {}
        unitFormModel = UnitFormModel()
        _post = UnitFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertUnit(_Form)
            
            if _Form['UnitID'] != None:
                IsUpdate = True

            if UpsertResult['rtn'] == True:
                unitFormModel = mstBL.InitialiseUnitFormModel(UpsertResult['UnitID'])
                
                if IsUpdate == False:
                    SysGoodMsg = 'Inserted Successfully'
                else:
                    SysGoodMsg = 'Updated Successfully'

            else:
                unitFormModel = mstBL.InitialiseErrorUnitFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = 'Insert Fail'
                else:
                    SysBadMsg = 'Update Fail'

        else:
            SysBadMsg = 'Invalid Input'

        return render(request, 'UnitForm.html', { 'SysGoodMsg' : SysGoodMsg, 'SysBadMsg' : SysBadMsg,  'Form' : unitFormModel })

@csrf_exempt
def DeleteUnit(request, UnitID=None):
    rtn = False

    if request.method == 'POST':
        rtn = pwsRepo.DeleteUnit(UnitID)
    else:
        rtn = False
    return HttpResponse(rtn)

def UpsertCountry(request):
    rtn = False
    rtn = pwsRepo.UpsertCountry()
    return HttpResponse(rtn)

