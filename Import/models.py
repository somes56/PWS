from django.db import models
from datetime import datetime
from Master.models import Item, Voyage, Port, Customer, ContainerSize, Class, Unit
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


class Container(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    No = models.CharField(max_length=50)
    Obl = models.ForeignKey(
        Obl,
        db_column="OblID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    SealNo = models.CharField(max_length=50, null=True, default="")
    ContainerSize = models.ForeignKey(
        ContainerSize,
        db_column="ContainerSizeID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Type = models.IntegerField(default=0)
    Status = models.IntegerField(default=0)
    ShipType = models.IntegerField(default=0)
    Movement = models.IntegerField(default=0)
    SealParty = models.IntegerField(default=0)
    Supplier = models.IntegerField(default=0)
    IsUnStuff = models.BooleanField(default=False)
    UnstuffDate = models.DateField(null=True)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "imp_Container"


class Hbl(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    No = models.CharField(max_length=50)
    Obl = models.ForeignKey(
        Obl,
        db_column="OblID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Container = models.ForeignKey(
        Container,
        db_column="ContainerID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Consignee = models.ForeignKey(
        Customer,
        db_column="ConsigneeID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Class = models.ForeignKey(
        Class,
        db_column="ClassID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Unit = models.ForeignKey(
        Unit,
        db_column="UnitID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Port = models.ForeignKey(
        Port,
        db_column="PortID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Quantity = models.IntegerField(default=0)
    Weight = models.DecimalField(max_digits=18, decimal_places=3, null=True, default=0)
    Volume = models.DecimalField(max_digits=18, decimal_places=3, null=True, default=0)
    Transhipment = models.IntegerField(default=0)
    InwardSurvey = models.IntegerField(default=0)
    MarkDesc = models.CharField(max_length=250, null=True, default="")
    PackageDesc = models.CharField(max_length=250, null=True, default="")
    LocationDesc = models.CharField(max_length=250, null=True, default="")
    CargoDesc = models.CharField(max_length=250, null=True, default="")
    Remarks = models.CharField(max_length=250, null=True, default="")
    HeavyLiftCargo = models.IntegerField(default=0)
    LongLengthCargo = models.IntegerField(default=0)
    PortPolice = models.IntegerField(default=0)
    CargoSurvey = models.IntegerField(default=0)
    MaqisHold = models.IntegerField(default=0)
    HealthHold = models.IntegerField(default=0)
    PreventiveHold = models.IntegerField(default=0)
    CustomsHold = models.IntegerField(default=0)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "imp_Hbl"


class Invoice(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    No = models.CharField(max_length=50)
    IssueDate = models.DateField(null=True)
    Hbl = models.ForeignKey(
        Hbl,
        db_column="HblID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    StorageDay = models.IntegerField(default=0)
    IsPartial = models.BooleanField(default=False)
    IssuedQuantity = models.IntegerField(default=0)
    IssuedWeight = models.DecimalField(
        max_digits=18, decimal_places=3, null=True, default=0
    )
    IssuedVolume = models.DecimalField(
        max_digits=18, decimal_places=3, null=True, default=0
    )
    BalanceQuantity = models.IntegerField(default=0)
    BalanceWeight = models.DecimalField(
        max_digits=18, decimal_places=3, null=True, default=0
    )
    BalanceVolume = models.DecimalField(
        max_digits=18, decimal_places=3, null=True, default=0
    )
    Consignee = models.ForeignKey(
        Customer,
        db_column="ConsigneeID",
        related_name="InvoiceConsignee",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    IidNo = models.CharField(max_length=50)
    PaymentType = models.IntegerField(default=0)
    RefNo = models.CharField(max_length=50)
    Amount = models.DecimalField(max_digits=18, decimal_places=2, null=True, default=0)
    AmountWord = models.TextField(null=True, default="")
    DeleteRemark = models.CharField(max_length=250, null=True, default="")
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "imp_Invoice"

class InvoiceItem(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Invoice = models.ForeignKey(
        Invoice,
        db_column="InvoiceID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Item = models.ForeignKey(
        Item,
        db_column="ItemID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Quantity = models.IntegerField(default=0)
    UnitAmount = models.DecimalField(max_digits=18, decimal_places=2, null=True, default=0)
    Amount = models.DecimalField(max_digits=18, decimal_places=2, null=True, default=0)
    IsDefault = models.BooleanField(default=False)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "imp_InvoiceItem"