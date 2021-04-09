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

    $('#OblID').on('change', function () {
        $('#ContainerID').val('')
        $('#ContainerNo').val('')
    });
})

function ConvertUpperCase(ID) {
    $(`#${ID}`).val($(`#${ID}`).val().toUpperCase())
}

function SearchObl() {
    var crit = {
        "mt": "Search Obl",
        "fn": "Obl",
        "p": {},
        "md": {
            "md1": "OblID",
            "md2": "OblNo"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchContainer(OblID) {
    var crit = {
        "mt": "Search Container",
        "fn": "ContainerByObl",
        "p": {
            "p1": OblID
        },
        "md": {
            "md1": "ContainerID",
            "md2": "ContainerNo"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchConsignee() {
    var crit = {
        "mt": "Search Consignee",
        "fn": "Customer",
        "p": {},
        "md": {
            "md1": "ConsigneeID",
            "md2": "ConsigneeName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchClass() {
    var crit = {
        "mt": "Search Class",
        "fn": "Class",
        "p": {},
        "md": {
            "md1": "ClassID",
            "md2": "ClassFullName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchUnit() {
    var crit = {
        "mt": "Search Unit",
        "fn": "Unit",
        "p": {},
        "md": {
            "md1": "UnitID",
            "md2": "UnitShortName"
        }
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

function SubmitValidation() {
    var msg = [];
    var i = 0;

    if ($('#No').val() === "") {
        msg[i] = "No is required.";
        i = i + 1;
    }

    if ($('#OblID').val() === "" || $('#OblNo').val() === "") {
        msg[i] = "Obl is required.";
        i = i + 1;
    }

    if ($('#ContainerID').val() === "" || $('#ContainerNo').val() === "") {
        msg[i] = "Container is required.";
        i = i + 1;
    }

    if ($('#ConsigneeID').val() === "" || $('#ConsigneeName').val() === "") {
        msg[i] = "Consignee is required.";
        i = i + 1;
    }

    if ($('#ClassID').val() === "" || $('#ClassFullName').val() === "") {
        msg[i] = "Class is required.";
        i = i + 1;
    }

    if ($('#UnitID').val() === "" || $('#UnitID').val() === "") {
        msg[i] = "Package is required.";
        i = i + 1;
    }

    if ($('#PortID').val() === "" || $('#PortName').val() === "") {
        msg[i] = "Port is required.";
        i = i + 1;
    }

    if ($('#Quantity').val() === "") {
        msg[i] = "Quantity is required.";
        i = i + 1;
    }

    if ($('#Weight').val() === "") {
        msg[i] = "Weight is required.";
        i = i + 1;
    }

    if ($('#Volume').val() === "") {
        msg[i] = "Volume is required.";
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
    window.location.href = `/Import/HblForm`
}

