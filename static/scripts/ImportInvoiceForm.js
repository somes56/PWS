$(function () {
    PartialInvoiceItemList()

    $("#ClientVerifyBlock").hide();

    $(document).keypress(function (e) {
        if (e.keyCode === 13) {
            e.preventDefault();
            return false;
        }
    });

    $(document).keydown(function (e) {
        if (e.keyCode === 8 && !$(e.target).is("input, textarea")) {
            e.preventDefault();
            return false;
        }
    });

    $('#IssueDate').datepicker({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
        yearRange: '2018:2050',
    });

    $('#IssueDate').on('change', function () {
        var DateUnstuff = new Date($('#UnstuffDate').val());
        var DateIssue = new Date($('#IssueDate').val());
        var DayDiff = Math.floor((DateIssue.getTime() - DateUnstuff.getTime()) / (1000 * 3600 * 24)) + 1;
        $('#StorageDay').val(DayDiff).trigger('change');
    })

    if ($("#InvoiceID").val() !== "") {
        $('#IssueDate').prop('disabled', true)
        $('#IsPartial').prop('disabled', true)
        $('#btnSearchHbl').prop('disabled', true)

    }
})

function PartialInvoiceItemList() {
    var InvoiceID = $('#InvoiceID').val();

    var url = `/Import/PartialInvoiceItemList`;
    url = InvoiceID === '' ? url : url + `/${InvoiceID}`

    $('#PartialInvoiceItemListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialInvoiceItemListLoading').hide();
            $('#PartialInvoiceItemList').text('Error in loading Invoice Item List');
        },
        success: function (data) {
            $('#PartialInvoiceItemListLoading').hide();
            $('#PartialInvoiceItemList').html(data);
        },
        type: "GET"
    });
}

function PickIssueDate() {
    $('#IssueDate').datepicker('show');
}

function ConvertUpperCase(ID) {
    $(`#${ID}`).val($(`#${ID}`).val().toUpperCase())
}

function IssuePartial(IsChecked) {

    if (IsChecked) {
        $('#IssuedQuantity').val('')
        $('#IssuedWeight').val('')
        $('#IssuedVolume').val('')
        $('#IssuedQuantity').attr('readonly', false)
        $('#IssuedWeight').attr('readonly', false)
        $('#IssuedVolume').attr('readonly', false)
    } else {
        $('#IssuedQuantity').attr('readonly', true)
        $('#IssuedWeight').attr('readonly', true)
        $('#IssuedVolume').attr('readonly', true)
        $('#IssuedQuantity').val($('#BalanceQuantity').val())
        $('#IssuedWeight').val($('#BalanceWeight').val())
        $('#IssuedVolume').val($('#BalanceVolume').val())
    }
}

