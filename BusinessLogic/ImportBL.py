from Import.formModels import OblFormModel, ContainerFormModel
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

    def InitialiseContainerFormModel(ContainerID=None):
        form = ContainerFormModel()

        try:
            if ContainerID == None:
                form.initial["ContainerID"] = None
                form.initial["Type"] = 0
                form.initial["Status"] = 1
                form.initial["ShipType"] = 0
                form.initial["Movement"] = 1
                form.initial["SealParty"] = 1
                form.initial["Supplier"] = 1
            else:
                Dto = importRepo.LoadContainer(ContainerID)
                form.initial["ContainerID"] = Dto.ID
                form.initial["No"] = Dto.No
                form.initial["OblID"] = Dto.Obl.ID
                form.initial["OblNo"] = Dto.Obl.No
                form.initial["SealNo"] = Dto.SealNo
                form.initial["ContainerSizeID"] = Dto.ContainerSize.ID
                form.initial["ContainerSizeName"] = Dto.ContainerSize.Name
                form.initial["Type"] = Dto.Type
                form.initial["Status"] = Dto.Status
                form.initial["ShipType"] = Dto.ShipType
                form.initial["Movement"] = Dto.Movement
                form.initial["SealParty"] = Dto.SealParty
                form.initial["Supplier"] = Dto.Supplier
        except Exception as e:
            print(e)

        return form

    def InitialiseErrorContainerFormModel(_Form):
        form = ContainerFormModel()

        try:
            form.initial["ContainerID"] = _Form["ContainerID"]
            form.initial["No"] = _Form["No"]
            form.initial["OblID"] = _Form["OblID"]
            form.initial["OblNo"] = _Form["OblNo"]
            form.initial["SealNo"] = _Form["SealNo"]
            form.initial["ContainerSizeID"] = _Form["ContainerSizeID"]
            form.initial["ContainerSizeName"] = _Form["ContainerSizeName"]
            form.initial["Type"] = _Form["Type"]
            form.initial["Status"] = _Form["Status"]
            form.initial["ShipType"] = _Form["ShipType"]
            form.initial["Movement"] = _Form["Movement"]
            form.initial["SealParty"] = _Form["SealParty"]
            form.initial["Supplier"] = _Form["Supplier"]
        except Exception as e:
            print(e)

        return form
