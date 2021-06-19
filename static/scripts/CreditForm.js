$(function () {
    PartialCreditItemList()

    $("#ClientVerifyBlock").hide();

    $('#IsPartial').prop('disabled', true)
    $('input[name="PaymentType"]').prop('disabled', true)

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

    $(document).on('change', '#ItemName', function () {
        var IsDefaultItem = false;
        IsDefaultItem = ['HANDLING CHARGES', 'FAF (FUEL ADJUSTMENT FACTOR)', 'STORAGE CHARGES', 'REMOVAL CHARGES'].includes($('#ItemName').val());

        if (IsDefaultItem) {
            var ClassType = $('#ClassShortName').val() === 'GENERAL' ? 'NORMAL' :
                $('#ClassShortName').val() === 'DG CLS I' ||
                    $('#ClassShortName').val() === 'DG CLS II' ||
                    $('#ClassShortName').val() === 'DG CLS III' ?
                    'DANGEROUS' : '';

            if (ClassType === 'NORMAL' || ClassType === 'DANGEROUS') {
                var FloorWeight = Math.floor(parseFloat($('#IssuedWeight').val()) / 1000);
                var FractionWeight = (parseFloat($('#IssuedWeight').val() / 1000)) - FloorWeight;
                FloorWeight += FractionWeight !== 0 ? 1 : 0;

                var FloorVolume = Math.floor(parseFloat($('#IssuedVolume').val()));
                var FractionVolume = parseFloat($('#IssuedVolume').val()) - FloorVolume;
                FloorVolume += FractionVolume !== 0 ? 1 : 0;

                var ItemQuantity = FloorWeight >= FloorVolume ? FloorWeight : FloorVolume;
                var DefaultItemCode = `${ClassType == 'NORMAL' ? 'N' : 'D'}${parseInt($('#StorageDay').val()) <= 3 ? 'D3' : 'D4'}${ItemQuantity <= 1 ? 'Q1' : 'Q2'}`;
                var url = `${window.location.origin}/Cmn/DefaultItemByAccountTypeCode/CN/${DefaultItemCode}/`

                $.ajax({
                    url: url,
                    cache: false,
                    error: function () {
                        alert('Error in getting Default Credit Item List');
                        $('#CreditItemID').val('');
                        $('#ItemID').val('');
                        $('#ItemName').val('');
                        $('#ItemQuantity').val('');
                        $('#ItemUnitAmount').val('');
                        $('#ItemQuantity').attr('readonly', false);
                        $('#ItemUnitAmount').attr('readonly', false);
                    },
                    success: function (data) {
                        var DefaultCreditItems = [];
                        DefaultCreditItems = data;

                        if (DefaultCreditItems?.length > 1) {
                            DefaultCreditItems.forEach(i => {
                                if (i.fields.Item === $('#ItemID').val()) {
                                    $('#ItemQuantity').val(ItemQuantity);
                                    $('#ItemUnitAmount').val(i.fields.Amount);
                                    $('#ItemQuantity').attr('readonly', true);
                                    $('#ItemUnitAmount').attr('readonly', true);
                                }
                            });
                        } else {
                            alert('Default Credit Item Master not found');
                        }
                    },
                    type: "GET"
                });

            } else {
                alert(`${$('#HblNo').val()} is not a General or Dangerous class`);
                $('#CreditItemID').val('');
                $('#ItemID').val('');
                $('#ItemName').val('');
                $('#ItemQuantity').val('');
                $('#ItemUnitAmount').val('');
                $('#ItemQuantity').attr('readonly', false);
                $('#ItemUnitAmount').attr('readonly', false);
            }
        } else {
            $('#ItemQuantity').val('');
            $('#ItemUnitAmount').val('');
            $('#ItemQuantity').attr('readonly', false);
            $('#ItemUnitAmount').attr('readonly', false);
        }
    })

})

function PartialCreditItemList() {
    var CreditID = $('#CreditID').val();

    var url = `/Import/PartialCreditItemList`;
    url = CreditID === '' ? url : url + `/${CreditID}`

    $('#PartialCreditItemListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialCreditItemListLoading').hide();
            $('#PartialCreditItemList').text('Error in loading Credit Item List');
        },
        success: function (data) {
            $('#PartialCreditItemListLoading').hide();
            $('#PartialCreditItemList').html(data);
        },
        type: "GET"
    });
}


