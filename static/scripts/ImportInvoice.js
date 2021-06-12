$(function () {
    PartialInvoiceList()

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
})

function PartialInvoiceList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Import/PartialInvoiceList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialInvoiceListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialInvoiceListLoading').hide();
            $('#PartialInvoiceList').text('Error in loading Invoice List');
        },
        success: function (data) {
            $('#PartialInvoiceListLoading').hide();
            $('#PartialInvoiceList').html(data);
        },
        type: "GET"
    });
}

function DeleteInvoice(InvoiceID, InvoiceNo) {
    var Dlg = confirm(`Are you sure to delete ${InvoiceNo} ?`)

    if (Dlg == true) {
        var DlgPrompt = prompt("Please enter delete remark");

        if(DlgPrompt !== "" && DlgPrompt !== null){
        var url = `/Import/DeleteInvoice/${InvoiceID}/${DlgPrompt.toString().toUpperCase()}`
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
                PartialInvoiceList();
            },
            type: "POST"
        });
        }else if(DlgPrompt === ""){
            alert("Delete remark is required.")
        }
    }
}

function GoToAddPage() {
    window.location.href = `/Import/InvoiceForm`
}

function GoToEditPage(InvoiceID) {
    window.location.href = `/Import/InvoiceForm/${InvoiceID}/`
}


