from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from Import.models import Obl, Container, Hbl
from Master.models import Voyage, Port, Customer, ContainerSize, Class, Unit


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
            PortDto = Port.objects.get(ID=Dto["PortID"])

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
