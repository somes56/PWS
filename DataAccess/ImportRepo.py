from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from Import.models import Obl, Container
from Master.models import Voyage, Port, Customer, ContainerSize


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