function SearchInvoice() {
    var crit = {
        "mt": "Search Invoice",
        "fn": "CreditInvoice",
        "p": {},
        "md": {}
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
    v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,
    v21, v22, v23) {
    var DateInvoiceIssue = new Date(v3);
    var DateInvoiceIssueIso = `${DateInvoiceIssue.getFullYear().toString()}-${DateInvoiceIssue.getMonth() + 1 < 10 ?
        '0' + (DateInvoiceIssue.getMonth() + 1).toString() : (DateInvoiceIssue.getMonth() + 1).toString()}-${DateInvoiceIssue.getDate() < 10
            ? '0' + DateInvoiceIssue.getDate().toString() : DateInvoiceIssue.getDate().toString()}`;

    var DateArrive = new Date(v18);
    var DateArriveIso = `${DateArrive.getFullYear().toString()}-${DateArrive.getMonth() + 1 < 10 ?
        '0' + (DateArrive.getMonth() + 1).toString() : (DateArrive.getMonth() + 1).toString()}-${DateArrive.getDate() < 10
            ? '0' + DateArrive.getDate().toString() : DateArrive.getDate().toString()}`;

    var DateUnstuff = new Date(v22);
    var DateUnstuffIso = `${DateUnstuff.getFullYear().toString()}-${DateUnstuff.getMonth() + 1 < 10 ?
        '0' + (DateUnstuff.getMonth() + 1).toString() : (DateUnstuff.getMonth() + 1).toString()}-${DateUnstuff.getDate() < 10
            ? '0' + DateUnstuff.getDate().toString() : DateUnstuff.getDate().toString()}`;


    $('#InvoiceID').val(v1).trigger('change');
    $('#InvoiceNo').val(v2).trigger('change');
    $('#InvoiceIssueDate').val(DateInvoiceIssueIso).trigger('change');
    $('#IsPartial').prop('checked', v4 === 'True' ? true : false)
    $('#IssuedQuantity').val(v5).trigger('change');

    $('#IssuedWeight').val(v6).trigger('change');
    $('#IssuedVolume').val(v7).trigger('change');
    $('#ConsigneeName').val(v8).trigger('change');
    $('input:radio[name=PaymentType]').val([parseInt(v9)]).trigger('change');
    $('#RefNo').val(v10).trigger('change');

    $('#IidNo').val(v11).trigger('change');
    $('#StorageDay').val(Math.floor(v12)).trigger('change');
    $('#HblNo').val(v13).trigger('change');
    $('#ClassShortName').val(v14).trigger('change');
    $('#OblNo').val(v15).trigger('change');

    $('#VoyageNo').val(v16).trigger('change');
    $('#ShipCallNo').val(v17).trigger('change');
    $('#Eta').val(DateArriveIso).trigger('change');
    $('#VesselName').val(v19).trigger('change');
    $('#LoadPortName').val(v20).trigger('change');

    $('#UnLoadPortName').val(v21).trigger('change');
    $('#UnstuffDate').val(DateUnstuffIso).trigger('change');
    $('#LocationDesc').val(v23).trigger('change');

    $('#AdvSearchModal').modal('hide');
}

function SubmitValidation() {
    var msg = [];
    var i = 0;

    if ($('#No').val() === "" && $('#CreditID').val() !== "") {
        msg[i] = "No is required.";
        i = i + 1;
    }

    if ($('#InvoiceID').val() === "" && $('#InvoiceNo').val() === "") {
        msg[i] = "Invoice is required.";
        i = i + 1;
    }

    if ($('#StorageDay').val() === "" || parseInt($('#StorageDay').val()) < 1) {
        msg[i] = "Storage Day is required.";
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

function UpsertCreditItem() {
    var CreditID = $('#CreditID').val();
    var CreditItemID = $('#CreditItemID').val();
    var ItemID = $('#ItemID').val();
    var ItemQuantity = parseInt($('#ItemQuantity').val());
    var ItemUnitAmount = $('#ItemUnitAmount').val();
    var IsDefaultItem = ['HANDLING CHARGES', 'FAF (FUEL ADJUSTMENT FACTOR)', 'STORAGE CHARGES', 'REMOVAL CHARGES'].includes($('#ItemName').val());

    if (CreditID === "") {
        alert('Credit No is required');
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

    var url = `${window.location.origin}/Import/UpsertCreditItem/${CreditID}/`
    url = CreditItemID !== "" ? url + `${CreditItemID}/` : url;
    url = url + `${ItemID}/${ItemQuantity}/${ItemUnitAmount}/${IsDefaultItem === true ? 1 : 0}/`;

    $('#PartialCreditItemListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            alert('Save Fail');
            $('#PartialCreditItemListLoading').hide();
        },
        success: function (data) {
            if (data == 'True') {
                alert('Saved Successfully');
            } else {
                alert('Save Fail');
            }
            PartialCreditItemList();
        },
        type: "POST"
    });

}

function CancelCreditItem() {
    $('#CreditItemID').val('');
    $('#ItemID').val('');
    $('#ItemName').val('');
    $('#ItemQuantity').val('');
    $('#ItemUnitAmount').val('');
    $('#ItemQuantity').attr('readonly', false);
    $('#ItemUnitAmount').attr('readonly', false);
}

function UpdateCreditItem(CreditItemID, ItemID, ItemName, ItemQuantity, ItemUnitAmount, IsDefault) {
    $('#CreditItemID').val(CreditItemID);
    $('#ItemID').val(ItemID);
    $('#ItemName').val(ItemName);
    $('#ItemQuantity').val(ItemQuantity);
    $('#ItemUnitAmount').val(ItemUnitAmount);
    $('#ItemQuantity').attr('readonly', IsDefault === 'True' ? true : false);
    $('#ItemUnitAmount').attr('readonly', IsDefault === 'True' ? true : false);
}

function DeleteCreditItem(CreditItemID, ItemName) {
    var Dlg = confirm(`Are you sure to delete ${ItemName} ?`)

    if (Dlg == true) {
        var url = `${window.location.origin}/Import/DeleteCreditItem/${CreditItemID}/`
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
                PartialCreditItemList();
            },
            type: "POST"
        });

    }
}

function ResetForm() {
    window.location.href = `/Import/CreditForm`
}