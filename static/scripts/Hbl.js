$(function () {
    PartialHblList()

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

function PartialHblList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Import/PartialHblList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialHblListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialHblListLoading').hide();
            $('#PartialHblList').text('Error in loading Hbl List');
        },
        success: function (data) {
            $('#PartialHblListLoading').hide();
            $('#PartialHblList').html(data);
        },
        type: "GET"
    });
}

function DeleteHbl(HblID, HblNo) {
    var Dlg = confirm(`Are you sure to delete ${HblNo} ?`)

    if (Dlg == true) {
        var url = `/Import/DeleteHbl/${HblID}/`
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
                PartialHblList();
            },
            type: "POST"
        });

    }
}

function GoToAddPage() {
    window.location.href = `/Import/HblForm`
}

function GoToEditPage(HblID) {
    window.location.href = `/Import/HblForm/${HblID}/`
}


