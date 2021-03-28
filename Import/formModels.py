from django import forms
from Import.models import Obl, Container


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


class ContainerFormModel(forms.ModelForm):
    ContainerID = forms.UUIDField(required=False)
    No = forms.CharField(max_length=50, required=False)
    OblID = forms.UUIDField(required=False)
    OblNo = forms.CharField(max_length=250, required=False)
    SealNo = forms.CharField(max_length=50, required=False)
    ContainerSizeID = forms.UUIDField(required=False)
    ContainerSizeName = forms.CharField(max_length=250, required=False)
    Type = forms.ChoiceField(
        choices=[
            (0, "Container"),
            (1, "Break Bulk"),
            (2, "Bulk Cargo"),
            (3, "Bonded Truck"),
        ],
        widget=forms.RadioSelect(),
    )
    Status = forms.ChoiceField(
        choices=[(0, "Empty"), (1, "Full")], widget=forms.RadioSelect()
    )
    ShipType = forms.ChoiceField(
        choices=[(0, "Lcl"), (1, "Fcl"), (2, "Coload")], widget=forms.RadioSelect()
    )
    Movement = forms.ChoiceField(
        choices=[
            (0, "Export"),
            (1, "Import"),
            (2, "R/Board"),
            (3, "T/Ship"),
            (4, "T/Rail"),
        ],
        widget=forms.RadioSelect(),
    )
    SealParty = forms.ChoiceField(
        choices=[(0, "Carrier"), (1, "Shipper"), (2, "T/Operator"), (3, "Customer")],
        widget=forms.RadioSelect(),
    )
    Supplier = forms.ChoiceField(
        choices=[(0, "Contractor"), (1, "Port Operator")], widget=forms.RadioSelect()
    )

    class Meta:
        model = Container
        fields = [
            "ContainerID",
            "No",
            "OblID",
            "OblNo",
            "SealNo",
            "ContainerSizeID",
            "ContainerSizeName",
            "Type",
            "Status",
            "ShipType",
            "Movement",
            "SealParty",
            "Supplier",
        ]
