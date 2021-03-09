$(function(){
    PartialCustomerList()

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

function PartialCustomerList(PageNumber = '0') {
    var SearchStr = $('#SearchString').val();

    var url = `/Master/PartialCustomerList`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`
    url = PageNumber !='0' ? url + `?page=${PageNumber}` : url;

    $('#PartialCustomerListLoading').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#PartialCustomerListLoading').hide();
            $('#PartialCustomerList').text('Error in loading Customer List');
        },
        success: function (data) {
            $('#PartialCustomerListLoading').hide();
            $('#PartialCustomerList').html(data);
        },
        type: "GET"
    });
}

function DeleteCustomer(CustomerID, CustomerName){
    var Dlg = confirm(`Are you sure to delete ${CustomerName} ?`)

    if(Dlg == true){
        var url = `/Master/DeleteCustomer/${CustomerID}/`
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
                PartialCustomerList();
            },
            type: "POST"
        });
        
    }
}

function GoToAddPage(){
    window.location.href = `/Master/CustomerForm`
}

function GoToEditPage(CustomerID){
    window.location.href = `/Master/CustomerForm/${CustomerID}/`
}


