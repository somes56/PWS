$(function () {
    PartialUnstuffContainerPendingList()
    PartialUnstuffContainerCompletedList()

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

function PartialUnstuffContainerPendingList(PageNumber = '0') {
    var SearchStr = $('#SearchPendingString').val();

    var url = `/Import/PartialUnstuffContainerPendingList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialUnstuffContainerPendingListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialUnstuffContainerPendingListLoading').hide();
            $('#PartialUnstuffContainerPendingList').text('Error in loading Container List');
        },
        success: function (data) {
            $('#PartialUnstuffContainerPendingListLoading').hide();
            $('#PartialUnstuffContainerPendingList').html(data);
        },
        type: "GET"
    });
}

function PartialUnstuffContainerCompletedList(PageNumber = '0') {
    var SearchStr = $('#SearchCompletedString').val();

    var url = `/Import/PartialUnstuffContainerCompletedList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber != '0' ? url + `?page=${PageNumber}` : url;

    $('#PartialUnstuffContainerCompletedListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialUnstuffContainerCompletedListLoading').hide();
            $('#PartialUnstuffContainerCompletedList').text('Error in loading Container List');
        },
        success: function (data) {
            $('#PartialUnstuffContainerCompletedListLoading').hide();
            $('#PartialUnstuffContainerCompletedList').html(data);
        },
        type: "GET"
    });
}

function GoToEditPage(ContainerID) {
    window.location.href = `/Import/UnstuffContainerForm/${ContainerID}/`
}


