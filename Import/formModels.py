from django import forms
from Import.models import Obl, Container, Hbl


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


class HblFormModel(forms.ModelForm):
    HblID = forms.UUIDField(required=False)
    No = forms.CharField(max_length=50, required=False)
    OblID = forms.UUIDField(required=False)
    OblNo = forms.CharField(max_length=250, required=False)
    ContainerID = forms.UUIDField(required=False)
    ContainerNo = forms.CharField(max_length=50, required=False)
    ConsigneeID = forms.UUIDField(required=False)
    ConsigneeName = forms.CharField(max_length=250, required=False)
    ClassID = forms.UUIDField(required=False)
    ClassFullName = forms.CharField(max_length=250, required=False)
    UnitID = forms.UUIDField(required=False)
    UnitShortName = forms.CharField(max_length=50, required=False)
    PortID = forms.UUIDField(required=False)
    PortName = forms.CharField(max_length=250, required=False)
    Quantity = forms.IntegerField(required=False)
    Weight = forms.DecimalField(max_digits=6, decimal_places=3, required=False)
    Volume = forms.DecimalField(max_digits=6, decimal_places=3, required=False)
    Transhipment = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )
    MarkDesc = forms.CharField(widget=forms.Textarea(), required=False)
    CargoDesc = forms.CharField(widget=forms.Textarea(), required=False)

    class Meta:
        model = Hbl
        fields = [
            "HblID",
            "No",
            "OblID",
            "OblNo",
            "ContainerID",
            "ContainerNo",
            "ConsigneeID",
            "ConsigneeName",
            "ClassID",
            "ClassFullName",
            "UnitID",
            "UnitShortName",
            "PortID",
            "PortName",
            "Quantity",
            "Weight",
            "Volume",
            "Transhipment",
            "MarkDesc",
            "CargoDesc",
        ]


class UnstuffContainerFormModel(forms.ModelForm):
    ContainerID = forms.UUIDField(required=False)
    ContainerNo = forms.CharField(max_length=50, required=False)
    UnstuffDate = forms.DateField(required=False)
    IsUnStuff = forms.BooleanField(required=False)
    HblID = forms.UUIDField(required=False)
    No = forms.CharField(max_length=50, required=False)
    ConsigneeName = forms.CharField(max_length=250, required=False)
    ClassFullName = forms.CharField(max_length=250, required=False)
    UnitShortName = forms.CharField(max_length=50, required=False)
    PortID = forms.UUIDField(required=False)
    PortName = forms.CharField(max_length=250, required=False)
    Quantity = forms.IntegerField(required=False)
    Weight = forms.DecimalField(max_digits=6, decimal_places=3, required=False)
    Volume = forms.DecimalField(max_digits=6, decimal_places=3, required=False)
    Transhipment = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )
    MarkDesc = forms.CharField(widget=forms.Textarea(), required=False)
    CargoDesc = forms.CharField(widget=forms.Textarea(), required=False)
    PackageDesc = forms.CharField(widget=forms.Textarea(), required=False)
    LocationDesc = forms.CharField(widget=forms.Textarea(), required=False)
    InwardSurvey = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.RadioSelect(),
    )
    Remarks = forms.CharField(widget=forms.Textarea(), required=False)
    HeavyLiftCargo = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )
    LongLengthCargo = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )
    PortPolice = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )
    CargoSurvey = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )
    MaqisHold = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )
    HealthHold = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )
    PreventiveHold = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )
    CustomsHold = forms.ChoiceField(
        choices=[(0, "No"), (1, "Yes")], widget=forms.RadioSelect()
    )

    class Meta:
        model = Hbl
        fields = [
            "ContainerID",
            "ContainerNo",
            "UnstuffDate",
            "IsUnStuff",
            "HblID",
            "No",
            "ConsigneeName",
            "ClassFullName",
            "UnitShortName",
            "PortID",
            "PortName",
            "Quantity",
            "Weight",
            "Volume",
            "Transhipment",
            "MarkDesc",
            "CargoDesc",
            "InwardSurvey",
            "PackageDesc",
            "LocationDesc",
            "Remarks",
            "HeavyLiftCargo",
            "LongLengthCargo",
            "PortPolice",
            "CargoSurvey",
            "MaqisHold",
            "HealthHold",
            "PreventiveHold",
            "CustomsHold",
        ]
