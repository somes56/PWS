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

function SearchVoyage() {
    var crit = {
        "mt": "Search Voyage",
        "fn": "Voyage",
        "p": {},
        "md": {
            "md1": "VoyageID",
            "md2": "VoyageNo",
            "md3": "ShipCallNo",
            "md4": "VesselCode",
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchLoadPort() {
    var crit = {
        "mt": "Search LoadPort",
        "fn": "Port",
        "p": {},
        "md": {
            "md1": "LoadPortID",
            "md2": "LoadPortName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchUnLoadPort() {
    var crit = {
        "mt": "Search UnLoadPort",
        "fn": "Port",
        "p": {},
        "md": {
            "md1": "UnLoadPortID",
            "md2": "UnLoadPortName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchDestinationPort() {
    var crit = {
        "mt": "Search DestinationPort",
        "fn": "Port",
        "p": {},
        "md": {
            "md1": "DestinationPortID",
            "md2": "DestionationPortName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchShippingAgent() {
    var crit = {
        "mt": "Search ShippingAgent",
        "fn": "Customer",
        "p": {},
        "md": {
            "md1": "ShippingAgentID",
            "md2": "ShippingAgentName"
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


function SubmitValidation() {
    var msg = [];
    var i = 0;

    if ($('#No').val() === "") {
        msg[i] = "No is required.";
        i = i + 1;
    }

    if ($('#VoyageID').val() === "" || $('#VoyageNo').val() === "") {
        msg[i] = "Voyage is required.";
        i = i + 1;
    }

    if ($('#ShipCallNo').val() === "") {
        msg[i] = "Ship Call No is required.";
        i = i + 1;
    }

    if ($('#VesselCode').val() === "") {
        msg[i] = "Vessel Code is required.";
        i = i + 1;
    }

    if ($('#LoadPortID').val() === "" || $('#LoadPortName').val() === "") {
        msg[i] = "Load Port is required.";
        i = i + 1;
    }

    if ($('#UnLoadPortID').val() === "" || $('#UnLoadPortName').val() === "") {
        msg[i] = "UnLoad Port is required.";
        i = i + 1;
    }

    if ($('#DestinationPortID').val() === "" || $('#DestionationPortName').val() === "") {
        msg[i] = "Destination Port is required.";
        i = i + 1;
    }

    if ($('#ShippingAgentID').val() === "" || $('#ShippingAgentName').val() === "") {
        msg[i] = "Shipping Agent is required.";
        i = i + 1;
    }

    if ($('#ConsigneeID').val() === "" || $('#ConsigneeName').val() === "") {
        msg[i] = "Consignee is required.";
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
    window.location.href = `/Import/OblForm`
}