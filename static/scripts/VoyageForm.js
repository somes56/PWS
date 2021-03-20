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

    $('#Eta').datepicker({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
        yearRange: '2018:2050',
    });

    //     $('#btnPickDate').click(function() {
    //         $('#Eta').datepicker('show');
    //   });

})

function ConvertUpperCase(ID) {
    $(`#${ID}`).val($(`#${ID}`).val().toUpperCase())
}

function PickEta() {
    $('#Eta').datepicker('show');
}

function SearchVessel() {
    var crit = {
        "mt": "Search Vessel",
        "fn": "Vessel",
        "p": {},
        "md": {
            "md1": "VesselID",
            "md2": "VesselName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SubmitValidation() {
    var msg = [];
    var i = 0;

    if ($('#No').val() === "") {
        msg[i] = "Voyage No is required.";
        i = i + 1;
    }

    if ($('#ShipCallNo').val() === "") {
        msg[i] = "Ship Call No is required.";
        i = i + 1;
    }

    if ($('#VesselID').val() === "" || $('#VesselName').val() === "") {
        msg[i] = "Vessel is required.";
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
    window.location.href = `/Master/VoyageForm`
}