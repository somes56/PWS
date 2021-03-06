from Master.models import Country
from datetime import datetime
from django.utils import timezone
import requests

class pwsRepo:

    def UpsertMstCountry():
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