from DataAccess.MasterRepo import masterRepo
from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from BusinessLogic.ImportBL import importBL
from BusinessLogic.SysBL import sysBL
from DataAccess.ImportRepo import importRepo
from Import.formModels import (
    OblFormModel,
    ContainerFormModel,
    HblFormModel,
    UnstuffContainerFormModel,
    InvoiceFormModel,
    CreditFormModel,
)


def OblList(request):
    return render(request, "Obl.html")


def PartialOblList(request, SearchBy=""):
    Obls = []
    Obls = importRepo.PartialOblList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Obls, 50)

    try:
        OblPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        OblPaginator = _Paginator.page(1)
    except EmptyPage:
        OblPaginator = _Paginator.page(_Paginator.num_pages)

    return render(request, "PartialOblList.html", {"Obls": OblPaginator})


@csrf_exempt
def OblForm(request, OblID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        oblFormModel = OblFormModel()

        if OblID == None:
            oblFormModel = importBL.InitialiseOblFormModel(None)
        else:
            oblFormModel = importBL.InitialiseOblFormModel(OblID)

        return render(
            request,
            "OblForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": oblFormModel,
            },
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        oblFormModel = OblFormModel()
        _post = OblFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = importRepo.UpsertObl(_Form)

            if _Form["OblID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                oblFormModel = importBL.InitialiseOblFormModel(UpsertResult["OblID"])

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                oblFormModel = importBL.InitialiseErrorOblFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "OblForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": oblFormModel,
            },
        )


@csrf_exempt
def DeleteObl(request, OblID=None):
    rtn = False

    if request.method == "POST":
        rtn = importRepo.DeleteObl(OblID)
    else:
        rtn = False
    return HttpResponse(rtn)


def ContainerList(request):
    return render(request, "Container.html")


def PartialContainerList(request, SearchBy=""):
    Containers = []
    Containers = importRepo.PartialContainerList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Containers, 50)

    try:
        ContainerPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        ContainerPaginator = _Paginator.page(1)
    except EmptyPage:
        ContainerPaginator = _Paginator.page(_Paginator.num_pages)

    return render(
        request, "PartialContainerList.html", {"Containers": ContainerPaginator}
    )


@csrf_exempt
def ContainerForm(request, ContainerID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        containerFormModel = ContainerFormModel()

        if ContainerID == None:
            containerFormModel = importBL.InitialiseContainerFormModel(None)
        else:
            containerFormModel = importBL.InitialiseContainerFormModel(ContainerID)

        return render(
            request,
            "ContainerForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": containerFormModel,
            },
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        containerFormModel = ContainerFormModel()
        _post = ContainerFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = importRepo.UpsertContainer(_Form)

            if _Form["ContainerID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                containerFormModel = importBL.InitialiseContainerFormModel(
                    UpsertResult["ContainerID"]
                )

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                containerFormModel = importBL.InitialiseErrorContainerFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "ContainerForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": containerFormModel,
            },
        )


@csrf_exempt
def DeleteContainer(request, ContainerID=None):
    rtn = False

    if request.method == "POST":
        rtn = importRepo.DeleteContainer(ContainerID)
    else:
        rtn = False
    return HttpResponse(rtn)


def HblList(request):
    return render(request, "Hbl.html")


def PartialHblList(request, SearchBy=""):
    Hbls = []
    Hbls = importRepo.PartialHblList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Hbls, 50)

    try:
        HblPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        HblPaginator = _Paginator.page(1)
    except EmptyPage:
        HblPaginator = _Paginator.page(_Paginator.num_pages)

    return render(request, "PartialHblList.html", {"Hbls": HblPaginator})


@csrf_exempt
def HblForm(request, HblID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        hblFormModel = HblFormModel()

        if HblID == None:
            hblFormModel = importBL.InitialiseHblFormModel(None)
        else:
            hblFormModel = importBL.InitialiseHblFormModel(HblID)

        return render(
            request,
            "HblForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": hblFormModel,
            },
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        hblFormModel = HblFormModel()
        _post = HblFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = importRepo.UpsertHbl(_Form)

            if _Form["HblID"] != None:
                IsUpdate = True

            if UpsertResult["rtn"] == True:
                hblFormModel = importBL.InitialiseHblFormModel(UpsertResult["HblID"])

                if IsUpdate == False:
                    SysGoodMsg = "Inserted Successfully"
                else:
                    SysGoodMsg = "Updated Successfully"

            else:
                hblFormModel = importBL.InitialiseErrorHblFormModel(_Form)

                if IsUpdate == False:
                    SysBadMsg = "Insert Fail"
                else:
                    SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "HblForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": hblFormModel,
            },
        )


@csrf_exempt
def DeleteHbl(request, HblID=None):
    rtn = False

    if request.method == "POST":
        rtn = importRepo.DeleteHbl(HblID)
    else:
        rtn = False
    return HttpResponse(rtn)


def UnstuffContainerList(request):
    return render(request, "UnstuffContainer.html")


