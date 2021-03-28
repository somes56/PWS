from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from BusinessLogic.ImportBL import importBL
from DataAccess.ImportRepo import importRepo
from Import.formModels import OblFormModel, ContainerFormModel


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
        OblPaginator = _Paginator.page(paginator.num_pages)

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
        ContainerPaginator = _Paginator.page(paginator.num_pages)

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
