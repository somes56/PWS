from django import forms
from Master.models import Customer, Port, Unit, ContainerSize, Vessel, Item

class CustomerFormModel(forms.ModelForm):
    CustomerID = forms.UUIDField(required=False)
    Name = forms.CharField(max_length=250, required=False)
    Pic = forms.CharField(max_length=100, required=False)
    MobileNo = forms.CharField(max_length=25, required=False)
    TelNo =  forms.CharField(max_length=25, required=False)
    FaxNo = forms.CharField(max_length=25, required=False)
    Email = forms.CharField(max_length=50, required=False)
    Address = forms.CharField(widget=forms.Textarea(), required=False)
    City = forms.CharField(max_length=100, required=False)
    PostCode = forms.IntegerField(required=False)
    StateID = forms.UUIDField(required=False)
    StateName = forms.CharField(max_length=50, required=False)
    CountryID = forms.UUIDField(required=False)
    CountryName = forms.CharField(max_length=50, required=False)
    TermID = forms.UUIDField(required=False)
    TermName = forms.CharField(max_length=50, required=False)
    LimitAmount = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    IsAllowInvoice = forms.BooleanField(required=False)
    IsAllowDo = forms.BooleanField(required=False)

    class Meta:
        model = Customer
        fields = ['CustomerID', 'Name', 'Pic', 'MobileNo', 'TelNo', 'FaxNo', 'Email', 
                  'Address', 'City', 'PostCode', 'StateID', 'StateName', 'CountryID', 
                  'CountryName', 'TermID', 'TermName', 'LimitAmount', 'IsAllowInvoice', 'IsAllowDo']

class PortFormModel(forms.ModelForm):
    PortID = forms.UUIDField(required=False)
    Code = forms.CharField(max_length=10, required=False)
    Name = forms.CharField(max_length=250, required=False)
    CountryID = forms.UUIDField(required=False)
    CountryName = forms.CharField(max_length=50, required=False)
    IsSpecial = forms.BooleanField(required=False)
    
    class Meta:
        model = Port
        fields = ['PortID', 'Code', 'Name', 'CountryID', 'CountryName', 'IsSpecial']

class UnitFormModel(forms.ModelForm):
    UnitID = forms.UUIDField(required=False)
    Code = forms.CharField(max_length=10, required=False)
    ShortName = forms.CharField(max_length=50, required=False)
    FullName = forms.CharField(max_length=250, required=False)

    class Meta:
        model = Unit
        fields = ['UnitID', 'Code', 'ShortName', 'FullName']
        
class ContainerSizeFormModel(forms.ModelForm):
    ContainerSizeID = forms.UUIDField(required=False)
    Code = forms.CharField(max_length=10, required=False)
    Name = forms.CharField(max_length=250, required=False)
    Teus = forms.ChoiceField(choices=[(0,0), (1,1), (2,2)], widget=forms.RadioSelect())
    
    class Meta:
        model = ContainerSize
        fields = ['ContainerSizeID', 'Code', 'Name', 'Teus']

class VesselFormModel(forms.ModelForm):
    VesselID = forms.UUIDField(required=False)
    Code = forms.CharField(max_length=10, required=False)
    Name = forms.CharField(max_length=250, required=False)
    PortOperatorID = forms.UUIDField(required=False)
    PortOperatorName = forms.CharField(max_length=250, required=False)
    PsaID = forms.UUIDField(required=False)
    PsaName = forms.CharField(max_length=250, required=False)
    ShippingAgentID = forms.UUIDField(required=False)
    ShippingAgentName = forms.CharField(max_length=250, required=False)

    class Meta:
        model = Vessel
        fields = ['VesselID', 'Code', 'Name', 'PortOperatorID', 'PortOperatorName', 'PsaID', 'PsaName',
                  'ShippingAgentID', 'ShippingAgentName']

class ItemFormModel(forms.ModelForm):
    ItemID = forms.UUIDField(required=False)
    Code = forms.CharField(max_length=10, required=False)
    Name = forms.CharField(max_length=250, required=False)

    class Meta:
        model = Unit
        fields = ['ItemID', 'Code', 'Name']