def PartialUnstuffContainerPendingList(request, SearchBy=""):
    Containers = []
    Containers = importRepo.PartialUnstuffContainerPendingList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Containers, 50)

    try:
        ContainerPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        ContainerPaginator = _Paginator.page(1)
    except EmptyPage:
        ContainerPaginator = _Paginator.page(_Paginator.num_pages)

    return render(
        request,
        "PartialUnstuffContainerPendingList.html",
        {"Containers": ContainerPaginator},
    )


def PartialUnstuffContainerCompletedList(request, SearchBy=""):
    Containers = []
    Containers = importRepo.PartialUnstuffContainerCompletedList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Containers, 50)

    try:
        ContainerPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        ContainerPaginator = _Paginator.page(1)
    except EmptyPage:
        ContainerPaginator = _Paginator.page(_Paginator.num_pages)

    return render(
        request,
        "PartialUnstuffContainerCompletedList.html",
        {"Containers": ContainerPaginator},
    )


@csrf_exempt
def UnstuffContainerForm(request, ContainerID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        unstuffContainerFormModel = UnstuffContainerFormModel()
        unstuffContainerFormModel = importBL.InitialiseUnstuffContainerFormModel(
            ContainerID, None
        )

        return render(
            request,
            "UnstuffContainerForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": unstuffContainerFormModel,
            },
        )

    else:
        IsUpdate = False
        UpsertResult = {}
        unstuffContainerFormModel = UnstuffContainerFormModel()
        _post = UnstuffContainerFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data
            UpsertResult = importRepo.UpsertUnstuffContainer(_Form)

            if UpsertResult["rtn"] == True:
                unstuffContainerFormModel = (
                    importBL.InitialiseUnstuffContainerFormModel(
                        UpsertResult["ContainerID"], UpsertResult["HblID"]
                    )
                )

                SysGoodMsg = "Updated Successfully"

            else:
                unstuffContainerFormModel = (
                    importBL.InitialiseErrorUnstuffContainerFormModel(_Form)
                )

                SysBadMsg = "Update Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "UnstuffContainerForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": unstuffContainerFormModel,
            },
        )


def InvoiceList(request):
    return render(request, "ImportInvoice.html")


def PartialInvoiceList(request, SearchBy=""):
    Invoices = []
    Invoices = importRepo.PartialInvoiceList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Invoices, 50)

    try:
        InvoicePaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        InvoicePaginator = _Paginator.page(1)
    except EmptyPage:
        InvoicePaginator = _Paginator.page(_Paginator.num_pages)

    return render(
        request, "PartialImportInvoiceList.html", {"Invoices": InvoicePaginator}
    )


def PartialInvoiceItemList(request, InvoiceID=None):
    InvoiceItems = []
    InvoiceItems = importRepo.PartialInvoiceItemList(InvoiceID)

    return render(
        request, "PartialImportInvoiceItemList.html", {"InvoiceItems": InvoiceItems}
    )


@csrf_exempt
def InvoiceForm(request, InvoiceID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        invoiceFormModel = InvoiceFormModel()

        if InvoiceID == None:
            invoiceFormModel = importBL.InitialiseInvoiceFormModel(None)
        else:
            invoiceFormModel = importBL.InitialiseInvoiceFormModel(InvoiceID)

        return render(
            request,
            "ImportInvoiceForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": invoiceFormModel,
            },
        )

    else:
        IsUpdate = False
        InvoiceNo = None
        UpsertResult = {}
        invoiceFormModel = InvoiceFormModel()
        _post = InvoiceFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data

            if _Form["InvoiceID"] != None:
                IsUpdate = True
                InvoiceNo = _Form["No"]
            else:
                InvoiceNo = sysBL.GenerateRunningNo(
                    "d1c508dc-ff6b-4aa5-b478-8098e84aadc5", "IN"
                )

            if InvoiceNo != None:
                _Form["No"] = InvoiceNo
                UpsertResult = importRepo.UpsertInvoice(_Form)

                if UpsertResult["rtn"] == True:
                    invoiceFormModel = importBL.InitialiseInvoiceFormModel(
                        UpsertResult["InvoiceID"]
                    )

                    if IsUpdate == False:
                        SysGoodMsg = "Inserted Successfully"
                    else:
                        SysGoodMsg = "Updated Successfully"

                else:
                    invoiceFormModel = importBL.InitialiseErrorInvoiceFormModel(_Form)

                    if IsUpdate == False:
                        SysBadMsg = "Insert Fail"
                    else:
                        SysBadMsg = "Update Fail"

            else:
                invoiceFormModel = importBL.InitialiseErrorInvoiceFormModel(_Form)

                if IsUpdate:
                    SysBadMsg = "No is required"
                else:
                    SysBadMsg = "Invoice No Generation Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "ImportInvoiceForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": invoiceFormModel,
            },
        )


@csrf_exempt
def UpsertDefaultInvoiceItem(request, InvoiceID=None):
    rtn = {}

    if request.method == "POST":
        rtn = importBL.UpsertDefaultInvoiceItem(InvoiceID)

    return JsonResponse(rtn)


