$(function () {
    PartialContainerList()

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

function PartialContainerList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Import/PartialContainerList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialContainerListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialContainerListLoading').hide();
            $('#PartialContainerList').text('Error in loading Container List');
        },
        success: function (data) {
            $('#PartialContainerListLoading').hide();
            $('#PartialContainerList').html(data);
        },
        type: "GET"
    });
}

function DeleteContainer(ContainerID, ContainerNo) {
    var Dlg = confirm(`Are you sure to delete ${ContainerNo} ?`)

    if (Dlg == true) {
        var url = `/Import/DeleteContainer/${ContainerID}/`
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
                PartialContainerList();
            },
            type: "POST"
        });

    }
}

function GoToAddPage() {
    window.location.href = `/Import/ContainerForm`
}

function GoToEditPage(ContainerID) {
    window.location.href = `/Import/ContainerForm/${ContainerID}/`
}


