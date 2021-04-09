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

function SearchContainerSize() {
    var crit = {
        "mt": "Search ContainerSize",
        "fn": "ContainerSize",
        "p": {},
        "md": {
            "md1": "ContainerSizeID",
            "md2": "ContainerSizeName"
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

    if ($('#SealNo').val() === "") {
        msg[i] = "Seal No is required.";
        i = i + 1;
    }

    if ($('#ContainerSizeID').val() === "" || $('#ContainerSizeName').val() === "") {
        msg[i] = "Container Size is required.";
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
    window.location.href = `/Import/ContainerForm`
}