function SearchHbl() {
    var crit = {
        "mt": "Search Hbl",
        "fn": "HblHist",
        "p": {},
        "md": {}
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchConsignee() {
    var crit = {
        "mt": "Search Bill To",
        "fn": "Customer",
        "p": {},
        "md": {
            'md1': 'ConsigneeID',
            'md2': 'ConsigneeName'
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchItem() {
    var crit = {
        "mt": "Search Item",
        "fn": "Item",
        "p": {},
        "md": {
            'md1': 'ItemID',
            'md2': 'ItemName'
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function AdvSearchCustomSel(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,
    v11, v12, v13, v14, v15, v16, v17, v18, v19, v20) {
    var DateArrive = new Date(v6);
    var DateArriveIso = `${DateArrive.getFullYear().toString()}-${DateArrive.getMonth() + 1 < 10 ?
        '0' + (DateArrive.getMonth() + 1).toString() : (DateArrive.getMonth() + 1).toString()}-${DateArrive.getDate() < 10 ? '0' + DateArrive.getDate().toString() : DateArrive.getDate().toString()}`

    var DateUnstuff = new Date(v10);
    var DateIssue = new Date($('#IssueDate').val());
    var DateUnstuffIso = `${DateUnstuff.getFullYear().toString()}-${DateUnstuff.getMonth() + 1 < 10 ?
        '0' + (DateUnstuff.getMonth() + 1).toString() : (DateUnstuff.getMonth() + 1).toString()}-${DateUnstuff.getDate() < 10 ? '0' + DateUnstuff.getDate().toString() : DateUnstuff.getDate().toString()}`
    var DayDiff = Math.floor((DateIssue.getTime() - DateUnstuff.getTime()) / (1000 * 3600 * 24)) + 1;

    $('#HblID').val(v1).trigger('change');
    $('#HblNo').val(v2).trigger('change');
    $('#OblNo').val(v3).trigger('change');
    $('#VoyageNo').val(v4).trigger('change');
    $('#ShipCallNo').val(v5).trigger('change');

    $('#Eta').val(DateArriveIso).trigger('change');
    $('#VesselName').val(v7).trigger('change');
    $('#LoadPortName').val(v8).trigger('change');
    $('#UnLoadPortName').val(v9).trigger('change');
    $('#StorageDay').val(DayDiff).trigger('change');

    $('#UnstuffDate').val(DateUnstuffIso).trigger('change');
    $('#LocationDesc').val(v11).trigger('change');
    $('#PackageDesc').val(v12).trigger('change');
    $('#ConsigneeID').val(v13).trigger('change');
    $('#ConsigneeName').val(v14).trigger('change');

    $('#InitialQuantity').val(v15).trigger('change');
    $('#InitialWeight').val(v16).trigger('change');
    $('#InitialVolume').val(v17).trigger('change');
    $('#BalanceQuantity').val(v18).trigger('change');
    $('#BalanceWeight').val(v19).trigger('change');
    $('#BalanceVolume').val(v20).trigger('change');
    $('#IssuedQuantity').val(v18).trigger('change');
    $('#IssuedWeight').val(v19).trigger('change');
    $('#IssuedVolume').val(v20).trigger('change');

    $('#AdvSearchModal').modal('hide');
}

function SubmitValidation() {
    var msg = [];
    var i = 0;

    if ($('#No').val() === "" && $('#InvoiceID').val() !== "") {
        msg[i] = "No is required.";
        i = i + 1;
    }

    if ($('#HblID').val() === "" && $('#HblNo').val() === "") {
        msg[i] = "Hbl is required.";
        i = i + 1;
    }

    if ($('#StorageDay').val() === "" || $('#StorageDay').val() < 1) {
        msg[i] = "Storage Day is required.";
        i = i + 1;
    }

    if ($('#IssuedQuantity').val() === "" || parseInt($('#IssuedQuantity').val()) === 0) {
        msg[i] = "Quantity is required.";
        i = i + 1;
    }

    if ($('#IssuedWeight').val() === "" || parseFloat($('#IssuedWeight').val()) < 0.001) {
        msg[i] = "Weight is required.";
        i = i + 1;
    }

    if ($('#IssuedVolume').val() === "" || parseFloat($('#IssuedVolume').val()) < 0.001) {
        msg[i] = "Volume is required.";
        i = i + 1;
    }

    if ($('#ConsigneeID').val() === "" && $('#ConsigneeName').val() !== "") {
        msg[i] = "Bill To is required.";
        i = i + 1;
    }

    if ($('#IidNo').val() === "") {
        msg[i] = "IID No is required.";
        i = i + 1;
    }

    if ($('#InvoiceID').val() === "" && parseInt($('#IssuedQuantity').val()) > parseInt($('#BalanceQuantity').val())) {
        msg[i] = "Quantity exceeded balance quantity.";
        i = i + 1;
    }

    if ($('#InvoiceID').val() === "" && parseFloat($('#IssuedWeight').val()) > parseFloat($('#BalanceWeight').val())) {
        msg[i] = "Weight exceeded balance weight.";
        i = i + 1;
    }

    if ($('#InvoiceID').val() === "" && parseFloat($('#IssuedVolume').val()) > parseFloat($('#BalanceVolume').val())) {
        msg[i] = "Volume exceeded balance volume.";
        i = i + 1;
    }

    if (parseInt($('input[name="PaymentType"]:checked').val()) > 0 && $('#RefNo').val() === "") {
        msg[i] = "Reference no is required.";
        i = i + 1;
    }

    if (msg.length > 0) {
        $("#ClientVerifyMsg").html(msg.join("<br/>"));

        $("#ClientVerifyBlock").show();

        return false;
    } else {
        return true;
    }
}

function UpsertDefaultInvoiceItem() {
    var InvoiceID = $('#InvoiceID').val();
    var StorageDay = parseInt($('#StorageDay').val());
    var url = `${window.location.origin}/Import/UpsertDefaultInvoiceItem/${InvoiceID}/`;

    if (InvoiceID === "") {
        alert('Invoice No is required');
        return;
    }

    if (isNaN(StorageDay) || StorageDay < 1) {
        alert('Storage Day is required');
        return;
    }

    $('#PartialInvoiceItemListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            alert('Add Fail');
            $('#PartialInvoiceItemListLoading').hide();
        },
        success: function (data) {
            if (data.rtn == true) {
                alert('Added Successfully');
            } else {
                alert(data.SysBadMsg);
            }
            PartialInvoiceItemList();
        },
        type: "POST"
    });
}

function UpsertInvoiceItem() {
    var InvoiceID = $('#InvoiceID').val();
    var InvoiceItemID = $('#InvoiceItemID').val();
    var ItemID = $('#ItemID').val();
    var ItemQuantity = parseInt($('#ItemQuantity').val());
    var ItemUnitAmount = $('#ItemUnitAmount').val();

    if (InvoiceID === "") {
        alert('Invoice No is required');
        return;
    }

    if (ItemID === "") {
        alert('Item is required');
        return;
    }

    if (isNaN(ItemQuantity) || ItemQuantity < 1) {
        alert('Quantity is required');
        return;
    }

    if (isNaN(ItemUnitAmount) || ItemUnitAmount < 0.01) {
        alert('Unit Price is required');
        return;
    }

    var url = `${window.location.origin}/Import/UpsertInvoiceItem/${InvoiceID}/`
    url = InvoiceItemID !== "" ? url + `${InvoiceItemID}/` : url;
    url = url + `${ItemID}/${ItemQuantity}/${ItemUnitAmount}/`;

    $('#PartialInvoiceItemListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            alert('Save Fail');
            $('#PartialInvoiceItemListLoading').hide();
        },
        success: function (data) {
            if (data == 'True') {
                alert('Saved Successfully');
            } else {
                alert('Save Fail');
            }
            PartialInvoiceItemList();
        },
        type: "POST"
    });

}

function CancelInvoiceItem() {
    $('#InvoiceItemID').val('');
    $('#ItemID').val('');
    $('#ItemName').val('');
    $('#ItemQuantity').val('');
    $('#ItemUnitAmount').val('');
}

function UpdateInvoiceItem(InvoiceItemID, ItemID, ItemName, ItemQuantity, ItemUnitAmount) {
    $('#InvoiceItemID').val(InvoiceItemID);
    $('#ItemID').val(ItemID);
    $('#ItemName').val(ItemName);
    $('#ItemQuantity').val(ItemQuantity);
    $('#ItemUnitAmount').val(ItemUnitAmount);
}

function DeleteInvoiceItem(InvoiceItemID, ItemName) {
    var Dlg = confirm(`Are you sure to delete ${ItemName} ?`)

    if (Dlg == true) {
        var url = `${window.location.origin}/Import/DeleteInvoiceItem/${InvoiceItemID}/`
        $.ajax({
            url: url,
            cache: false,
            error: function () {
                alert('Delete Fail');
            },
            success: function (data) {
                if (data == 'True') {
                    alert('Deleted Successfully');
                } else {
                    alert('Delete Fail');
                }
                PartialInvoiceItemList();
            },
            type: "POST"
        });

    }
}


function ResetForm() {
    window.location.href = `/Import/InvoiceForm`
}