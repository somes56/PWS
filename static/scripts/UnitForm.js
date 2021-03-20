$(function () {
    $("#ClientVerifyBlock").hide();

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

function ConvertUpperCase(ID) {
    $(`#${ID}`).val($(`#${ID}`).val().toUpperCase())
}

function SubmitValidation() {
    var msg = [];
    var i = 0;

    if ($('#Code').val() === "") {
        msg[i] = "Code is required.";
        i = i + 1;
    }

    if ($('#ShortName').val() === "") {
        msg[i] = "Short Name is required.";
        i = i + 1;
    }

    if ($('#FullName').val() === "") {
        msg[i] = "Full Name is required.";
        i = i + 1;
    }

    if (msg.length > 0) {
        $("#ClientVerifyMsg").html(msg.join("<br/>"));

        $("#ClientVerifyBlock").show();

        return false;
    } else {
        return true;
    }
}

function ResetForm() {
    window.location.href = `/Master/UnitForm`
}