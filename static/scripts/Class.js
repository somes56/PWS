$(function () {
    PartialClassList()

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

function PartialClassList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Master/PartialClassList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialClassListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialClassListLoading').hide();
            $('#PartialClassList').text('Error in loading Class List');
        },
        success: function (data) {
            $('#PartialClassListLoading').hide();
            $('#PartialClassList').html(data);
        },
        type: "GET"
    });
}

function DeleteClass(CLassID, ShortName) {
    var Dlg = confirm(`Are you sure to delete ${ShortName} ?`)

    if (Dlg == true) {
        var url = `/Master/DeleteClass/${CLassID}/`
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
                PartialClassList();
            },
            type: "POST"
        });

    }
}

function GoToAddPage() {
    window.location.href = `/Master/ClassForm`
}

function GoToEditPage(ClassID) {
    window.location.href = `/Master/ClassForm/${ClassID}/`
}