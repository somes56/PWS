$(function () {
    PartialCreditList()

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

function PartialCreditList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Import/PartialCreditList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialCreditListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialCreditListLoading').hide();
            $('#PartialCreditList').text('Error in loading Credit List');
        },
        success: function (data) {
            $('#PartialCreditListLoading').hide();
            $('#PartialCreditList').html(data);
        },
        type: "GET"
    });
}

function DeleteCredit(CreditID, CreditNo) {
    var Dlg = confirm(`Are you sure to delete ${CreditNo} ?`)

    if (Dlg == true) {
        var DlgPrompt = prompt("Please enter delete remark");

        if (DlgPrompt !== "" && DlgPrompt !== null) {
            var url = `/Import/DeleteCredit/${CreditID}/${DlgPrompt.toString().toUpperCase()}`
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
                    PartialCreditList();
                },
                type: "POST"
            });
        } else if (DlgPrompt === "") {
            alert("Delete remark is required.")
        }
    }
}

function GoToAddPage() {
    window.location.href = `/Import/CreditForm`
}

function GoToEditPage(CreditID) {
    window.location.href = `/Import/CreditForm/${CreditID}/`
}


