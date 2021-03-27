from Import.formModels import OblFormModel
from DataAccess.ImportRepo import importRepo


class importBL:
    def InitialiseOblFormModel(OblID=None):
        form = OblFormModel()

        try:
            if OblID == None:
                form.initial["OblID"] = None
            else:
                Dto = importRepo.LoadObl(OblID)
                form.initial["OblID"] = Dto.ID
                form.initial["No"] = Dto.No
                form.initial["VoyageID"] = Dto.Voyage.ID
                form.initial["VoyageNo"] = Dto.Voyage.No
                form.initial["ShipCallNo"] = Dto.Voyage.ShipCallNo
                form.initial["VesselCode"] = Dto.Voyage.Vessel.Code
                form.initial["LoadPortID"] = Dto.LoadPort.ID
                form.initial["LoadPortName"] = Dto.LoadPort.Name
                form.initial["UnLoadPortID"] = Dto.UnloadPort.ID
                form.initial["UnLoadPortName"] = Dto.UnloadPort.Name
                form.initial["DestinationPortID"] = Dto.DestinationPort.ID
                form.initial["DestionationPortName"] = Dto.DestinationPort.Name
                form.initial["ShippingAgentID"] = Dto.ShippingAgent.ID
                form.initial["ShippingAgentName"] = Dto.ShippingAgent.Name
                form.initial["ConsigneeID"] = Dto.Consignee.ID
                form.initial["ConsigneeName"] = Dto.Consignee.Name
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorOblFormModel(_Form):
        form = OblFormModel()

        try:
            form.initial["OblID"] = _Form["OblID"]
            form.initial["No"] = _Form["No"]
            form.initial["VoyageID"] = _Form["VoyageID"]
            form.initial["VoyageNo"] = _Form["VoyageNo"]
            form.initial["ShipCallNo"] = _Form["ShipCallNo"]
            form.initial["VesselCode"] = _Form["VesselCode"]
            form.initial["LoadPortID"] = _Form["LoadPortID"]
            form.initial["LoadPortName"] = _Form["LoadPortName"]
            form.initial["UnLoadPortID"] = _Form["UnLoadPortID"]
            form.initial["UnLoadPortName"] = _Form["UnLoadPortName"]
            form.initial["DestinationPortID"] = _Form["DestinationPortID"]
            form.initial["DestionationPortName"] = _Form["DestionationPortName"]
            form.initial["ShippingAgentID"] = _Form["ShippingAgentID"]
            form.initial["ShippingAgentName"] = _Form["ShippingAgentName"]
            form.initial["ConsigneeID"] = _Form["ConsigneeID"]
            form.initial["ConsigneeName"] = _Form["ConsigneeName"]
        except Exception as e:
            print(e)

        return form
