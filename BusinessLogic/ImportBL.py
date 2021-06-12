from Import.formModels import (
    OblFormModel,
    ContainerFormModel,
    HblFormModel,
    UnstuffContainerFormModel,
    InvoiceFormModel,
)
from Import.dtos import DefaultInvoiceItemUpsertDto
from datetime import datetime
from django.utils import timezone
from DataAccess.ImportRepo import importRepo
from DataAccess.MasterRepo import masterRepo
import math


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
                form.initial["VoyageID"] = None if Dto.Voyage == None else Dto.Voyage.ID
                form.initial["VoyageNo"] = "" if Dto.Voyage == None else Dto.Voyage.No
                form.initial["ShipCallNo"] = (
                    "" if Dto.Voyage == None else Dto.Voyage.ShipCallNo
                )
                form.initial["VesselCode"] = (
                    ""
                    if Dto.Voyage == None
                    else None
                    if Dto.Voyage.Vessel == None
                    else Dto.Voyage.Vessel.Code
                )
                form.initial["LoadPortID"] = (
                    None if Dto.LoadPort == None else Dto.LoadPort.ID
                )
                form.initial["LoadPortName"] = (
                    "" if Dto.LoadPort == None else Dto.LoadPort.Name
                )
                form.initial["UnLoadPortID"] = (
                    None if Dto.UnloadPort == None else Dto.UnloadPort.ID
                )
                form.initial["UnLoadPortName"] = (
                    "" if Dto.UnloadPort == None else Dto.UnloadPort.Name
                )
                form.initial["DestinationPortID"] = (
                    None if Dto.DestinationPort == None else Dto.DestinationPort.ID
                )
                form.initial["DestionationPortName"] = (
                    "" if Dto.DestinationPort == None else Dto.DestinationPort.Name
                )
                form.initial["ShippingAgentID"] = (
                    None if Dto.ShippingAgent == None else Dto.ShippingAgent.ID
                )
                form.initial["ShippingAgentName"] = (
                    "" if Dto.ShippingAgent == None else Dto.ShippingAgent.Name
                )
                form.initial["ConsigneeID"] = (
                    None if Dto.Consignee == None else Dto.Consignee.ID
                )
                form.initial["ConsigneeName"] = (
                    "" if Dto.Consignee == None else Dto.Consignee.Name
                )
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
                form.initial["OblID"] = None if Dto.Obl == None else Dto.Obl.ID
                form.initial["OblNo"] = "" if Dto.Obl == None else Dto.Obl.No
                form.initial["SealNo"] = Dto.SealNo
                form.initial["ContainerSizeID"] = (
                    None if Dto.ContainerSize == None else Dto.ContainerSize.ID
                )
                form.initial["ContainerSizeName"] = (
                    "" if Dto.ContainerSize == None else Dto.ContainerSize.Name
                )
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

    def InitialiseHblFormModel(HblID=None):
        form = HblFormModel()

        try:
            if HblID == None:
                form.initial["HblID"] = None
                form.initial["OblID"] = None
                form.initial["Transhipment"] = 0
            else:
                Dto = importRepo.LoadHbl(HblID)
                form.initial["HblID"] = Dto.ID
                form.initial["No"] = Dto.No
                form.initial["OblID"] = None if Dto.Obl == None else Dto.Obl.ID
                form.initial["OblNo"] = "" if Dto.Obl == None else Dto.Obl.No
                form.initial["ContainerID"] = (
                    None if Dto.Container == None else Dto.Container.ID
                )
                form.initial["ContainerNo"] = (
                    "" if Dto.Container == None else Dto.Container.No
                )
                form.initial["ConsigneeID"] = (
                    None if Dto.Consignee == None else Dto.Consignee.ID
                )
                form.initial["ConsigneeName"] = (
                    "" if Dto.Consignee == None else Dto.Consignee.Name
                )
                form.initial["ClassID"] = None if Dto.Class == None else Dto.Class.ID
                form.initial["ClassFullName"] = (
                    "" if Dto.Class == None else Dto.Class.FullName
                )
                form.initial["UnitID"] = None if Dto.Unit == None else Dto.Unit.ID
                form.initial["UnitShortName"] = (
                    "" if Dto.Unit == None else Dto.Unit.ShortName
                )
                form.initial["PortID"] = None if Dto.Port == None else Dto.Port.ID
                form.initial["PortName"] = "" if Dto.Port == None else Dto.Port.Name
                form.initial["Quantity"] = Dto.Quantity
                form.initial["Weight"] = Dto.Weight
                form.initial["Volume"] = Dto.Volume
                form.initial["Transhipment"] = Dto.Transhipment
                form.initial["MarkDesc"] = Dto.MarkDesc
                form.initial["CargoDesc"] = Dto.CargoDesc

        except Exception as e:
            print(e)

        return form

    def InitialiseErrorHblFormModel(_Form):
        form = HblFormModel()

        try:
            form.initial["HblID"] = _Form["HblID"]
            form.initial["No"] = _Form["No"]
            form.initial["OblID"] = _Form["OblID"]
            form.initial["OblNo"] = _Form["OblNo"]
            form.initial["ContainerID"] = _Form["ContainerID"]
            form.initial["ContainerNo"] = _Form["ContainerNo"]
            form.initial["ConsigneeID"] = _Form["ConsigneeID"]
            form.initial["ConsigneeName"] = _Form["ConsigneeName"]
            form.initial["ClassID"] = _Form["ClassID"]
            form.initial["ClassFullName"] = _Form["ClassFullName"]
            form.initial["UnitID"] = _Form["UnitID"]
            form.initial["UnitShortName"] = _Form["UnitShortName"]
            form.initial["PortID"] = _Form["PortID"]
            form.initial["PortName"] = _Form["PortName"]
            form.initial["Quantity"] = _Form["Quantity"]
            form.initial["Weight"] = _Form["Weight"]
            form.initial["Volume"] = _Form["Volume"]
            form.initial["Transhipment"] = _Form["Transhipment"]
            form.initial["MarkDesc"] = _Form["MarkDesc"]
            form.initial["CargoDesc"] = _Form["CargoDesc"]
        except Exception as e:
            print(e)

        return form

    def InitialiseUnstuffContainerFormModel(ContainerID=None, HblID=None):
        form = UnstuffContainerFormModel()

        try:
            if HblID == None:
                Dto = importRepo.LoadContainer(ContainerID)
                form.initial["ContainerID"] = Dto.ID
                form.initial["ContainerNo"] = Dto.No
                form.initial["UnstuffDate"] = Dto.UnstuffDate
                form.initial["IsUnStuff"] = Dto.IsUnStuff
                form.initial["HblID"] = None
                form.initial["Transhipment"] = 0
                form.initial["InwardSurvey"] = 0
                form.initial["HeavyLiftCargo"] = 0
                form.initial["LongLengthCargo"] = 0
                form.initial["PortPolice"] = 0
                form.initial["CargoSurvey"] = 0
                form.initial["MaqisHold"] = 0
                form.initial["HealthHold"] = 0
                form.initial["PreventiveHold"] = 0
                form.initial["CustomsHold"] = 0
            else:
                Dto = importRepo.LoadHbl(HblID)
                form.initial["ContainerID"] = (
                    None if Dto.Container == None else Dto.Container.ID
                )
                form.initial["ContainerNo"] = (
                    "" if Dto.Container == None else Dto.Container.No
                )
                form.initial["UnstuffDate"] = (
                    None if Dto.Container == None else Dto.Container.UnstuffDate
                )
                form.initial["IsUnStuff"] = (
                    False if Dto.Container == None else Dto.Container.IsUnStuff
                )
                form.initial["HblID"] = Dto.ID
                form.initial["No"] = Dto.No
                form.initial["ConsigneeName"] = (
                    "" if Dto.Consignee == None else Dto.Consignee.Name
                )
                form.initial["ClassFullName"] = (
                    "" if Dto.Class == None else Dto.Class.FullName
                )
                form.initial["UnitShortName"] = (
                    "" if Dto.Unit == None else Dto.Unit.ShortName
                )
                form.initial["PortID"] = None if Dto.Port == None else Dto.Port.ID
                form.initial["PortName"] = "" if Dto.Port == None else Dto.Port.Name
                form.initial["Quantity"] = Dto.Quantity
                form.initial["Weight"] = Dto.Weight
                form.initial["Volume"] = Dto.Volume
                form.initial["Transhipment"] = Dto.Transhipment
                form.initial["MarkDesc"] = Dto.MarkDesc
                form.initial["CargoDesc"] = Dto.CargoDesc
                form.initial["PackageDesc"] = Dto.PackageDesc
                form.initial["LocationDesc"] = Dto.LocationDesc
                form.initial["InwardSurvey"] = Dto.InwardSurvey
                form.initial["Remarks"] = Dto.Remarks
                form.initial["HeavyLiftCargo"] = Dto.HeavyLiftCargo
                form.initial["LongLengthCargo"] = Dto.LongLengthCargo
                form.initial["PortPolice"] = Dto.PortPolice
                form.initial["CargoSurvey"] = Dto.CargoSurvey
                form.initial["MaqisHold"] = Dto.MaqisHold
                form.initial["HealthHold"] = Dto.HealthHold
                form.initial["PreventiveHold"] = Dto.PreventiveHold
                form.initial["CustomsHold"] = Dto.CustomsHold

        except Exception as e:
            print(e)

        return form

    def InitialiseErrorUnstuffContainerFormModel(_Form):
        form = UnstuffContainerFormModel()

        try:
            form.initial["ContainerID"] = _Form["ContainerID"]
            form.initial["ContainerNo"] = _Form["ContainerNo"]
            form.initial["UnstuffDate"] = _Form["UnstuffDate"]
            form.initial["IsUnStuff"] = _Form["IsUnstuff"]
            form.initial["HblID"] = _Form["HblID"]
            form.initial["No"] = _Form["No"]
            form.initial["ConsigneeName"] = _Form["ConsigneeName"]
            form.initial["ClassFullName"] = _Form["ClassFullName"]
            form.initial["UnitShortName"] = _Form["UnitShortName"]
            form.initial["PortID"] = _Form["PortID"]
            form.initial["PortName"] = _Form["PortName"]
            form.initial["Quantity"] = _Form["Quantity"]
            form.initial["Weight"] = _Form["Weight"]
            form.initial["Volume"] = _Form["Volume"]
            form.initial["Transhipment"] = _Form["Transhipment"]
            form.initial["MarkDesc"] = _Form["MarkDesc"]
            form.initial["CargoDesc"] = _Form["CargoDesc"]
            form.initial["PackageDesc"] = _Form["PackageDesc"]
            form.initial["LocationDesc"] = _Form["LocationDesc"]
            form.initial["InwardSurvey"] = _Form["InwardSurvey"]
            form.initial["Remarks"] = _Form["Remarks"]
            form.initial["HeavyLiftCargo"] = _Form["HeavyLiftCargo"]
            form.initial["LongLengthCargo"] = _Form["LongLengthCargo"]
            form.initial["PortPolice"] = _Form["PortPolice"]
            form.initial["CargoSurvey"] = _Form["CargoSurvey"]
            form.initial["MaqisHold"] = _Form["MaqisHold"]
            form.initial["HealthHold"] = _Form["HealthHold"]
            form.initial["PreventiveHold"] = _Form["PreventiveHold"]
            form.initial["CustomsHold"] = _Form["CustomsHold"]
        except Exception as e:
            print(e)

        return form

    def InitialiseInvoiceFormModel(InvoiceID=None):
        form = InvoiceFormModel()

        try:
            if InvoiceID == None:
                form.initial["InvoiceID"] = None
                form.initial["IssueDate"] = datetime.now(tz=timezone.utc)
                form.initial["PaymentType"] = 0
            else:
                Dto = importRepo.LoadInvoice(InvoiceID)
                form.initial["InvoiceID"] = Dto.ID
                form.initial["No"] = Dto.No
                form.initial["IssueDate"] = Dto.IssueDate
                form.initial["HblID"] = None if Dto.Hbl == None else Dto.Hbl.ID
                form.initial["HblNo"] = "" if Dto.Hbl == None else Dto.Hbl.No
                form.initial["OblNo"] = (
                    ""
                    if Dto.Hbl == None
                    else ""
                    if Dto.Hbl.Obl == None
                    else Dto.Hbl.Obl.No
                )
                form.initial["VoyageNo"] = (
                    ""
                    if Dto.Hbl == None
                    else ""
                    if Dto.Hbl.Obl == None
                    else ""
                    if Dto.Hbl.Obl.Voyage == None
                    else Dto.Hbl.Obl.Voyage.No
                )
                form.initial["ShipCallNo"] = (
                    ""
                    if Dto.Hbl == None
                    else ""
                    if Dto.Hbl.Obl == None
                    else ""
                    if Dto.Hbl.Obl.Voyage == None
                    else Dto.Hbl.Obl.Voyage.ShipCallNo
                )
                form.initial["Eta"] = (
                    ""
                    if Dto.Hbl == None
                    else ""
                    if Dto.Hbl.Obl == None
                    else ""
                    if Dto.Hbl.Obl.Voyage == None
                    else Dto.Hbl.Obl.Voyage.Eta
                )
                form.initial["VesselName"] = (
                    ""
                    if Dto.Hbl == None
                    else ""
                    if Dto.Hbl.Obl == None
                    else ""
                    if Dto.Hbl.Obl.Voyage == None
                    else ""
                    if Dto.Hbl.Obl.Voyage.Vessel == None
                    else Dto.Hbl.Obl.Voyage.Vessel.Name
                )
                form.initial["LoadPortName"] = (
                    ""
                    if Dto.Hbl == None
                    else ""
                    if Dto.Hbl.Obl == None
                    else ""
                    if Dto.Hbl.Obl.LoadPort == None
                    else Dto.Hbl.Obl.LoadPort.Name
                )
                form.initial["UnLoadPortName"] = (
                    ""
                    if Dto.Hbl == None
                    else ""
                    if Dto.Hbl.Obl == None
                    else ""
                    if Dto.Hbl.Obl.UnloadPort == None
                    else Dto.Hbl.Obl.UnloadPort.Name
                )
                form.initial["StorageDay"] = Dto.StorageDay
                form.initial["UnstuffDate"] = (
                    ""
                    if Dto.Hbl == None
                    else ""
                    if Dto.Hbl.Container == None
                    else Dto.Hbl.Container.UnstuffDate
                )
                form.initial["IsPartial"] = Dto.IsPartial
                form.initial["IssuedQuantity"] = Dto.IssuedQuantity
                form.initial["IssuedWeight"] = Dto.IssuedWeight
                form.initial["IssuedVolume"] = Dto.IssuedVolume
                form.initial["InitialQuantity"] = (
                    0 if Dto.Hbl == None else Dto.Hbl.Quantity
                )
                form.initial["InitialWeight"] = 0 if Dto.Hbl == None else Dto.Hbl.Weight
                form.initial["InitialVolume"] = 0 if Dto.Hbl == None else Dto.Hbl.Volume
                form.initial["BalanceQuantity"] = Dto.BalanceQuantity
                form.initial["BalanceWeight"] = Dto.BalanceWeight
                form.initial["BalanceVolume"] = Dto.BalanceVolume
                form.initial["LocationDesc"] = (
                    "" if Dto.Hbl == None else Dto.Hbl.LocationDesc
                )
                form.initial["PackageDesc"] = (
                    "" if Dto.Hbl == None else Dto.Hbl.PackageDesc
                )
                form.initial["ConsigneeID"] = (
                    None if Dto.Consignee == None else Dto.Consignee.ID
                )
                form.initial["ConsigneeName"] = (
                    "" if Dto.Consignee == None else Dto.Consignee.Name
                )
                form.initial["PaymentType"] = Dto.PaymentType
                form.initial["RefNo"] = Dto.RefNo
                form.initial["IidNo"] = Dto.IidNo

        except Exception as e:
            print(e)

        return form

    def InitialiseErrorInvoiceFormModel(_Form):
        form = InvoiceFormModel()

        try:
            form.initial["InvoiceID"] = _Form["InvoiceID"]
            form.initial["No"] = _Form["No"]
            form.initial["IssueDate"] = _Form["IssueDate"]
            form.initial["HblID"] = _Form["HblID"]
            form.initial["HblNo"] = _Form["HblNo"]
            form.initial["OblNo"] = _Form["OblNo"]
            form.initial["VoyageNo"] = _Form["VoyageNo"]
            form.initial["ShipCallNo"] = _Form["ShipCallNo"]
            form.initial["Eta"] = _Form["Eta"]
            form.initial["VesselName"] = _Form["VesselName"]
            form.initial["LoadPortName"] = _Form["LoadPortName"]
            form.initial["UnLoadPortName"] = _Form["UnLoadPortName"]
            form.initial["StorageDay"] = _Form["StorageDay"]
            form.initial["UnstuffDate"] = _Form["UnstuffDate"]
            form.initial["IsPartial"] = _Form["IsPartial"]
            form.initial["IssuedQuantity"] = _Form["IssuedQuantity"]
            form.initial["IssuedWeight"] = _Form["IssuedWeight"]
            form.initial["IssuedVolume"] = _Form["IssuedVolume"]
            form.initial["InitialQuantity"] = _Form["InitialQuantity"]
            form.initial["InitialWeight"] = _Form["InitialWeight"]
            form.initial["InitialVolume"] = _Form["InitialVolume"]
            form.initial["BalanceQuantity"] = _Form["BalanceQuantity"]
            form.initial["BalanceWeight"] = _Form["BalanceWeight"]
            form.initial["BalanceVolume"] = _Form["BalanceVolume"]
            form.initial["LocationDesc"] = _Form["LocationDesc"]
            form.initial["PackageDesc"] = _Form["PackageDesc"]
            form.initial["ConsigneeID"] = _Form["ConsigneeID"]
            form.initial["ConsigneeName"] = _Form["ConsigneeName"]
            form.initial["PaymentType"] = _Form["PaymentType"]
            form.initial["RefNo"] = _Form["RefNo"]
            form.initial["IidNo"] = _Form["IidNo"]
        except Exception as e:
            print(e)

        return form

    def UpsertDefaultInvoiceItem(InvoiceID=None):
        rtn = False
        SysBadMsg = None

        InvoiceDto = None
        FloorWeight = 0
        FloorVolume = 0
        FractionWeight = 0
        FractionVolume = 0
        ItemQuantity = 0
        ClassType = None
        DefaultItemCode = None
        DefaultItemDto = None
        TotalInvoiceAmount = 0
        UpsertResult = 0

        try:
            InvoiceDto = importRepo.LoadInvoice(InvoiceID)

            FloorWeight = math.floor(InvoiceDto.IssuedWeight / 1000)
            FractionWeight = (InvoiceDto.IssuedWeight / 1000) - FloorWeight
            FloorWeight += 1 if FractionWeight != 0 else 0

            FloorVolume = math.floor(InvoiceDto.IssuedVolume)
            FractionVolume = InvoiceDto.IssuedVolume - FloorVolume
            FloorVolume += 1 if FractionVolume != 0 else 0

            ItemQuantity = FloorWeight if FloorWeight >= FloorVolume else FloorVolume

            ClassType = (
                "NORMAL"
                if InvoiceDto.Hbl.Class.ShortName == "GENERAL"
                else "DANGEROUS"
                if InvoiceDto.Hbl.Class.ShortName == "DG CLS I"
                else "DANGEROUS"
                if InvoiceDto.Hbl.Class.ShortName == "DG CLS II"
                else "DANGEROUS"
                if InvoiceDto.Hbl.Class.ShortName == "DG CLS III"
                else None
            )

            if ClassType == "NORMAL" or ClassType == "DANGEROUS":
                DefaultItemCode = "%s%s%s" % (
                    "N" if ClassType == "NORMAL" else "D",
                    "D3" if InvoiceDto.StorageDay <= 3 else "D4",
                    "Q1" if ItemQuantity <= 1 else "Q2",
                )

                DefaultItemDto = masterRepo.AdvSearchDefaultItemByAccountTypeCode(
                    "IN", DefaultItemCode
                )

                importRepo.DeleteDefaultInvoiceItem(InvoiceID)

                importRepo.UpdateInvoiceAmount(InvoiceID)

                for dto in DefaultItemDto:
                    UpsertDto = DefaultInvoiceItemUpsertDto()
                    UpsertDto.InvoiceID = str(InvoiceID)
                    UpsertDto.ItemID = str(dto.Item.ID)
                    UpsertDto.ItemQuantity = ItemQuantity
                    UpsertDto.ItemUnitAmount = dto.Amount
                    UpsertDto.ItemAmount = (
                        dto.Amount * ItemQuantity * InvoiceDto.StorageDay
                        if dto.Item.Name == "STORAGE CHARGES"
                        else dto.Amount * ItemQuantity * 1
                    )
                    TotalInvoiceAmount += UpsertDto.ItemAmount
                    UpsertResult += (
                        1
                        if importRepo.UpsertDefaultInvoiceItem(UpsertDto) == True
                        else 0
                    )

                if UpsertResult == len(DefaultItemDto):
                    importRepo.UpdateInvoiceAmount(InvoiceID)
                    rtn = True
                else:
                    SysBadMsg = "One or more than one default item(s) failed to add"

            else:
                SysBadMsg = "%s is not a General or Dangerous class" % InvoiceDto.Hbl.No

        except Exception as e:
            print(e)
            SysBadMsg = e

        return {"rtn": rtn, "SysBadMsg": SysBadMsg}

    def UpsertInvoiceItem(
        InvoiceID, InvoiceItemID, ItemID, ItemQuantity, ItemUnitAmount
    ):
        rtn = False

        rtn = importRepo.UpsertInvoiceItem(
            InvoiceID, InvoiceItemID, ItemID, ItemQuantity, ItemUnitAmount
        )

        importRepo.UpdateInvoiceAmount(InvoiceID)

        return rtn

    def DeleteInvoiceItem(InvoiceItemID):
        rtn = False
        InvoiceItemDto = None

        InvoiceItemDto = importRepo.LoadInvoiceItem(InvoiceItemID)

        rtn = importRepo.DeleteInvoiceItem(InvoiceItemID)

        importRepo.UpdateInvoiceAmount(InvoiceItemDto.Invoice.ID)

        return rtn
