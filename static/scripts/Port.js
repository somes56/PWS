$(function(){
    PartialPortList()

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

function PartialPortList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Master/PartialPortList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber !='0' ? url + `?page=${PageNumber}` : url;

    $('#PartialPortListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialPortListLoading').hide();
            $('#PartialPortList').text('Error in loading Port List');
        },
        success: function (data) {
            $('#PartialPortListLoading').hide();
            $('#PartialPortList').html(data);
        },
        type: "GET"
    });
}

function DeletePort(PortID, PortName){
    var Dlg = confirm(`Are you sure to delete ${PortName} ?`)

    if(Dlg == true){
        var url = `/Master/DeletePort/${PortID}/`
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
                PartialPortList();
            },
            type: "POST"
        });
        
    }
}

function GoToAddPage(){
    window.location.href = `/Master/PortForm`
}

function GoToEditPage(PortID){
    window.location.href = `/Master/PortForm/${PortID}/`
}