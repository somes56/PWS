from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.utils import timezone
from BusinessLogic.MasterBL import mstBL
from DataAccess.PWSRepo import pwsRepo
from Master.formModels import (
    CustomerFormModel,
    PortFormModel,
    UnitFormModel,
    ContainerSizeFormModel,
    VesselFormModel,
    ItemFormModel,
    ClassFormModel,
    VoyageFormModel,
)
from Master.models import Country, Customer, State, Term


def CustomerList(request):
    return render(request, "Customer.html")


def PartialCustomerList(request, SearchBy=""):
    Customers = []
    Customers = pwsRepo.PartialCustomerList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Customers, 50)

    try:
        CustomerPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        CustomerPaginator = _Paginator.page(1)
    except EmptyPage:
        CustomerPaginator = _Paginator.page(paginator.num_pages)

    return render(request, "PartialCustomerList.html", {"Customers": CustomerPaginator})


@csrf_exempt
def CustomerForm(request, CustomerID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        customerFormModel = CustomerFormModel()

        if CustomerID == None:
            customerFormModel = mstBL.InitialiseCustomerFormModel(None)
        else:
            customerFormModel = mstBL.InitialiseCustomerFormModel(CustomerID)

        return render(
            request,
            "CustomerForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": customerFormModel,
            },
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        customerFormModel = CustomerFormModel()
        _post = CustomerFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertCustomer(_Form)

            if _Form["CustomerID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                customerFormModel = mstBL.InitialiseCustomerFormModel(
                    UpsertResult["CustomerID"]
                )

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                customerFormModel = mstBL.InitialiseErrorCustomerFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "CustomerForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": customerFormModel,
            },
        )


@csrf_exempt
def DeleteCustomer(request, CustomerID=None):
    rtn = False

    if request.method == "POST":
        rtn = pwsRepo.DeleteCustomer(CustomerID)
    else:
        rtn = False
    return HttpResponse(rtn)


def PortList(request):
    return render(request, "Port.html")


def PartialPortList(request, SearchBy=""):
    Ports = []
    Ports = pwsRepo.PartialPortList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Ports, 50)

    try:
        PortPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        PortPaginator = _Paginator.page(1)
    except EmptyPage:
        PortPaginator = _Paginator.page(paginator.num_pages)

    return render(request, "PartialPortList.html", {"Ports": PortPaginator})


@csrf_exempt
def PortForm(request, PortID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        portFormModel = PortFormModel()

        if PortID == None:
            portFormModel = mstBL.InitialisePortFormModel(None)
        else:
            portFormModel = mstBL.InitialisePortFormModel(PortID)

        return render(
            request,
            "PortForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": portFormModel},
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        portFormModel = PortFormModel()
        _post = PortFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertPort(_Form)

            if _Form["PortID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                portFormModel = mstBL.InitialisePortFormModel(UpsertResult["PortID"])

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                portFormModel = mstBL.InitialiseErrorPortFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "PortForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": portFormModel},
        )


@csrf_exempt
def DeletePort(request, PortID=None):
    rtn = False

    if request.method == "POST":
        rtn = pwsRepo.DeletePort(PortID)
    else:
        rtn = False
    return HttpResponse(rtn)


def UnitList(request):
    return render(request, "Unit.html")


def PartialUnitList(request, SearchBy=""):
    Units = []
    Units = pwsRepo.PartialUnitList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Units, 50)

    try:
        UnitPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        UnitPaginator = _Paginator.page(1)
    except EmptyPage:
        UnitPaginator = _Paginator.page(paginator.num_pages)

    return render(request, "PartialUnitList.html", {"Units": UnitPaginator})


@csrf_exempt
def UnitForm(request, UnitID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        unitFormModel = UnitFormModel()

        if UnitID == None:
            unitFormModel = mstBL.InitialiseUnitFormModel(None)
        else:
            unitFormModel = mstBL.InitialiseUnitFormModel(UnitID)

        return render(
            request,
            "UnitForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": unitFormModel},
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        unitFormModel = UnitFormModel()
        _post = UnitFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertUnit(_Form)

            if _Form["UnitID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                unitFormModel = mstBL.InitialiseUnitFormModel(UpsertResult["UnitID"])

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                unitFormModel = mstBL.InitialiseErrorUnitFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "UnitForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": unitFormModel},
        )


