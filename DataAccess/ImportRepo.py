from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from Import.models import Obl
from Master.models import Voyage, Port, Customer


class importRepo:
    def PartialOblList(SearchBy=""):
        Obls = []

        try:
            Obls = Obl.objects.filter(IsActive=True, No__icontains=SearchBy).order_by(
                "No"
            )[:100]
        except Exception as e:
            print(e)

        return Obls

    def LoadObl(OblID):
        OblDto = Obl()

        try:
            OblDto = Obl.objects.get(ID=OblID, IsActive=True)
        except Exception as e:
            print(e)

        return OblDto

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
