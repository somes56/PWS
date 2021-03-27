from django.db import models
from datetime import datetime
from Master.models import Voyage, Port, Customer
import uuid


class Obl(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    No = models.CharField(max_length=250)
    Voyage = models.ForeignKey(
        Voyage,
        db_column="VoyageID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    LoadPort = models.ForeignKey(
        Port,
        db_column="LoadPortID",
        related_name="LoadPort",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    UnloadPort = models.ForeignKey(
        Port,
        db_column="UnloadPortID",
        related_name="UnloadPort",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    DestinationPort = models.ForeignKey(
        Port,
        db_column="DestinationPortID",
        related_name="DestinationPort",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    ShippingAgent = models.ForeignKey(
        Customer,
        db_column="ShippingAgentID",
        related_name="OblShippingAgent",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Consignee = models.ForeignKey(
        Customer,
        db_column="ConsigneeID",
        related_name="Consignee",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "imp_Obl"