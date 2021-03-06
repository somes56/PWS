from Master.formModels import (
    CustomerFormModel,
    PortFormModel,
    UnitFormModel,
    ContainerSizeFormModel,
    VesselFormModel,
    ItemFormModel,
    ClassFormModel,
    VoyageFormModel,
    OperatorFormModel,
)
from datetime import datetime
from django.utils import timezone
from DataAccess.MasterRepo import masterRepo


class mstBL:
    def InitialiseCustomerFormModel(CustomerID=None):
        form = CustomerFormModel()

        try:
            if CustomerID == None:
                form.initial["CustomerID"] = None
            else:
                Dto = masterRepo.LoadCustomer(CustomerID)
                form.initial["CustomerID"] = Dto.ID
                form.initial["Name"] = Dto.Name
                form.initial["Pic"] = Dto.Pic
                form.initial["MobileNo"] = Dto.MobileNo
                form.initial["TelNo"] = Dto.TelNo
                form.initial["FaxNo"] = Dto.FaxNo
                form.initial["Email"] = Dto.Email
                form.initial["Address"] = Dto.Address
                form.initial["City"] = Dto.City
                form.initial["PostCode"] = Dto.PostCode
                form.initial["StateID"] = None if Dto.State == None else Dto.State.ID
                form.initial["StateName"] = "" if Dto.State == None else Dto.State.Name
                form.initial["CountryID"] = (
                    None if Dto.Country == None else Dto.Country.ID
                )
                form.initial["CountryName"] = (
                    "" if Dto.Country == None else Dto.Country.Name
                )
                form.initial["TermID"] = None if Dto.Term == None else Dto.Term.ID
                form.initial["TermName"] = "" if Dto.Term == None else Dto.Term.Name
                form.initial["LimitAmount"] = Dto.LimitAmount
                form.initial["IsAllowInvoice"] = Dto.IsAllowInvoice
                form.initial["IsAllowDo"] = Dto.IsAllowDo
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorCustomerFormModel(_Form):
        form = CustomerFormModel()

        try:
            form.initial["CustomerID"] = _Form["CustomerID"]
            form.initial["Name"] = _Form["Name"]
            form.initial["Pic"] = _Form["Pic"]
            form.initial["MobileNo"] = _Form["MobileNo"]
            form.initial["TelNo"] = _Form["TelNo"]
            form.initial["FaxNo"] = _Form["FaxNo"]
            form.initial["Email"] = _Form["Email"]
            form.initial["Address"] = _Form["Address"]
            form.initial["City"] = _Form["City"]
            form.initial["PostCode"] = _Form["PostCode"]
            form.initial["StateID"] = _Form["StateID"]
            form.initial["StateName"] = _Form["StateName"]
            form.initial["CountryID"] = _Form["CountryID"]
            form.initial["CountryName"] = _Form["CountryName"]
            form.initial["TermID"] = _Form["TermID"]
            form.initial["TermName"] = _Form["TermName"]
            form.initial["LimitAmount"] = _Form["LimitAmount"]
            form.initial["IsAllowInvoice"] = _Form["IsAllowInvoice"]
            form.initial["IsAllowDo"] = _Form["IsAllowDo"]
        except Exception as e:
            print(e)

        return form

    def InitialisePortFormModel(PortID=None):
        form = PortFormModel()

        try:
            if PortID == None:
                form.initial["PortID"] = None
            else:
                Dto = masterRepo.LoadPort(PortID)
                form.initial["PortID"] = Dto.ID
                form.initial["Code"] = Dto.Code
                form.initial["Name"] = Dto.Name
                form.initial["CountryID"] = (
                    None if Dto.Country == None else Dto.Country.ID
                )
                form.initial["CountryName"] = (
                    "" if Dto.Country == None else Dto.Country.Name
                )
                form.initial["IsSpecial"] = Dto.IsSpecial
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorPortFormModel(_Form):
        form = PortFormModel()

        try:
            form.initial["PortID"] = _Form["PortID"]
            form.initial["Code"] = _Form["Code"]
            form.initial["Name"] = _Form["Name"]
            form.initial["CountryID"] = _Form["CountryID"]
            form.initial["CountryName"] = _Form["CountryName"]
            form.initial["IsSpecial"] = _Form["IsSpecial"]
        except Exception as e:
            print(e)

        return form

    def InitialiseUnitFormModel(UnitID=None):
        form = UnitFormModel()

        try:
            if UnitID == None:
                form.initial["UnitID"] = None
            else:
                Dto = masterRepo.LoadUnit(UnitID)
                form.initial["UnitID"] = Dto.ID
                form.initial["Code"] = Dto.Code
                form.initial["ShortName"] = Dto.ShortName
                form.initial["FullName"] = Dto.FullName
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorUnitFormModel(_Form):
        form = UnitFormModel()

        try:
            form.initial["UnitID"] = _Form["UnitID"]
            form.initial["Code"] = _Form["Code"]
            form.initial["ShortName"] = _Form["ShortName"]
            form.initial["FullName"] = _Form["FullName"]
        except Exception as e:
            print(e)

        return form

    def InitialiseContainerSizeFormModel(ContainerSizeID=None):
        form = ContainerSizeFormModel()

        try:
            if ContainerSizeID == None:
                form.initial["ContainerSizeID"] = None
                form.initial["Teus"] = 1
            else:
                Dto = masterRepo.LoadContainerSize(ContainerSizeID)
                form.initial["ContainerSizeID"] = Dto.ID
                form.initial["Code"] = Dto.Code
                form.initial["Name"] = Dto.Name
                form.initial["Teus"] = Dto.Teus
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorContainerSizeFormModel(_Form):
        form = ContainerSizeFormModel()

        try:
            form.initial["ContainerSizeID"] = _Form["ContainerSizeID"]
            form.initial["Code"] = _Form["Code"]
            form.initial["Name"] = _Form["Name"]
            form.initial["Teus"] = _Form["Teus"]
        except Exception as e:
            print(e)

        return form

    def InitialiseVesselFormModel(VesselID=None):
        form = VesselFormModel()

        try:
            if VesselID == None:
                form.initial["VesselID"] = None
            else:
                Dto = masterRepo.LoadVessel(VesselID)
                form.initial["VesselID"] = Dto.ID
                form.initial["Code"] = Dto.Code
                form.initial["Name"] = Dto.Name
                form.initial["PortOperatorID"] = (
                    None if Dto.PortOperator == None else Dto.PortOperator.ID
                )
                form.initial["PortOperatorName"] = (
                    "" if Dto.PortOperator == None else Dto.PortOperator.Name
                )
                form.initial["PsaID"] = None if Dto.Psa == None else Dto.Psa.ID
                form.initial["PsaName"] = "" if Dto.Psa == None else Dto.Psa.Name
                form.initial["ShippingAgentID"] = (
                    None if Dto.ShippingAgent == None else Dto.ShippingAgent.ID
                )
                form.initial["ShippingAgentName"] = (
                    "" if Dto.ShippingAgent == None else Dto.ShippingAgent.Name
                )
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorVesselFormModel(_Form):
        form = VesselFormModel()

        try:
            form.initial["VesselID"] = _Form["VesselID"]
            form.initial["Code"] = _Form["Code"]
            form.initial["Name"] = _Form["Name"]
            form.initial["PortOperatorID"] = _Form["PortOperatorID"]
            form.initial["PortOperatorName"] = _Form["PortOperatorName"]
            form.initial["PsaID"] = _Form["PsaID"]
            form.initial["PsaName"] = _Form["PsaName"]
            form.initial["ShippingAgentID"] = _Form["ShippingAgentID"]
            form.initial["ShippingAgentName"] = _Form["ShippingAgentName"]
        except Exception as e:
            print(e)

        return form

    def InitialiseItemFormModel(ItemID=None):
        form = ItemFormModel()

        try:
            if ItemID == None:
                form.initial["ItemID"] = None
            else:
                Dto = masterRepo.LoadItem(ItemID)
                form.initial["ItemID"] = Dto.ID
                form.initial["Code"] = Dto.Code
                form.initial["Name"] = Dto.Name
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorItemFormModel(_Form):
        form = ItemFormModel()

        try:
            form.initial["ItemID"] = _Form["ItemID"]
            form.initial["Code"] = _Form["Code"]
            form.initial["Name"] = _Form["Name"]
        except Exception as e:
            print(e)

        return form

    def InitialiseClassFormModel(ClassID=None):
        form = ClassFormModel()

        try:
            if ClassID == None:
                form.initial["ClassID"] = None
            else:
                Dto = masterRepo.LoadClass(ClassID)
                form.initial["ClassID"] = Dto.ID
                form.initial["Code"] = Dto.Code
                form.initial["ShortName"] = Dto.ShortName
                form.initial["FullName"] = Dto.FullName
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorClassFormModel(_Form):
        form = ClassFormModel()

        try:
            form.initial["ClassID"] = _Form["ClassID"]
            form.initial["Code"] = _Form["Code"]
            form.initial["ShortName"] = _Form["ShortName"]
            form.initial["FullName"] = _Form["FullName"]
        except Exception as e:
            print(e)

        return form

    def InitialiseVoyageFormModel(VoyageID=None):
        form = VoyageFormModel()

        try:
            if VoyageID == None:
                form.initial["VoyageID"] = None
                form.initial["Eta"] = datetime.now(tz=timezone.utc)
            else:
                Dto = masterRepo.LoadVoyage(VoyageID)
                form.initial["VoyageID"] = Dto.ID
                form.initial["No"] = Dto.No
                form.initial["ShipCallNo"] = Dto.ShipCallNo
                form.initial["Eta"] = Dto.Eta
                form.initial["VesselID"] = None if Dto.Vessel == None else Dto.Vessel.ID
                form.initial["VesselName"] = (
                    "" if Dto.Vessel == None else Dto.Vessel.Name
                )

        except Exception as e:
            print(e)

        return form

    def InitialiseErrorVoyageFormModel(_Form):
        form = VoyageFormModel()

        try:
            form.initial["VoyageID"] = _Form["VoyageID"]
            form.initial["No"] = _Form["No"]
            form.initial["ShipCallNo"] = _Form["ShipCallNo"]
            form.initial["Eta"] = _Form["Eta"]
            form.initial["VesselID"] = _Form["VesselID"]
            form.initial["VesselName"] = _Form["VesselName"]
        except Exception as e:
            print(e)

        return form

    def InitialiseOperatorFormModel(OperatorID=None):
        form = OperatorFormModel()

        try:
            if OperatorID == None:
                form.initial["OperatorID"] = None
            else:
                Dto = masterRepo.LoadOperator(OperatorID)
                form.initial["OperatorID"] = Dto.ID
                form.initial["Code"] = Dto.Code
                form.initial["Name"] = Dto.Name
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorOperatorFormModel(_Form):
        form = OperatorFormModel()

        try:
            form.initial["OperatorID"] = _Form["OperatorID"]
            form.initial["Code"] = _Form["Code"]
            form.initial["Name"] = _Form["Name"]
        except Exception as e:
            print(e)

        return form