@csrf_exempt
def DeleteUnit(request, UnitID=None):
    rtn = False

    if request.method == "POST":
        rtn = pwsRepo.DeleteUnit(UnitID)
    else:
        rtn = False
    return HttpResponse(rtn)


def ContainerSizeList(request):
    return render(request, "ContainerSize.html")


def PartialContainerSizeList(request, SearchBy=""):
    ContainerSizes = []
    ContainerSizes = pwsRepo.PartialContainerSizeList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(ContainerSizes, 50)

    try:
        ContainerSizePaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        ContainerSizePaginator = _Paginator.page(1)
    except EmptyPage:
        ContainerSizePaginator = _Paginator.page(paginator.num_pages)

    return render(
        request,
        "PartialContainerSizeList.html",
        {"ContainerSizes": ContainerSizePaginator},
    )


@csrf_exempt
def ContainerSizeForm(request, ContainerSizeID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        containerSizeFormModel = ContainerSizeFormModel()

        if ContainerSizeID == None:
            containerSizeFormModel = mstBL.InitialiseContainerSizeFormModel(None)
        else:
            containerSizeFormModel = mstBL.InitialiseContainerSizeFormModel(
                ContainerSizeID
            )

        return render(
            request,
            "ContainerSizeForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": containerSizeFormModel,
            },
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        containerSizeFormModel = ContainerSizeFormModel()
        _post = ContainerSizeFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertContainerSize(_Form)

            if _Form["ContainerSizeID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                containerSizeFormModel = mstBL.InitialiseContainerSizeFormModel(
                    UpsertResult["ContainerSizeID"]
                )

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                containerSizeFormModel = mstBL.InitialiseErrorContainerSizeFormModel(
                    _Form
                )

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "ContainerSizeForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": containerSizeFormModel,
            },
        )


@csrf_exempt
def DeleteContainerSize(request, ContainerSizeID=None):
    rtn = False

    if request.method == "POST":
        rtn = pwsRepo.DeleteContainerSize(ContainerSizeID)
    else:
        rtn = False
    return HttpResponse(rtn)


def VesselList(request):
    return render(request, "Vessel.html")


def PartialVesselList(request, SearchBy=""):
    Vessels = []
    Vessels = pwsRepo.PartialVesselList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Vessels, 50)

    try:
        VesselPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        VesselPaginator = _Paginator.page(1)
    except EmptyPage:
        VesselPaginator = _Paginator.page(paginator.num_pages)

    return render(request, "PartialVesselList.html", {"Vessels": VesselPaginator})


@csrf_exempt
def VesselForm(request, VesselID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        vesselFormModel = VesselFormModel()

        if VesselID == None:
            vesselFormModel = mstBL.InitialiseVesselFormModel(None)
        else:
            vesselFormModel = mstBL.InitialiseVesselFormModel(VesselID)

        return render(
            request,
            "VesselForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": vesselFormModel},
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        vesselFormModel = VesselFormModel()
        _post = VesselFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertVessel(_Form)

            if _Form["VesselID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                vesselFormModel = mstBL.InitialiseVesselFormModel(
                    UpsertResult["VesselID"]
                )

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                vesselFormModel = mstBL.InitialiseErrorVesselFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "VesselForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": vesselFormModel},
        )


@csrf_exempt
def DeleteVessel(request, VesselID=None):
    rtn = False

    if request.method == "POST":
        rtn = pwsRepo.DeleteVessel(VesselID)
    else:
        rtn = False
    return HttpResponse(rtn)


def ItemList(request):
    return render(request, "Item.html")


def PartialItemList(request, SearchBy=""):
    Items = []
    Items = pwsRepo.PartialItemList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Items, 50)

    try:
        ItemPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        ItemPaginator = _Paginator.page(1)
    except EmptyPage:
        ItemPaginator = _Paginator.page(paginator.num_pages)

    return render(request, "PartialItemList.html", {"Items": ItemPaginator})


