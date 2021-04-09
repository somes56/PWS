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

    $('#UnstuffDate').datepicker({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
        yearRange: '2018:2050',
    });


    $('input[name="Transhipment"]').on('click', function (e) {
        if (e.target.value === '0') {
            $('#PortID').val('');
            $('#PortName').val('');
        }
    });
})

function PickUnstuffDate() {
    $('#UnstuffDate').datepicker('show');
}

function ConvertUpperCase(ID) {
    $(`#${ID}`).val($(`#${ID}`).val().toUpperCase())
}

function SearchHbl() {
    var crit = {
        "mt": "Search Hbl By Container",
        "fn": "HblByContainer",
        "p": {
            "p1": $('#ContainerID').val()
        },
        "md": {}
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchPort() {
    var crit = {
        "mt": "Search Port",
        "fn": "Port",
        "p": {},
        "md": {
            "md1": "PortID",
            "md2": "PortName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function AdvSearchCustomSel(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,
    v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,
    v21, v22, v23, v24, v25) {

    $('#HblID').val(v1).trigger('change');
    $('#No').val(v2).trigger('change');
    $('#ConsigneeName').val(v3).trigger('change');
    $('#ClassFullName').val(v4).trigger('change');
    $('#UnitShortName').val(v5).trigger('change');

    $('#PortID').val(v6).trigger('change');
    $('#PortName').val(v7).trigger('change');
    $('#Quantity').val(v8).trigger('change');
    $('#Weight').val(v9).trigger('change');
    $('#Volume').val(v10).trigger('change');

    $('input[name="Transhipment"]').val([v11]).trigger('change');
    $('#MarkDesc').val(v12).trigger('change');
    $('#CargoDesc').val(v13).trigger('change');
    $('input[name="InwardSurvey"]').val([v14]).trigger('change');
    $('#PackageDesc').val(v15).trigger('change');

    $('#LocationDesc').val(v16).trigger('change');
    $('#Remarks').val(v17).trigger('change');
    $('input[name="HeavyLiftCargo"]').val([v18]).trigger('change');
    $('input[name="LongLengthCargo"]').val([v19]).trigger('change');
    $('input[name="PortPolice"]').val([v20]).trigger('change');

    $('input[name="CargoSurvey"]').val([v21]).trigger('change');
    $('input[name="MaqisHold"]').val([v22]).trigger('change');
    $('input[name="HealthHold"]').val([v23]).trigger('change');
    $('input[name="PreventiveHold"]').val([v24]).trigger('change');
    $('input[name="CustomsHold"]').val([v25]).trigger('change');

    $('#AdvSearchModal').modal('hide');
}

function SubmitValidation() {
    var msg = [];
    var i = 0;

    if ($('#ContainerID').val() === "" || $('#ContainerNo').val() === "") {
        msg[i] = "Container is required.";
        i = i + 1;
    }

    if ($('#IsUnStuff').prop('checked') === true && $('#UnstuffDate').val() === "") {
        msg[i] = "Unstuff Date is required.";
        i = i + 1;
    }

    if ($('input[name="Transhipment"]:checked').val() === '1' && ($('#PortID').val() === "" || $('#PortName').val() === "")) {
        msg[i] = "Port is required.";
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

function OnCheckUnstuff(Checked) {
    if (Checked === false) {
        $('#UnstuffDate').val('')
    }
}

function ResetForm() {
    var ContainerID = $('#ContainerID').val()
    window.location.href = `/Import/UnstuffContainerForm/${ContainerID}`
}
