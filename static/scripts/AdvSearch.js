//begin .js
$(function(){
    $('#AdvSearchModal').on('shown.bs.modal', Search);
})

function OpenAdvSearch(crit) {

    var objcrit = JSON.parse(crit);

    $('#TargetID').val('');
    $('#SearchString').val('');
    $('#SearchResult').empty();

    $('#TargetID').val(crit);
    $('#AdvSearchModalTitle').text(objcrit.mt);
    $('#AdvSearchModal').modal('show');
}

function Search() {

    var px = "";
    var SearchStr = $('#SearchString').val();
    var objcrit = JSON.parse($('#TargetID').val());

    for (var a in objcrit.p) {
        if (objcrit.p.hasOwnProperty(a)) {
            if ($('#' + objcrit.p[a]).val() === undefined) {
                px += a + "=" + objcrit.p[a] + "&";
            } else {
                px += a + "=" + $('#' + objcrit.p[a]).val() + "&";
            }
        }
    }

    var url = `/Cmn/AdvSearch${objcrit.fn}`;
    url = SearchStr === '' ? url : url + `/${SearchStr}`

    $('#AdvSearchLoadingBar').show();

    $.ajax({
        url: url,
        cache: false,
        error: function () {
            $('#SearchResult').html('<span style="color:red">Error in Loading ' + objcrit.fn + ' List.</span>');
            $('#AdvSearchLoadingBar').hide();
        },
        success: function (data) {
            $('#SearchResult').empty().append(data);
            $('#AdvSearchLoadingBar').hide();
        },
        type: "GET"
    });
}

function AdvSearchSelOne(v1) {

    var objcrit = JSON.parse($('#TargetID').val());
    AdvSearchFillResult(v1, objcrit.md.md1);
    $('#AdvSearchModal').modal('hide');
}

function AdvSearchSelTwo(v1, v2) {

    var objcrit = JSON.parse($('#TargetID').val());
    AdvSearchFillResult(v1, objcrit.md.md1);
    AdvSearchFillResult(v2, objcrit.md.md2);
    $('#AdvSearchModal').modal('hide');
}

function AdvSearchSelThree(v1, v2, v3) {

    var objcrit = JSON.parse($('#TargetID').val());
    AdvSearchFillResult(v1, objcrit.md.md1);
    AdvSearchFillResult(v2, objcrit.md.md2);
    AdvSearchFillResult(v3, objcrit.md.md3);
    $('#AdvSearchModal').modal('hide');
}

function AdvSearchSelFour(v1, v2, v3, v4) {

    var objcrit = JSON.parse($('#TargetID').val());
    AdvSearchFillResult(v1, objcrit.md.md1);
    AdvSearchFillResult(v2, objcrit.md.md2);
    AdvSearchFillResult(v3, objcrit.md.md3);
    AdvSearchFillResult(v4, objcrit.md.md4);
    $('#AdvSearchModal').modal('hide');
}

function AdvSearchSelFive(v1, v2, v3, v4, v5) {

    var objcrit = JSON.parse($('#TargetID').val());
    AdvSearchFillResult(v1, objcrit.md.md1);
    AdvSearchFillResult(v2, objcrit.md.md2);
    AdvSearchFillResult(v3, objcrit.md.md3);
    AdvSearchFillResult(v4, objcrit.md.md4);
    AdvSearchFillResult(v5, objcrit.md.md5);
    $('#AdvSearchModal').modal('hide');
}

function AdvSearchSelSix(v1, v2, v3, v4, v5, v6) {

    var objcrit = JSON.parse($('#TargetID').val());
    AdvSearchFillResult(v1, objcrit.md.md1);
    AdvSearchFillResult(v2, objcrit.md.md2);
    AdvSearchFillResult(v3, objcrit.md.md3);
    AdvSearchFillResult(v4, objcrit.md.md4);
    AdvSearchFillResult(v5, objcrit.md.md5);
    AdvSearchFillResult(v6, objcrit.md.md6);
    $('#AdvSearchModal').modal('hide');
}

function AdvSearchSelSeven(v1, v2, v3, v4, v5, v6, v7) {

    var objcrit = JSON.parse($('#TargetID').val());
    AdvSearchFillResult(v1, objcrit.md.md1);
    AdvSearchFillResult(v2, objcrit.md.md2);
    AdvSearchFillResult(v3, objcrit.md.md3);
    AdvSearchFillResult(v4, objcrit.md.md4);
    AdvSearchFillResult(v5, objcrit.md.md5);
    AdvSearchFillResult(v6, objcrit.md.md6);
    AdvSearchFillResult(v7, objcrit.md.md7);
    $('#AdvSearchModal').modal('hide');
}

function AdvSearchFillResult(v, md) {
    $('#' + md).val(v).trigger('change');
}