@csrf_exempt
def ItemForm(request, ItemID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        itemFormModel = ItemFormModel()

        if ItemID == None:
            itemFormModel = mstBL.InitialiseItemFormModel(None)
        else:
            itemFormModel = mstBL.InitialiseItemFormModel(ItemID)

        return render(
            request,
            "ItemForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": itemFormModel},
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        itemFormModel = ItemFormModel()
        _post = ItemFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertItem(_Form)

            if _Form["ItemID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                itemFormModel = mstBL.InitialiseItemFormModel(UpsertResult["ItemID"])

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                itemFormModel = mstBL.InitialiseErrorItemFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "ItemForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": itemFormModel},
        )


@csrf_exempt
def DeleteItem(request, ItemID=None):
    rtn = False

    if request.method == "POST":
        rtn = pwsRepo.DeleteItem(ItemID)
    else:
        rtn = False
    return HttpResponse(rtn)


def ClassList(request):
    return render(request, "Class.html")


def PartialClassList(request, SearchBy=""):
    Classes = []
    Classes = pwsRepo.PartialClassList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Classes, 50)

    try:
        ClassPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        ClassPaginator = _Paginator.page(1)
    except EmptyPage:
        ClassPaginator = _Paginator.page(paginator.num_pages)

    return render(request, "PartialClassList.html", {"Classes": ClassPaginator})


@csrf_exempt
def ClassForm(request, ClassID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        classFormModel = ClassFormModel()

        if ClassID == None:
            classFormModel = mstBL.InitialiseClassFormModel(None)
        else:
            classFormModel = mstBL.InitialiseClassFormModel(ClassID)

        return render(
            request,
            "ClassForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": classFormModel},
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        classFormModel = ClassFormModel()
        _post = ClassFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertClass(_Form)

            if _Form["ClassID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                classFormModel = mstBL.InitialiseClassFormModel(UpsertResult["ClassID"])

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                classFormModel = mstBL.InitialiseErrorClassFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "ClassForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": classFormModel},
        )


@csrf_exempt
def DeleteClass(request, ClassID=None):
    rtn = False

    if request.method == "POST":
        rtn = pwsRepo.DeleteClass(ClassID)
    else:
        rtn = False
    return HttpResponse(rtn)


def VoyageList(request):
    return render(request, "Voyage.html")


def PartialVoyageList(request, SearchBy=""):
    Voyages = []
    Voyages = pwsRepo.PartialVoyageList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Voyages, 50)

    try:
        VoyagePaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        VoyagePaginator = _Paginator.page(1)
    except EmptyPage:
        VoyagePaginator = _Paginator.page(paginator.num_pages)

    return render(request, "PartialVoyageList.html", {"Voyages": VoyagePaginator})


@csrf_exempt
def VoyageForm(request, VoyageID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        voyageFormModel = VoyageFormModel()

        if VoyageID == None:
            voyageFormModel = mstBL.InitialiseVoyageFormModel(None)
        else:
            voyageFormModel = mstBL.InitialiseVoyageFormModel(VoyageID)

        return render(
            request,
            "VoyageForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": voyageFormModel},
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        voyageFormModel = VoyageFormModel()
        _post = VoyageFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = pwsRepo.UpsertVoyage(_Form)

            if _Form["VoyageID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                voyageFormModel = mstBL.InitialiseVoyageFormModel(
                    UpsertResult["VoyageID"]
                )

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                voyageFormModel = mstBL.InitialiseErrorVoyageFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "VoyageForm.html",
            {"SysGoodMsg": SysGoodMsg, "SysBadMsg": SysBadMsg, "Form": voyageFormModel},
        )


@csrf_exempt
def DeleteVoyage(request, VoyageID=None):
    rtn = False

    if request.method == "POST":
        rtn = pwsRepo.DeleteVoyage(VoyageID)
    else:
        rtn = False
    return HttpResponse(rtn)


def UpsertCountry(request):
    rtn = False
    rtn = pwsRepo.UpsertCountry()
    return HttpResponse(rtn)