@csrf_exempt
def UpsertInvoiceItem(
    request,
    InvoiceID=None,
    InvoiceItemID=None,
    ItemID=None,
    ItemQuantity=0,
    ItemUnitAmount=None,
):
    rtn = False

    if request.method == "POST":
        rtn = importBL.UpsertInvoiceItem(
            InvoiceID, InvoiceItemID, ItemID, ItemQuantity, float(ItemUnitAmount)
        )

    else:
        rtn = False
    return HttpResponse(rtn)


@csrf_exempt
def DeleteInvoice(request, InvoiceID=None, DeleteRemark=None):
    rtn = False

    if request.method == "POST":
        rtn = importRepo.DeleteInvoice(InvoiceID, DeleteRemark)
    else:
        rtn = False
    return HttpResponse(rtn)


@csrf_exempt
def DeleteInvoiceItem(request, InvoiceItemID=None):
    rtn = False

    if request.method == "POST":
        rtn = importBL.DeleteInvoiceItem(InvoiceItemID)
    else:
        rtn = False
    return HttpResponse(rtn)


def CreditList(request):
    return render(request, "Credit.html")


def PartialCreditList(request, SearchBy=""):
    Credits = []
    Credits = importRepo.PartialCreditList(SearchBy)

    Page = request.GET.get("page", 1)
    _Paginator = Paginator(Credits, 50)

    try:
        CreditPaginator = _Paginator.page(Page)
    except PageNotAnInteger:
        CreditPaginator = _Paginator.page(1)
    except EmptyPage:
        CreditPaginator = _Paginator.page(_Paginator.num_pages)

    return render(request, "PartialCreditList.html", {"Credits": CreditPaginator})


def PartialCreditItemList(request, CreditID=None):
    CreditItems = []
    CreditItems = importRepo.PartialCreditItemList(CreditID)

    return render(request, "PartialCreditItemList.html", {"CreditItems": CreditItems})


@csrf_exempt
def CreditForm(request, CreditID=None):
    SysGoodMsg = ""
    SysBadMsg = ""

    if request.method == "GET":
        creditFormModel = CreditFormModel()

        if CreditID == None:
            creditFormModel = importBL.InitialiseCreditFormModel(None)
        else:
            creditFormModel = importBL.InitialiseCreditFormModel(CreditID)

        return render(
            request,
            "CreditForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": creditFormModel,
            },
        )

    else:
        IsUpdate = False
        CreditNo = None
        UpsertResult = {}
        creditFormModel = CreditFormModel()
        _post = CreditFormModel(request.POST)

        if _post.is_valid():
            _Form = _post.cleaned_data

            if _Form["CreditID"] != None:
                IsUpdate = True
                CreditNo = _Form["No"]
            else:
                CreditNo = sysBL.GenerateRunningNo(
                    "d1c508dc-ff6b-4aa5-b478-8098e84aadc5", "CN"
                )

            if CreditNo != None:
                _Form["No"] = CreditNo
                UpsertResult = importRepo.UpsertCredit(_Form)

                if UpsertResult["rtn"] == True:
                    creditFormModel = importBL.InitialiseCreditFormModel(
                        UpsertResult["CreditID"]
                    )

                    if IsUpdate == False:
                        SysGoodMsg = "Inserted Successfully"
                    else:
                        SysGoodMsg = "Updated Successfully"

                else:
                    creditFormModel = importBL.InitialiseErrorCreditFormModel(_Form)

                    if IsUpdate == False:
                        SysBadMsg = "Insert Fail"
                    else:
                        SysBadMsg = "Update Fail"

            else:
                creditFormModel = importBL.InitialiseErrorCreditFormModel(_Form)

                if IsUpdate:
                    SysBadMsg = "No is required"
                else:
                    SysBadMsg = "Credit No Generation Fail"

        else:
            SysBadMsg = "Invalid Input"

        return render(
            request,
            "CreditForm.html",
            {
                "SysGoodMsg": SysGoodMsg,
                "SysBadMsg": SysBadMsg,
                "Form": creditFormModel,
            },
        )


@csrf_exempt
def UpsertCreditItem(
    request,
    CreditID=None,
    CreditItemID=None,
    ItemID=None,
    ItemQuantity=0,
    ItemUnitAmount=None,
    IsDefaultItem=0,
):
    rtn = False

    if request.method == "POST":
        rtn = importRepo.UpsertCreditItem(
            importRepo,
            CreditID,
            CreditItemID,
            ItemID,
            ItemQuantity,
            float(ItemUnitAmount),
            True if IsDefaultItem == 1 else False,
        )
    else:
        rtn = False
    return HttpResponse(rtn)


@csrf_exempt
def DeleteCreditItem(request, CreditItemID=None):
    rtn = False

    if request.method == "POST":
        rtn = importRepo.DeleteCreditItem(importRepo, CreditItemID)
    else:
        rtn = False
    return HttpResponse(rtn)


@csrf_exempt
def DeleteCredit(request, CreditID=None, DeleteRemark=None):
    rtn = False

    if request.method == "POST":
        rtn = importRepo.DeleteCredit(CreditID, DeleteRemark)
    else:
        rtn = False
    return HttpResponse(rtn)
