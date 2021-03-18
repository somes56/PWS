from django.db import models
from datetime import datetime
import uuid

class Country(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=150, null=True)
    IsoCode = models.CharField(max_length=2, null=True)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = 'mst_Country'

class Term(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50, null=True)
    Type = models.IntegerField()
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)
    
    class Meta:
        db_table = 'mst_Term'

class State(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50, null=True)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)

    class Meta:
        db_table = 'mst_State'

class Customer(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=250)
    Pic = models.CharField(max_length=100, null=True, default=None)
    MobileNo = models.CharField(max_length=25, null=True, default=None)
    TelNo =  models.CharField(max_length=25, null=True, default=None)
    FaxNo = models.CharField(max_length=25, null=True, default=None)
    Email = models.CharField(max_length=50, null=True, default=None)
    Address = models.TextField()
    City = models.CharField(max_length=100, null=True, default=None)
    PostCode = models.IntegerField(default=0)
    State = models.ForeignKey(State, db_column='StateID', on_delete=models.PROTECT, unique=False, null=True, default=None)
    Country = models.ForeignKey(Country, db_column='CountryID', on_delete=models.PROTECT, unique=False, null=True, default=None)
    Term = models.ForeignKey(Term, db_column='TermID', on_delete=models.PROTECT, unique=False, null=True, default=None)
    LimitAmount = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0)
    IsAllowInvoice = models.BooleanField(default=False)
    IsAllowDo = models.BooleanField(default=False)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)
    
    class Meta:
        db_table = 'mst_Customer'

class Port(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=10)
    Name = models.CharField(max_length=250)
    Country = models.ForeignKey(Country, db_column='CountryID', on_delete=models.PROTECT, unique=False, null=True, default=None)
    IsSpecial = models.BooleanField(default=False)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)
    
    class Meta:
        db_table = 'mst_Port'
        
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
        db_table = 'mst_Unit'
        
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
        db_table = 'mst_ContainerSize'
        
class Vessel(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Code = models.CharField(max_length=10)
    Name = models.CharField(max_length=250)
    PortOperator = models.ForeignKey(Customer, db_column='PortOperatorID', related_name='PortOperator', on_delete=models.PROTECT, unique=False, null=True, default=None)
    Psa = models.ForeignKey(Customer, db_column='PsaID', related_name='Psa', on_delete=models.PROTECT, unique=False, null=True, default=None)
    ShippingAgent = models.ForeignKey(Customer, db_column='ShippingAgentID', related_name='ShippingAgent', on_delete=models.PROTECT, unique=False, null=True, default=None)
    IsActive = models.BooleanField(default=False)
    CreateDate = models.DateTimeField(null=True, default=datetime.today())
    CreateBy = models.UUIDField(null=True)
    UpdateDate = models.DateTimeField(null=True, default=datetime.today())
    UpdateBy = models.UUIDField(null=True)
    
    class Meta:
        db_table = 'mst_Vessel'

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
        db_table = 'mst_Item'

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
        db_table = 'mst_Class'
