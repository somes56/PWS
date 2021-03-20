$(function () {
    PartialOperatorList()

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

function PartialOperatorList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Master/PartialOperatorList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialOperatorListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialOperatorListLoading').hide();
            $('#PartialOperatorList').text('Error in loading Operator List');
        },
        success: function (data) {
            $('#PartialOperatorListLoading').hide();
            $('#PartialOperatorList').html(data);
        },
        type: "GET"
    });
}

function DeleteOperator(OperatorID, Name) {
    var Dlg = confirm(`Are you sure to delete ${Name} ?`)

    if (Dlg == true) {
        var url = `/Master/DeleteOperator/${OperatorID}/`
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
                PartialOperatorList();
            },
            type: "POST"
        });

    }
}

function GoToAddPage() {
    window.location.href = `/Master/OperatorForm`
}

function GoToEditPage(OperatorID) {
    window.location.href = `/Master/OperatorForm/${OperatorID}/`
}