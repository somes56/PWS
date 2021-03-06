from Master.models import Country, State, Term
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