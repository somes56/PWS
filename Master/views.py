from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.utils import timezone
from BusinessLogic.MasterBL import mstBL
from DataAccess.PWSRepo import pwsRepo
from Master.formModels import CustomerFormModel
from Master.models import Country, Customer, State, Term

def CustomerList(request):
    return render(request, 'Customer.html')

def PartialCustomerList(request, SearchBy=''):
    Customers = []
    Customers = pwsRepo.PartialCustomerList(SearchBy)

    Page = request.GET.get('page', 1)
    _Paginator = Paginator(Customers, 5)
    
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
            customerFormModel.initial['CustomerID'] = None
        else:
            CustomerDto = pwsRepo.LoadCustomer(CustomerID)
            customerFormModel.initial['CustomerID'] = CustomerDto.ID
            customerFormModel.initial['Name'] = CustomerDto.Name
            customerFormModel.initial['Pic'] = CustomerDto.Pic 
            customerFormModel.initial['MobileNo'] = CustomerDto.MobileNo 
            customerFormModel.initial['TelNo'] = CustomerDto.TelNo
            customerFormModel.initial['FaxNo'] = CustomerDto.FaxNo 
            customerFormModel.initial['Email'] = CustomerDto.Email 
            customerFormModel.initial['Address'] = CustomerDto.Address 
            customerFormModel.initial['City'] = CustomerDto.City 
            customerFormModel.initial['PostCode'] = CustomerDto.PostCode 
            customerFormModel.initial['StateID'] = CustomerDto.State.ID
            customerFormModel.initial['StateName'] = CustomerDto.State.Name
            customerFormModel.initial['CountryID'] = CustomerDto.Country.ID
            customerFormModel.initial['CountryName'] = CustomerDto.Country.Name
            customerFormModel.initial['TermID'] = CustomerDto.Term.ID
            customerFormModel.initial['TermName'] = CustomerDto.Term.Name
            customerFormModel.initial['LimitAmount'] = CustomerDto.LimitAmount
            customerFormModel.initial['IsAllowInvoice'] = CustomerDto.IsAllowInvoice
            customerFormModel.initial['IsAllowDo'] = CustomerDto.IsAllowDo
            
        return render(request, 'CustomerForm.html', { 'SysGoodMsg' : SysGoodMsg, 'SysBadMsg' : SysBadMsg,  'Form' : customerFormModel })

    else:
        IsUpdate = False
        UpsertResult = {}
        newCustomerFormModel = CustomerFormModel()
        customerFormModel = CustomerFormModel(request.POST)

        if customerFormModel.is_valid():
            _Form = customerFormModel.cleaned_data
            UpsertResult = pwsRepo.UpsertCustomer(_Form)
            
            if _Form['CustomerID'] != None:
                IsUpdate = True

            if UpsertResult['rtn'] == True:

                CustomerDto = pwsRepo.LoadCustomer(UpsertResult['CustomerID'])
                newCustomerFormModel.initial['CustomerID'] = CustomerDto.ID
                newCustomerFormModel.initial['Name'] = CustomerDto.Name
                newCustomerFormModel.initial['Pic'] = CustomerDto.Pic 
                newCustomerFormModel.initial['MobileNo'] = CustomerDto.MobileNo 
                newCustomerFormModel.initial['TelNo'] = CustomerDto.TelNo
                newCustomerFormModel.initial['FaxNo'] = CustomerDto.FaxNo 
                newCustomerFormModel.initial['Email'] = CustomerDto.Email 
                newCustomerFormModel.initial['Address'] = CustomerDto.Address 
                newCustomerFormModel.initial['City'] = CustomerDto.City 
                newCustomerFormModel.initial['PostCode'] = CustomerDto.PostCode 
                newCustomerFormModel.initial['StateID'] = CustomerDto.State.ID
                newCustomerFormModel.initial['StateName'] = CustomerDto.State.Name
                newCustomerFormModel.initial['CountryID'] = CustomerDto.Country.ID
                newCustomerFormModel.initial['CountryName'] = CustomerDto.Country.Name
                newCustomerFormModel.initial['TermID'] = CustomerDto.Term.ID
                newCustomerFormModel.initial['TermName'] = CustomerDto.Term.Name
                newCustomerFormModel.initial['LimitAmount'] = CustomerDto.LimitAmount
                newCustomerFormModel.initial['IsAllowInvoice'] = CustomerDto.IsAllowInvoice
                newCustomerFormModel.initial['IsAllowDo'] = CustomerDto.IsAllowDo

                if IsUpdate == False:
                    SysGoodMsg = 'Inserted Successfully'
                else:
                    SysGoodMsg = 'Updated Successfully'

            else:
                
                newCustomerFormModel.initial['CustomerID'] = _Form['CustomerID']
                newCustomerFormModel.initial['Name'] = _Form['Name']
                newCustomerFormModel.initial['Pic'] = _Form['Pic']
                newCustomerFormModel.initial['MobileNo'] = _Form['MobileNo']
                newCustomerFormModel.initial['TelNo'] = _Form['TelNo']
                newCustomerFormModel.initial['FaxNo'] = _Form['FaxNo']
                newCustomerFormModel.initial['Email'] = _Form['Email']
                newCustomerFormModel.initial['Address'] = _Form['Address']
                newCustomerFormModel.initial['City'] = _Form['City'] 
                newCustomerFormModel.initial['PostCode'] = _Form['PostCode'] 
                newCustomerFormModel.initial['StateID'] = _Form['StateID']
                newCustomerFormModel.initial['StateName'] = _Form['StateName']
                newCustomerFormModel.initial['CountryID'] = _Form['CountryID']
                newCustomerFormModel.initial['CountryName'] = _Form['CountryName']
                newCustomerFormModel.initial['TermID'] = _Form['TermID']
                newCustomerFormModel.initial['TermName'] = _Form['TermName']
                newCustomerFormModel.initial['LimitAmount'] = _Form['LimitAmount']
                newCustomerFormModel.initial['IsAllowInvoice'] = _Form['IsAllowInvoice']
                newCustomerFormModel.initial['IsAllowDo'] = _Form['IsAllowDo']

                if IsUpdate == False:
                    SysBadMsg = 'Insert Fail'
                else:
                    SysBadMsg = 'Update Fail'

        else:
            SysBadMsg = 'Invalid Input'

        return render(request, 'CustomerForm.html', { 'SysGoodMsg' : SysGoodMsg, 'SysBadMsg' : SysBadMsg,  'Form' : newCustomerFormModel })

@csrf_exempt
def DeleteCustomer(request, CustomerID=None):
    rtn = False

    if request.method == 'POST':
        rtn = pwsRepo.DeleteCustomer(CustomerID)
    else:
        rtn = False
    return HttpResponse(rtn)

def UpsertCountry(request):
    rtn = False
    rtn = pwsRepo.UpsertCountry()
    return HttpResponse(rtn)

