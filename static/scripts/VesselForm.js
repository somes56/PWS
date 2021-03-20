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

function SearchPortOperator() {
    var crit = {
        "mt": "Search Port Operator",
        "fn": "Customer",
        "p": {},
        "md": {
            "md1": "PortOperatorID",
            "md2": "PortOperatorName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchPsa() {
    var crit = {
        "mt": "Search Psa",
        "fn": "Customer",
        "p": {},
        "md": {
            "md1": "PsaID",
            "md2": "PsaName"
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

function SubmitValidation() {
    var msg = [];
    var i = 0;

    if ($('#Code').val() === "") {
        msg[i] = "Code is required.";
        i = i + 1;
    }

    if ($('#Name').val() === "") {
        msg[i] = "Name is required.";
        i = i + 1;
    }

    if ($('#PortOperatorID').val() === "" || $('#PortOperatorName').val() === "") {
        msg[i] = "Port Operator is required.";
        i = i + 1;
    }

    if ($('#PsaID').val() === "" || $('#PsaName').val() === "") {
        msg[i] = "Psa is required.";
        i = i + 1;
    }

    if ($('#ShippingAgentID').val() === "" || $('#ShippingAgentName').val() === "") {
        msg[i] = "ShippingAgent is required.";
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
    window.location.href = `/Master/VesselForm`
}