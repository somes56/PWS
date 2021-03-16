$(function(){
    PartialItemList()

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

function PartialItemList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Master/PartialItemList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber !='0' ? url + `?page=${PageNumber}` : url;

    $('#PartialItemListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialItemListLoading').hide();
            $('#PartialItemList').text('Error in loading Item List');
        },
        success: function (data) {
            $('#PartialItemListLoading').hide();
            $('#PartialItemList').html(data);
        },
        type: "GET"
    });
}

function DeleteItem(ItemID, Name){
    var Dlg = confirm(`Are you sure to delete ${Name} ?`)

    if(Dlg == true){
        var url = `/Master/DeleteItem/${ItemID}/`
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
                PartialItemList();
            },
            type: "POST"
        });
        
    }
}

function GoToAddPage(){
    window.location.href = `/Master/ItemForm`
}

function GoToEditPage(ItemID){
    window.location.href = `/Master/ItemForm/${ItemID}/`
}