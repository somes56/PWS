from django.db import models
from datetime import datetime
import uuid


class Country(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=150, null=True, default="")
    IsoCode = models.CharField(max_length=2, null=True, default="")
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_Country"


class Term(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50, null=True, default="")
    Type = models.IntegerField()
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_Term"


class State(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50, null=True, default="")
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_State"


class Customer(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=250)
    Pic = models.CharField(max_length=100, null=True, default="")
    MobileNo = models.CharField(max_length=25, null=True, default="")
    TelNo = models.CharField(max_length=25, null=True, default="")
    FaxNo = models.CharField(max_length=25, null=True, default="")
    Email = models.CharField(max_length=50, null=True, default="")
    Address = models.TextField()
    City = models.CharField(max_length=100, null=True, default="")
    PostCode = models.CharField(max_length=10, null=True, default="")
    State = models.ForeignKey(
        State,
        db_column="StateID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Country = models.ForeignKey(
        Country,
        db_column="CountryID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Term = models.ForeignKey(
        Term,
        db_column="TermID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    LimitAmount = models.DecimalField(
        max_digits=18, decimal_places=2, null=True, default=0
    )
    IsAllowInvoice = models.BooleanField(default=False)
    IsAllowDo = models.BooleanField(default=False)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_Customer"


class Port(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=10)
    Name = models.CharField(max_length=250)
    Country = models.ForeignKey(
        Country,
        db_column="CountryID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    IsSpecial = models.BooleanField(default=False)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_Port"


class Unit(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=10)
    ShortName = models.CharField(max_length=50)
    FullName = models.CharField(max_length=250)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_Unit"


class ContainerSize(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=10)
    Name = models.CharField(max_length=250)
    Teus = models.IntegerField(default=0)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_ContainerSize"


class Vessel(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=10)
    Name = models.CharField(max_length=250)
    PortOperator = models.ForeignKey(
        Customer,
        db_column="PortOperatorID",
        related_name="PortOperator",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Psa = models.ForeignKey(
        Customer,
        db_column="PsaID",
        related_name="Psa",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    ShippingAgent = models.ForeignKey(
        Customer,
        db_column="ShippingAgentID",
        related_name="ShippingAgent",
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
        db_table = "mst_Vessel"


class Item(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=10)
    Name = models.CharField(max_length=250)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_Item"


class Class(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=10)
    ShortName = models.CharField(max_length=25)
    FullName = models.CharField(max_length=250)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_Class"


class Voyage(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    No = models.CharField(max_length=15)
    ShipCallNo = models.CharField(max_length=15)
    Vessel = models.ForeignKey(
        Vessel,
        db_column="VesselID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Eta = models.DateField(null=True)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_Voyage"


class Operator(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=15)
    Name = models.CharField(max_length=100)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_Operator"


class SysCompany(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=2)  ##HQ,WP,NP
    Name = models.CharField(max_length=100)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "sys_Company"


class SysRunningNoHist(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Company = models.ForeignKey(
        SysCompany,
        db_column="CompanyID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    AccountType = models.CharField(
        max_length=2
    )  # Invoice(IN),Credit Note(CN),DebitNote(DN), Export Invoice(EN), Container Shipping Note (CS)
    RollNo = models.IntegerField(default=0)
    LastYear = models.IntegerField(default=0)
    LastMonth = models.IntegerField(default=0)
    LastDay = models.IntegerField(default=0)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "sys_RunningNoHist"


class DefaultItem(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    AccountType = models.CharField(
        max_length=2
    )  # Invoice(IN),Credit Note(CN),DebitNote(DN), Export Invoice(EN), All(AN)
    Code = models.CharField(max_length=15)
    Item = models.ForeignKey(
        Item,
        db_column="ItemID",
        on_delete=models.PROTECT,
        unique=False,
        null=True,
        default=None,
    )
    Amount = models.DecimalField(max_digits=18, decimal_places=2, null=True, default=0)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = "mst_DefaultItem"