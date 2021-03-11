from Master.formModels import CustomerFormModel, PortFormModel, UnitFormModel
from DataAccess.PWSRepo import pwsRepo

class mstBL:
    
    def InitialiseCustomerFormModel(CustomerID=None):
        form = CustomerFormModel()

        try:
            if CustomerID == None:
                form.initial['CustomerID'] = None
            else:
                Dto = pwsRepo.LoadCustomer(CustomerID)
                form.initial['CustomerID'] = Dto.ID
                form.initial['Name'] = Dto.Name
                form.initial['Pic'] = Dto.Pic 
                form.initial['MobileNo'] = Dto.MobileNo 
                form.initial['TelNo'] = Dto.TelNo
                form.initial['FaxNo'] = Dto.FaxNo 
                form.initial['Email'] = Dto.Email 
                form.initial['Address'] = Dto.Address 
                form.initial['City'] = Dto.City 
                form.initial['PostCode'] = Dto.PostCode 
                form.initial['StateID'] = Dto.State.ID
                form.initial['StateName'] = Dto.State.Name
                form.initial['CountryID'] = Dto.Country.ID
                form.initial['CountryName'] = Dto.Country.Name
                form.initial['TermID'] = Dto.Term.ID
                form.initial['TermName'] = Dto.Term.Name
                form.initial['LimitAmount'] = Dto.LimitAmount
                form.initial['IsAllowInvoice'] = Dto.IsAllowInvoice
                form.initial['IsAllowDo'] = Dto.IsAllowDo
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorCustomerFormModel(_Form):
        form = CustomerFormModel()
        
        try:
            form.initial['CustomerID'] = _Form['CustomerID']
            form.initial['Name'] = _Form['Name']
            form.initial['Pic'] = _Form['Pic']
            form.initial['MobileNo'] = _Form['MobileNo']
            form.initial['TelNo'] = _Form['TelNo']
            form.initial['FaxNo'] = _Form['FaxNo']
            form.initial['Email'] = _Form['Email']
            form.initial['Address'] = _Form['Address']
            form.initial['City'] = _Form['City'] 
            form.initial['PostCode'] = _Form['PostCode'] 
            form.initial['StateID'] = _Form['StateID']
            form.initial['StateName'] = _Form['StateName']
            form.initial['CountryID'] = _Form['CountryID']
            form.initial['CountryName'] = _Form['CountryName']
            form.initial['TermID'] = _Form['TermID']
            form.initial['TermName'] = _Form['TermName']
            form.initial['LimitAmount'] = _Form['LimitAmount']
            form.initial['IsAllowInvoice'] = _Form['IsAllowInvoice']
            form.initial['IsAllowDo'] = _Form['IsAllowDo']
        except Exception as e:
            print(e)
        
        return form

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

