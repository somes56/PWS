from Master.formModels import PortFormModel, UnitFormModel
from DataAccess.PWSRepo import pwsRepo

class mstBL:

    def InitialisePortFormModel(PortID=None):
        form = PortFormModel()

        try:
            if PortID == None:
                form.initial['PortID'] = None
            else:
                Dto = pwsRepo.LoadPort(PortID)
                form.initial['PortID'] = Dto.ID
                form.initial['Code'] = Dto.Code
                form.initial['Name'] = Dto.Name
                form.initial['CountryID'] = Dto.Country.ID
                form.initial['CountryName'] = Dto.Country.Name
                form.initial['IsSpecial'] = Dto.IsSpecial
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorPortFormModel(_Form):
        form = PortFormModel()

        try:
            form.initial['PortID'] = _Form['PortID']
            form.initial['Code'] = _Form['Code']
            form.initial['Name'] = _Form['Name']
            form.initial['CountryID'] = _Form['CountryID']
            form.initial['CountryName'] = _Form['CountryName']
            form.initial['IsSpecial'] = _Form['IsSpecial']
        except Exception as e:
            print(e)
        
        return form

    def InitialiseUnitFormModel(UnitID=None):
        form = UnitFormModel()

        try:
            if UnitID == None:
                form.initial['UnitID'] = None
            else:
                Dto = pwsRepo.LoadUnit(UnitID)
                form.initial['UnitID'] = Dto.ID
                form.initial['Code'] = Dto.Code
                form.initial['ShortName'] = Dto.ShortName
                form.initial['FullName'] = Dto.FullName
        except Exception as e:
            print(e)

        return form
        
    def InitialiseErrorUnitFormModel(_Form):
        form = UnitFormModel()

        try:
            form.initial['UnitID'] = _Form['UnitID']
            form.initial['Code'] = _Form['Code']
            form.initial['ShortName'] = _Form['ShortName']
            form.initial['ShortName'] = _Form['ShortName']
        except Exception as e:
            print(e)
        
        return form

