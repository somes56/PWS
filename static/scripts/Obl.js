$(function () {
    PartialOblList()

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

function PartialOblList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Import/PartialOblList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialOblListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialOblListLoading').hide();
            $('#PartialOblList').text('Error in loading Obl List');
        },
        success: function (data) {
            $('#PartialOblListLoading').hide();
            $('#PartialOblList').html(data);
        },
        type: "GET"
    });
}

function DeleteObl(OblID, OblNo) {
    var Dlg = confirm(`Are you sure to delete ${OblNo} ?`)

    if (Dlg == true) {
        var url = `/Import/DeleteObl/${OblID}/`
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
                PartialOblList();
            },
            type: "POST"
        });

    }
}

function GoToAddPage() {
    window.location.href = `/Import/OblForm`
}

function GoToEditPage(OblID) {
    window.location.href = `/Import/OblForm/${OblID}/`
}


