$(function(){
    PartialContainerSizeList()

    $(document).keypress(function (e) {
        if (e.keyCode === 13) {
            e.preventDefault();
            return false;
        }
    });

    $(document).keydown(function (e) {
        if (e.keyCode === 8 && !$(e.target).is("input, textarea")){
            e.preventDefault();
            return false;
        }
    });
})

function PartialContainerSizeList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Master/PartialContainerSizeList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber !='0' ? url + `?page=${PageNumber}` : url;

    $('#PartialContainerSizeListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialContainerSizeListLoading').hide();
            $('#PartialContainerSizeList').text('Error in loading Container Size List');
        },
        success: function (data) {
            $('#PartialContainerSizeListLoading').hide();
            $('#PartialContainerSizeList').html(data);
        },
        type: "GET"
    });
}

function DeleteContainerSize(ContainerSizeID, Name){
    var Dlg = confirm(`Are you sure to delete ${Name} ?`)

    if(Dlg == true){
        var url = `/Master/DeleteContainerSize/${ContainerSizeID}/`
        $.ajax({
            url: url,
            cache: false,
            error: function () {
                alert('Delete Fail');
            },
            success: function (data) {
                if(data == 'True'){
                    alert('Deleted Successfully');
                }else{
                    alert('Delete Fail');
                }
                PartialContainerSizeList();
            },
            type: "POST"
        });
        
    }
}

function GoToAddPage(){
    window.location.href = `/Master/ContainerSizeForm`
}

function GoToEditPage(ContainerSizeID){
    window.location.href = `/Master/ContainerSizeForm/${ContainerSizeID}/`
}