from Master.models import Country, State, Term, Customer
from datetime import datetime
from django.db.models import Q
from django.utils import timezone
import requests

class pwsRepo:

    def AdvSearchState(SearchBy=''):
        States = []

        try:
            States = State.objects.filter(IsActive=True, Name__icontains=SearchBy).order_by('Name')
        except Exception as e:
            States = []
            print(e)

        return States
        
    def AdvSearchCountry(SearchBy=''):
        Countries = []

        try:
            Countries = Country.objects.filter(Q(Name__icontains=SearchBy) | Q(IsoCode__icontains=SearchBy), IsActive=True).order_by('Name')
        except Exception as e:
            Countries = []
            print(e)

        return Countries
        
    def AdvSearchTerm(SearchBy=''):
        Terms = []

        try:
            Terms = Term.objects.filter(IsActive=True, Name__icontains=SearchBy).order_by('Name')
        except Exception as e:
            Terms = []
            print(e)

        return Terms

    def PartialCustomerList(SearchBy=''):
        Customers = []

        try:
            Customers = Customer.objects.filter(IsActive=True, Name__icontains=SearchBy)
        except Exception as e:
            Customers = []
            print(e)

        return Customers

    def LoadCustomer(CustomerID):
        CustomerDto = Customer()

        try:
            CustomerDto = Customer.objects.get(ID=CustomerID, IsActive=True)
        except Exception as e:
            CustomerDto = Customer();
            print(e)
        
        return CustomerDto


    def UpsertCountry():
        rtn = False
        insert = 0

        try:
            Record = Country.objects.all().count()

            if Record == 0:
                res = requests.get('https://countrycode.org/api/countryCode/countryMenu')
                Countries = res.json()

                for country in Countries:
                    c = Country.objects.create(Name=country['name'], IsoCode=str(country['code']).upper(), IsActive=True, CreateDate= datetime.now(tz=timezone.utc), 
                    CreateBy=None, UpdateDate=datetime.now(tz=timezone.utc), UpdateBy=None)

                    if(c.ID):
                        insert += 1

                if (len(Countries) == insert):
                    rtn = True
                    
            else:
                rtn = True

        except Exception as e:
            rtn = False
            print(e)
            
        return rtn
    
    def UpsertCustomer(Dto):
        rtn = False
        CustomerID = None
        StateDto = None
        CountryDto = None
        TermDto = None
        UpsertDto = None
        
        try:
            StateDto = State.objects.get(ID=Dto['StateID'])
            CountryDto = Country.objects.get(ID=Dto['CountryID'])
            TermDto = Term.objects.get(ID=Dto['TermID'])
            
            if Dto['CustomerID'] == None:
                
                UpsertDto = Customer.objects.create(Name=Dto['Name'], Pic=Dto['Pic'], MobileNo=Dto['MobileNo'], TelNo=Dto['TelNo'],
                            FaxNo=Dto['FaxNo'], Email=Dto['Email'], Address=Dto['Address'], City=Dto['City'], PostCode=Dto['PostCode'],
                            State=StateDto, Country=CountryDto, Term=TermDto, LimitAmount=Dto['LimitAmount'], IsAllowInvoice=Dto['IsAllowInvoice'],
                            IsAllowDo=Dto['IsAllowDo'], IsActive=True, CreateDate=datetime.now(tz=timezone.utc), CreateBy=None,
                            UpdateDate=datetime.now(tz=timezone.utc), UpdateBy=None)
                
                if UpsertDto.ID:
                    rtn = True
                    CustomerID = UpsertDto.ID

            else:
                UpsertDto = Customer.objects.get(ID=Dto['CustomerID'])
                UpsertDto.Name = Dto['Name']
                UpsertDto.Pic = Dto['Pic']
                UpsertDto.MobileNo = Dto['MobileNo']
                UpsertDto.TelNo = Dto['TelNo']
                UpsertDto.FaxNo = Dto['FaxNo']
                UpsertDto.Email = Dto['Email']
                UpsertDto.Address = Dto['Address']
                UpsertDto.City = Dto['City']
                UpsertDto.PostCode = Dto['PostCode']
                UpsertDto.State = StateDto
                UpsertDto.Country = CountryDto
                UpsertDto.Term = TermDto
                UpsertDto.LimitAmount = Dto['LimitAmount']
                UpsertDto.IsAllowInvoice = Dto['IsAllowInvoice']
                UpsertDto.IsAllowDo = Dto['IsAllowDo']
                UpsertDto.IsActive = True
                UpsertDto.UpdateDate = datetime.now(tz=timezone.utc) 
                UpsertDto.UpdateBy = None
                UpsertDto.save()
                rtn = True
                CustomerID = Dto['CustomerID']
                        
        except Exception as e:
            print(e)
        
        return { 'rtn' : rtn, 'CustomerID' : CustomerID }
    
    def DeleteCustomer(CustomerID):
        rtn = False

        try:
            CustomerDto = Customer.objects.get(ID=CustomerID)
            CustomerDto.IsActive = False
            CustomerDto.UpdateDate = datetime.now(tz=timezone.utc) 
            CustomerDto.UpdateBy = None
            CustomerDto.save()
            rtn = True
        except Exception as e:
            print(e)
        
        return rtn
            