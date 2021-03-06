from django import forms
from Master.models import Customer

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
        fields = ['CustomerID', 'Name', 'Pic', 'MobileNo', 'TelNo', 'FaxNo', 'Email', 'Address', 'City', 'PostCode', 'StateID', 'StateName', 'CountryID', 'CountryName', 'TermID', 'TermName', 'LimitAmount', 'IsAllowInvoice', 'IsAllowDo']