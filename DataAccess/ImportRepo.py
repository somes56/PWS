from datetime import datetime
import uuid
from django.db.models import Q
from django.utils import timezone
from django.db import connection
from Import.models import InvoiceItem, Obl, Container, Hbl, Invoice
from Master.models import Voyage, Port, Customer, ContainerSize, Class, Unit, Item
from BusinessLogic.SysBL import sysBL


class importRepo:
    def AdvSearchObl(SearchBy=""):
        Obls = []

        try:
            Obls = Obl.objects.filter(IsActive=True, No__icontains=SearchBy).order_by(
                "No"
            )
        except Exception as e:
            print(e)

        return Obls

    def AdvSearchContainerByObl(OblID=None, SearchBy=""):
        Containers = []

        try:
            Containers = Container.objects.filter(
                IsActive=True, Obl__ID=OblID, No__icontains=SearchBy
            ).order_by("No")
        except Exception as e:
            print(e)

        return Containers

    def AdvSearchHblByContainer(ContainerID=None, SearchBy=""):
        Hbls = []

        try:
            Hbls = Hbl.objects.filter(
                IsActive=True, Container__ID=ContainerID, No__icontains=SearchBy
            ).order_by("No")
        except Exception as e:
            print(e)

        return Hbls

    def AdvSearchHblHist(SearchBy=""):
        Hbls = []

        SearchBy = "%" + SearchBy + "%"

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT 	Hbl."ID" , Hbl."No" , Hbl."Quantity" AS "InitialQuantity", Hbl."Weight"  AS "InitialWeight", Hbl."Volume" AS "InitialVolume", 
		                        CASE WHEN HblHist."BalanceQuantity" ISNULL THEN Hbl."Quantity"  ELSE HblHist."BalanceQuantity" END AS "BalanceQuantity",
		                        CASE WHEN HblHist."BalanceWeight" ISNULL THEN Hbl."Weight"  ELSE HblHist."BalanceWeight" END AS "BalanceWeight",
		                        CASE WHEN HblHist."BalanceVolume" ISNULL THEN Hbl."Volume"  ELSE HblHist."BalanceVolume" END AS "BalanceVolume",
                                Obl."No" AS "OblNo", Voyage."No" AS "VoyageNo", Voyage."ShipCallNo", Voyage."Eta", Vessel."Name" AS "VesselName",
                                LoadPort."Name" AS "LoadPortName", UnloadPort."Name" AS "UnloadPortName", Container."UnstuffDate", Hbl."LocationDesc",
                                Hbl."PackageDesc", HblConsignee."ID" AS "ConsigneeID", HblConsignee."Name" AS "ConsigneeName"
                        FROM "imp_Hbl" Hbl
                        INNER JOIN "imp_Obl"  Obl ON Hbl."OblID" = Obl."ID"
                        INNER JOIN "mst_Voyage" Voyage ON Obl."VoyageID" = Voyage."ID" 
                        INNER JOIN "mst_Vessel" Vessel ON Voyage."VesselID" = Vessel."ID" 
                        INNER JOIN  "mst_Port" LoadPort ON Obl."LoadPortID" = LoadPort."ID" 
                        INNER JOIN "mst_Port" UnloadPort ON Obl."UnloadPortID" = UnloadPort."ID" 
                        INNER JOIN "imp_Container" Container ON Hbl."ContainerID" = Container."ID" 
                        INNER JOIN "mst_Customer" HblConsignee ON Hbl."ConsigneeID" = HblConsignee."ID"   
                        LEFT JOIN
                        (
                            SELECT ii2."HblID" , ii2."BalanceQuantity" , ii2."BalanceWeight" , ii2."BalanceVolume" 
                            FROM
                            (
                                SELECT ii."HblID", MAX(ii."CreateDate") AS "CreateDate" 
                                FROM "imp_Invoice" ii WHERE ii."IsActive" = TRUE GROUP BY ii."HblID" 
                            ) AS InvoiceHist INNER JOIN "imp_Invoice" ii2  ON InvoiceHist."HblID" = ii2."HblID"  AND InvoiceHist."CreateDate" = ii2."CreateDate" 
                        ) AS HblHist ON Hbl."ID"  = HblHist."HblID"
                        WHERE HblHist."BalanceQuantity" > 0 OR HblHist."BalanceQuantity" IS NULL AND Hbl."No" LIKE UPPER(%s) OR Obl."No" LIKE UPPER(%s)
                        ORDER BY Obl."No", Hbl."No" ASC """,
                    [SearchBy, SearchBy],
                )
                Hbls = cursor.fetchall()
        except Exception as e:
            print(e)

        return Hbls

    def PartialOblList(SearchBy=""):
        Obls = []

        try:
            Obls = Obl.objects.filter(IsActive=True, No__icontains=SearchBy).order_by(
                "No"
            )[:100]
        except Exception as e:
            print(e)

        return Obls

    def PartialContainerList(SearchBy=""):
        Containers = []

        try:
            Containers = Container.objects.filter(
                Q(Obl__No__icontains=SearchBy) | Q(No__icontains=SearchBy),
                IsActive=True,
            ).order_by("Obl__No", "No")[:100]
        except Exception as e:
            print(e)

        return Containers

    def PartialHblList(SearchBy=""):
        Hbls = []

        try:
            Hbls = Hbl.objects.filter(
                Q(Obl__No__icontains=SearchBy)
                | Q(Container__No__icontains=SearchBy)
                | Q(No__icontains=SearchBy),
                IsActive=True,
            ).order_by("Obl__No", "Container__No", "No")[:100]
        except Exception as e:
            print(e)

        return Hbls

    def PartialUnstuffContainerPendingList(SearchBy=""):
        Containers = []

        try:
            Containers = Container.objects.filter(
                IsActive=True, IsUnStuff=False, No__icontains=SearchBy
            ).order_by("Obl__No", "No")[:100]
        except Exception as e:
            print(e)

        return Containers

    def PartialUnstuffContainerCompletedList(SearchBy=""):
        Containers = []

        try:
            Containers = Container.objects.filter(
                IsActive=True, IsUnStuff=True, No__icontains=SearchBy
            ).order_by("Obl__No", "No")[:100]
        except Exception as e:
            print(e)

        return Containers

    def PartialInvoiceList(SearchBy=""):
        Invoices = []

        try:
            Invoices = Invoice.objects.filter(
                Q(Hbl__No__icontains=SearchBy) | Q(No__icontains=SearchBy),
                IsActive=True,
            ).order_by("-No")[:100]
        except Exception as e:
            print(e)

        return Invoices

    def PartialInvoiceItemList(InvoiceID=None):
        InvoiceItems = []

        try:
            InvoiceItems = InvoiceItem.objects.filter(
                Invoice__ID=InvoiceID, IsActive=True
            ).order_by("Item__Name")[:100]
        except Exception as e:
            print(e)

        return InvoiceItems

    def LoadObl(OblID):
        OblDto = Obl()

        try:
            OblDto = Obl.objects.get(ID=OblID, IsActive=True)
        except Exception as e:
            print(e)

        return OblDto

    def LoadContainer(ContainerID):
        ContainerDto = Container()

        try:
            ContainerDto = Container.objects.get(ID=ContainerID, IsActive=True)
        except Exception as e:
            print(e)

        return ContainerDto

    def LoadHbl(HblID):
        HblDto = Hbl()

        try:
            HblDto = Hbl.objects.get(ID=HblID, IsActive=True)
        except Exception as e:
            print(e)

        return HblDto

    def LoadInvoice(InvoiceID):
        InvoiceDto = Invoice()

        try:
            InvoiceDto = Invoice.objects.get(ID=InvoiceID, IsActive=True)
        except Exception as e:
            print(e)

        return InvoiceDto

    def LoadInvoiceItem(InvoiceItemID):
        InvoiceItemDto = InvoiceItem()

        try:
            InvoiceItemDto = InvoiceItem.objects.get(ID=InvoiceItemID, IsActive=True)
        except Exception as e:
            print(e)

        return InvoiceItemDto

    def UpsertObl(Dto):
        rtn = False
        OblID = None
        VoyageDto = None
        LoadPortDto = None
        UnLoadPortDto = None
        DestinationPortDto = None
        ShippingAgentDto = None
        ConsigneeDto = None
        UpsertDto = None

        try:
            VoyageDto = Voyage.objects.get(ID=Dto["VoyageID"])
            LoadPortDto = Port.objects.get(ID=Dto["LoadPortID"])
            UnLoadPortDto = Port.objects.get(ID=Dto["UnLoadPortID"])
            DestinationPortDto = Port.objects.get(ID=Dto["DestinationPortID"])
            ShippingAgentDto = Customer.objects.get(ID=Dto["ShippingAgentID"])
            ConsigneeDto = Customer.objects.get(ID=Dto["ConsigneeID"])

            if Dto["OblID"] == None:

                UpsertDto = Obl.objects.create(
                    No=Dto["No"],
                    Voyage=VoyageDto,
                    LoadPort=LoadPortDto,
                    UnloadPort=UnLoadPortDto,
                    DestinationPort=DestinationPortDto,
                    ShippingAgent=ShippingAgentDto,
                    Consignee=ConsigneeDto,
                    IsActive=True,
                    CreateDate=datetime.now(tz=timezone.utc),
                    CreateBy=None,
                    UpdateDate=datetime.now(tz=timezone.utc),
                    UpdateBy=None,
                )

                if UpsertDto.ID:
                    rtn = True
                    OblID = UpsertDto.ID

            else:
                UpsertDto = Obl.objects.get(ID=Dto["OblID"])
                UpsertDto.No = Dto["No"]
                UpsertDto.Voyage = VoyageDto
                UpsertDto.LoadPort = LoadPortDto
                UpsertDto.UnloadPort = UnLoadPortDto
                UpsertDto.DestinationPort = DestinationPortDto
                UpsertDto.ShippingAgent = ShippingAgentDto
                UpsertDto.Consignee = ConsigneeDto
                UpsertDto.IsActive = True
                UpsertDto.UpdateDate = datetime.now(tz=timezone.utc)
                UpsertDto.UpdateBy = None
                UpsertDto.save()
                rtn = True
                OblID = Dto["OblID"]

        except Exception as e:
            print(e)

        return {"rtn": rtn, "OblID": OblID}

    def UpsertContainer(Dto):
        rtn = False
        ContainerID = None
        OblDto = None
        ContainerSizeDto = None
        UpsertDto = None

        try:
            OblDto = Obl.objects.get(ID=Dto["OblID"])
            ContainerSizeDto = ContainerSize.objects.get(ID=Dto["ContainerSizeID"])

            if Dto["ContainerID"] == None:

                UpsertDto = Container.objects.create(
                    No=Dto["No"],
                    Obl=OblDto,
                    SealNo=Dto["SealNo"],
                    ContainerSize=ContainerSizeDto,
                    Type=Dto["Type"],
                    Status=Dto["Status"],
                    ShipType=Dto["ShipType"],
                    Movement=Dto["Movement"],
                    SealParty=Dto["SealParty"],
                    Supplier=Dto["Supplier"],
                    IsUnStuff=False,
                    UnstuffDate=None,
                    IsActive=True,
                    CreateDate=datetime.now(tz=timezone.utc),
                    CreateBy=None,
                    UpdateDate=datetime.now(tz=timezone.utc),
                    UpdateBy=None,
                )

                if UpsertDto.ID:
                    rtn = True
                    ContainerID = UpsertDto.ID

            else:
                UpsertDto = Container.objects.get(ID=Dto["ContainerID"])
                UpsertDto.No = Dto["No"]
                UpsertDto.Obl = OblDto
                UpsertDto.SealNo = Dto["SealNo"]
                UpsertDto.ContainerSize = ContainerSizeDto
                UpsertDto.Type = Dto["Type"]
                UpsertDto.Status = Dto["Status"]
                UpsertDto.ShipType = Dto["ShipType"]
                UpsertDto.Movement = Dto["Movement"]
                UpsertDto.SealParty = Dto["SealParty"]
                UpsertDto.Supplier = Dto["Supplier"]
                UpsertDto.IsActive = True
                UpsertDto.UpdateDate = datetime.now(tz=timezone.utc)
                UpsertDto.UpdateBy = None
                UpsertDto.save()
                rtn = True
                ContainerID = Dto["ContainerID"]

        except Exception as e:
            print(e)

        return {"rtn": rtn, "ContainerID": ContainerID}

    def UpsertHbl(Dto):
        rtn = False
        HblID = None
        OblDto = None
        ContainerDto = None
        ConsigneeDto = None
        ClassDto = None
        UnitDto = None
        PortDto = None
        UpsertDto = None

        try:
            OblDto = Obl.objects.get(ID=Dto["OblID"])
            ContainerDto = Container.objects.get(ID=Dto["ContainerID"])
            ConsigneeDto = Customer.objects.get(ID=Dto["ConsigneeID"])
            ClassDto = Class.objects.get(ID=Dto["ClassID"])
            UnitDto = Unit.objects.get(ID=Dto["UnitID"])
            PortDto = (
                None if Dto["PortID"] == None else Port.objects.get(ID=Dto["PortID"])
            )

            if Dto["HblID"] == None:

                UpsertDto = Hbl.objects.create(
                    No=Dto["No"],
                    Obl=OblDto,
                    Container=ContainerDto,
                    Consignee=ConsigneeDto,
                    Class=ClassDto,
                    Unit=UnitDto,
                    Port=PortDto,
                    Quantity=Dto["Quantity"],
                    Weight=Dto["Weight"],
                    Volume=Dto["Volume"],
                    Transhipment=Dto["Transhipment"],
                    MarkDesc=Dto["MarkDesc"],
                    CargoDesc=Dto["CargoDesc"],
                    IsActive=True,
                    CreateDate=datetime.now(tz=timezone.utc),
                    CreateBy=None,
                    UpdateDate=datetime.now(tz=timezone.utc),
                    UpdateBy=None,
                )

                if UpsertDto.ID:
                    rtn = True
                    HblID = UpsertDto.ID

            else:
                UpsertDto = Hbl.objects.get(ID=Dto["HblID"])
                UpsertDto.No = Dto["No"]
                UpsertDto.Obl = OblDto
                UpsertDto.Container = ContainerDto
                UpsertDto.Consignee = ConsigneeDto
                UpsertDto.Class = ClassDto
                UpsertDto.Unit = UnitDto
                UpsertDto.Port = PortDto
                UpsertDto.Quantity = Dto["Quantity"]
                UpsertDto.Weight = Dto["Weight"]
                UpsertDto.Volume = Dto["Volume"]
                UpsertDto.Transhipment = Dto["Transhipment"]
                UpsertDto.MarkDesc = Dto["MarkDesc"]
                UpsertDto.CargoDesc = Dto["CargoDesc"]
                UpsertDto.IsActive = True
                UpsertDto.UpdateDate = datetime.now(tz=timezone.utc)
                UpsertDto.UpdateBy = None
                UpsertDto.save()
                rtn = True
                HblID = Dto["HblID"]

        except Exception as e:
            print(e)

        return {"rtn": rtn, "HblID": HblID}

    def UpsertUnstuffContainer(Dto):
        rtn = False
        ContainerID = None
        HblID = None
        UnstuffDate = None
        PortDto = None
        UpsertContainerDto = None
        UpsertHblDto = None

        try:
            if Dto["PortID"] != None:
                PortDto = Port.objects.get(ID=Dto["PortID"])

            if Dto["IsUnStuff"] == True:
                UnstuffDate = Dto["UnstuffDate"]

            UpsertContainerDto = Container.objects.get(ID=Dto["ContainerID"])
            UpsertContainerDto.UnstuffDate = UnstuffDate
            UpsertContainerDto.IsUnStuff = Dto["IsUnStuff"]
            UpsertContainerDto.IsActive = True
            UpsertContainerDto.UpdateDate = datetime.now(tz=timezone.utc)
            UpsertContainerDto.UpdateBy = None
            UpsertContainerDto.save()
            ContainerID = Dto["ContainerID"]

            if Dto["HblID"] != None:
                UpsertHblDto = Hbl.objects.get(ID=Dto["HblID"])
                UpsertHblDto.MarkDesc = Dto["MarkDesc"]
                UpsertHblDto.Transhipment = Dto["Transhipment"]
                UpsertHblDto.Port = PortDto
                UpsertHblDto.PackageDesc = Dto["PackageDesc"]
                UpsertHblDto.LocationDesc = Dto["LocationDesc"]
                UpsertHblDto.Remarks = Dto["Remarks"]
                UpsertHblDto.InwardSurvey = Dto["InwardSurvey"]
                UpsertHblDto.HeavyLiftCargo = Dto["HeavyLiftCargo"]
                UpsertHblDto.LongLengthCargo = Dto["LongLengthCargo"]
                UpsertHblDto.PortPolice = Dto["PortPolice"]
                UpsertHblDto.CargoSurvey = Dto["CargoSurvey"]
                UpsertHblDto.MaqisHold = Dto["MaqisHold"]
                UpsertHblDto.HealthHold = Dto["HealthHold"]
                UpsertHblDto.PreventiveHold = Dto["PreventiveHold"]
                UpsertHblDto.CustomsHold = Dto["CustomsHold"]
                UpsertHblDto.IsActive = True
                UpsertHblDto.UpdateDate = datetime.now(tz=timezone.utc)
                UpsertHblDto.UpdateBy = None
                UpsertHblDto.save()
                rtn = True
                HblID = Dto["HblID"]
            else:
                rtn = True

        except Exception as e:
            print(e)

        return {"rtn": rtn, "ContainerID": ContainerID, "HblID": HblID}

    def UpsertInvoice(Dto):
        rtn = False
        InvoiceID = None
        HblDto = None
        ConsigneeDto = None
        UpsertDto = None

        try:
            HblDto = Hbl.objects.get(ID=Dto["HblID"])
            ConsigneeDto = Customer.objects.get(ID=Dto["ConsigneeID"])

            if Dto["InvoiceID"] == None:

                UpsertDto = Invoice.objects.create(
                    No=Dto["No"],
                    IssueDate=Dto["IssueDate"],
                    Hbl=HblDto,
                    StorageDay=Dto["StorageDay"],
                    IsPartial=Dto["IsPartial"],
                    IssuedQuantity=Dto["IssuedQuantity"],
                    IssuedWeight=Dto["IssuedWeight"],
                    IssuedVolume=Dto["IssuedVolume"],
                    BalanceQuantity=Dto["BalanceQuantity"] - Dto["IssuedQuantity"],
                    BalanceWeight=Dto["BalanceWeight"] - Dto["IssuedWeight"],
                    BalanceVolume=Dto["BalanceVolume"] - Dto["IssuedVolume"],
                    Consignee=ConsigneeDto,
                    IidNo=Dto["IidNo"],
                    PaymentType=Dto["PaymentType"],
                    RefNo=Dto["RefNo"],
                    IsActive=True,
                    CreateDate=datetime.now(tz=timezone.utc),
                    CreateBy=None,
                    UpdateDate=datetime.now(tz=timezone.utc),
                    UpdateBy=None,
                )

                if UpsertDto.ID:
                    rtn = True
                    InvoiceID = UpsertDto.ID

            else:
                UpsertDto = Invoice.objects.get(ID=Dto["InvoiceID"])
                UpsertDto.Consignee = ConsigneeDto
                UpsertDto.IidNo = Dto["IidNo"]
                UpsertDto.PaymentType = Dto["PaymentType"]
                UpsertDto.RefNo = Dto["RefNo"]
                UpsertDto.IsActive = True
                UpsertDto.UpdateDate = datetime.now(tz=timezone.utc)
                UpsertDto.UpdateBy = None
                UpsertDto.save()
                rtn = True
                InvoiceID = Dto["InvoiceID"]

        except Exception as e:
            print(e)

        return {"rtn": rtn, "InvoiceID": InvoiceID}

    def UpdateInvoiceAmount(InvoiceID):
        rtn = False
        TotalInvoiceAmount = 0.00
        TotalInvoiceAmountWord = ""

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT COALESCE(SUM("Amount"), 0) AS "TotalInvoiceAmount" FROM "imp_InvoiceItem" iii WHERE "InvoiceID" = %s AND "IsActive" = TRUE""",
                    [InvoiceID],
                )
                TotalInvoiceAmount = cursor.fetchone()[0]

                if TotalInvoiceAmount > 0:
                    TotalInvoiceAmountWord = "RINGGIT MALAYSIA " + sysBL.ConvertToWords(
                        sysBL, "{:.2f}".format(TotalInvoiceAmount)
                    )

                cursor.execute(
                    """UPDATE "imp_Invoice" SET "Amount" = %s, "AmountWord" = %s WHERE "ID" = %s""",
                    [
                        0 if TotalInvoiceAmount == None else TotalInvoiceAmount,
                        TotalInvoiceAmountWord,
                        InvoiceID,
                    ],
                )
                rtn = True

        except Exception as e:
            print(e)

        return rtn

    def UpsertDefaultInvoiceItem(Dto):
        rtn = False
        InvoiceDto = None
        ItemDto = None
        UpsertDto = None

        try:
            InvoiceDto = Invoice.objects.get(ID=uuid.UUID(Dto.InvoiceID))
            ItemDto = Item.objects.get(ID=uuid.UUID(Dto.ItemID))

            UpsertDto = InvoiceItem.objects.create(
                Invoice=InvoiceDto,
                Item=ItemDto,
                Quantity=Dto.ItemQuantity,
                UnitAmount=Dto.ItemUnitAmount,
                Amount=Dto.ItemAmount,
                IsDefault=True,
                IsActive=True,
                CreateDate=datetime.now(tz=timezone.utc),
                CreateBy=None,
                UpdateDate=datetime.now(tz=timezone.utc),
                UpdateBy=None,
            )

            if UpsertDto.ID:
                rtn = True

        except Exception as e:
            print(e)

        return rtn

    def UpsertInvoiceItem(
        InvoiceID, InvoiceItemID, ItemID, ItemQuantity, ItemUnitAmount
    ):
        rtn = False
        InvoiceDto = None
        ItemDto = None
        UpsertDto = None

        try:
            InvoiceDto = Invoice.objects.get(ID=InvoiceID)
            ItemDto = Item.objects.get(ID=ItemID)

            if InvoiceItemID == None:

                UpsertDto = InvoiceItem.objects.create(
                    Invoice=InvoiceDto,
                    Item=ItemDto,
                    Quantity=ItemQuantity,
                    UnitAmount=ItemUnitAmount,
                    Amount=ItemQuantity * ItemUnitAmount,
                    IsDefault=False,
                    IsActive=True,
                    CreateDate=datetime.now(tz=timezone.utc),
                    CreateBy=None,
                    UpdateDate=datetime.now(tz=timezone.utc),
                    UpdateBy=None,
                )

                if UpsertDto.ID:
                    rtn = True

            else:
                UpsertDto = InvoiceItem.objects.get(ID=InvoiceItemID)
                UpsertDto.Item = ItemDto
                UpsertDto.Quantity = ItemQuantity
                UpsertDto.UnitAmount = ItemUnitAmount
                UpsertDto.Amount = ItemQuantity * ItemUnitAmount
                UpsertDto.IsActive = True
                UpsertDto.UpdateDate = datetime.now(tz=timezone.utc)
                UpsertDto.UpdateBy = None
                UpsertDto.save()
                rtn = True

        except Exception as e:
            print(e)

        return rtn

    def DeleteObl(OblID):
        rtn = False

        try:
            OblDto = Obl.objects.get(ID=OblID)
            OblDto.IsActive = False
            OblDto.UpdateDate = datetime.now(tz=timezone.utc)
            OblDto.UpdateBy = None
            OblDto.save()
            rtn = True
        except Exception as e:
            print(e)

        return rtn

    def DeleteContainer(ContainerID):
        rtn = False

        try:
            ContainerDto = Container.objects.get(ID=ContainerID)
            ContainerDto.IsActive = False
            ContainerDto.UpdateDate = datetime.now(tz=timezone.utc)
            ContainerDto.UpdateBy = None
            ContainerDto.save()
            rtn = True
        except Exception as e:
            print(e)

        return rtn

    def DeleteHbl(HblID):
        rtn = False

        try:
            HblDto = Hbl.objects.get(ID=HblID)
            HblDto.IsActive = False
            HblDto.UpdateDate = datetime.now(tz=timezone.utc)
            HblDto.UpdateBy = None
            HblDto.save()
            rtn = True
        except Exception as e:
            print(e)

        return rtn

    def DeleteInvoice(InvoiceID, DeleteRemark):
        rtn = False
        HblQuantity = 0
        HblWeight = 0
        HblVolume = 0

        try:
            InvoiceDto = Invoice.objects.get(ID=InvoiceID)
            InvoiceDto.DeleteRemark = DeleteRemark
            InvoiceDto.IsActive = False
            InvoiceDto.UpdateDate = datetime.now(tz=timezone.utc)
            InvoiceDto.UpdateBy = None
            InvoiceDto.save()

            HblQuantity = InvoiceDto.Hbl.Quantity
            HblWeight = InvoiceDto.Hbl.Weight
            HblVolume = InvoiceDto.Hbl.Volume

            InvoiceByHblDto = Invoice.objects.filter(
                Hbl__ID=InvoiceDto.Hbl.ID, IsActive=True
            )

            for Record in InvoiceByHblDto:
                UpsertDto = Invoice.objects.get(ID=Record.ID)
                UpsertDto.IsPartial = True
                UpsertDto.BalanceQuantity = HblQuantity - UpsertDto.IssuedQuantity
                UpsertDto.BalanceWeight = HblWeight - UpsertDto.IssuedWeight
                UpsertDto.BalanceVolume = HblVolume - UpsertDto.IssuedVolume
                UpsertDto.UpdateDate = datetime.now(tz=timezone.utc)
                UpsertDto.UpdateBy = None
                UpsertDto.save()

                HblQuantity -= UpsertDto.IssuedQuantity
                HblWeight -= UpsertDto.IssuedWeight
                HblVolume -= UpsertDto.IssuedVolume

            InvoiceItemDtos = InvoiceItem.objects.filter(Invoice__ID=InvoiceID)

            for Record in InvoiceItemDtos:
                UpsertDto = InvoiceItem.objects.get(ID=Record.ID)
                UpsertDto.IsActive = False
                UpsertDto.UpdateDate = datetime.now(tz=timezone.utc)
                UpsertDto.UpdateBy = None
                UpsertDto.save()

            rtn = True
        except Exception as e:
            print(e)

        return rtn

    def DeleteDefaultInvoiceItem(InvoiceID):
        rtn = False

        try:
            DeleteDto = InvoiceItem.objects.filter(
                IsDefault=True, Invoice__ID=InvoiceID
            ).delete()
            rtn = True if DeleteDto[0] > 0 else False
        except Exception as e:
            print(e)

        return rtn

    def DeleteInvoiceItem(InvoiceItemID):
        rtn = False

        try:
            InvoiceItemDto = InvoiceItem.objects.get(ID=InvoiceItemID)
            InvoiceItemDto.IsActive = False
            InvoiceItemDto.UpdateDate = datetime.now(tz=timezone.utc)
            InvoiceItemDto.UpdateBy = None
            InvoiceItemDto.save()
            rtn = True
        except Exception as e:
            print(e)

        return rtn
