$(function () {
    PartialVoyageList()

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

function PartialVoyageList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Master/PartialVoyageList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialVoyageListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialVoyageListLoading').hide();
            $('#PartialVoyageList').text('Error in loading Voyage List');
        },
        success: function (data) {
            $('#PartialVoyageListLoading').hide();
            $('#PartialVoyageList').html(data);
        },
        type: "GET"
    });
}

function DeleteVoyage(VoyageID, VoyageNo) {
    var Dlg = confirm(`Are you sure to delete ${VoyageNo} ?`)

    if (Dlg == true) {
        var url = `/Master/DeleteVoyage/${VoyageID}/`
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
                PartialVoyageList();
            },
            type: "POST"
        });

    }
}

function GoToAddPage() {
    window.location.href = `/Master/VoyageForm`
}

function GoToEditPage(VoyageID) {
    window.location.href = `/Master/VoyageForm/${VoyageID}/`
}