from django import forms
from Import.models import Obl


class OblFormModel(forms.ModelForm):
    OblID = forms.UUIDField(required=False)
    No = forms.CharField(max_length=250, required=False)
    VoyageID = forms.UUIDField(required=False)
    VoyageNo = forms.CharField(max_length=15, required=False)
    ShipCallNo = forms.CharField(max_length=15, required=False)
    VesselCode = forms.CharField(max_length=10, required=False)
    LoadPortID = forms.UUIDField(required=False)
    LoadPortName = forms.CharField(max_length=250, required=False)
    UnLoadPortID = forms.UUIDField(required=False)
    UnLoadPortName = forms.CharField(max_length=250, required=False)
    DestinationPortID = forms.UUIDField(required=False)
    DestionationPortName = forms.CharField(max_length=250, required=False)
    ShippingAgentID = forms.UUIDField(required=False)
    ShippingAgentName = forms.CharField(max_length=250, required=False)
    ConsigneeID = forms.UUIDField(required=False)
    ConsigneeName = forms.CharField(max_length=250, required=False)

    class Meta:
        model = Obl
        fields = [
            "OblID",
            "No",
            "VoyageID",
            "VoyageNo",
            "ShipCallNo",
            "VesselCode",
            "LoadPortID",
            "LoadPortName",
            "UnLoadPortID",
            "UnLoadPortName",
            "DestinationPortID",
            "DestionationPortName",
            "ShippingAgentID",
            "ShippingAgentName",
            "ConsigneeID",
            "ConsigneeName",
        ]
