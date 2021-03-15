$(function(){
    PartialVesselList()

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

function PartialVesselList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Master/PartialVesselList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber !='0' ? url + `?page=${PageNumber}` : url;

    $('#PartialVesselListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialVesselListLoading').hide();
            $('#PartialVesselList').text('Error in loading Vessel List');
        },
        success: function (data) {
            $('#PartialVesselListLoading').hide();
            $('#PartialVesselList').html(data);
        },
        type: "GET"
    });
}

function DeleteVessel(VesselID, VesselName){
    var Dlg = confirm(`Are you sure to delete ${VesselName} ?`)

    if(Dlg == true){
        var url = `/Master/DeleteVessel/${VesselID}/`
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
                PartialVesselList();
            },
            type: "POST"
        });
        
    }
}

function GoToAddPage(){
    window.location.href = `/Master/VesselForm`
}

function GoToEditPage(VesselID){
    window.location.href = `/Master/VesselForm/${VesselID}/`
}