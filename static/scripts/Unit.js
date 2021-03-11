$(function(){
    PartialUnitList()

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

function PartialUnitList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Master/PartialUnitList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber !='0' ? url + `?page=${PageNumber}` : url;

    $('#PartialUnitListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialUnitListLoading').hide();
            $('#PartialUnitList').text('Error in loading Unit List');
        },
        success: function (data) {
            $('#PartialUnitListLoading').hide();
            $('#PartialUnitList').html(data);
        },
        type: "GET"
    });
}

function DeletePort(UnitID, ShortName){
    var Dlg = confirm(`Are you sure to delete ${ShortName} ?`)

    if(Dlg == true){
        var url = `/Master/DeleteUnit/${UnitID}/`
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
                PartialUnitList();
            },
            type: "POST"
        });
        
    }
}

function GoToAddPage(){
    window.location.href = `/Master/UnitForm`
}

function GoToEditPage(UnitID){
    window.location.href = `/Master/UnitForm/${UnitID}/`
}