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


function Numbers(evt) {

    var e = event || evt;
    var charCode = e.which || e.keyCode;

    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}

function NumberDecimals(evt) {
    if ((evt.which != 46 || $(this).val().indexOf('.') != -1) && (evt.which < 48 || evt.which > 57))
        return false;
    return true;
}

function SearchState() {
    var crit = {
        "mt": "Search State",
        "fn": "State",
        "p": {},
        "md": {
            "md1": "StateID",
            "md2": "StateName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchCountry() {
    var crit = {
        "mt": "Search Country",
        "fn": "Country",
        "p": {},
        "md": {
            "md1": "CountryID",
            "md2": "CountryName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SearchTerm() {
    var crit = {
        "mt": "Search Term",
        "fn": "Term",
        "p": {},
        "md": {
            "md1": "TermID",
            "md2": "TermName"
        }
    };
    OpenAdvSearch(JSON.stringify(crit));
}

function SubmitValidation() {
    var msg = [];
    var i = 0;

    if ($('#Name').val() === "") {
        msg[i] = "Company is required.";
        i = i + 1;
    }

    if ($('#Pic').val() === "") {
        msg[i] = "Contact Person is required.";
        i = i + 1;
    }

    if ($('#MobileNo').val() === "") {
        msg[i] = "Mobile No is required.";
        i = i + 1;
    }

    if ($('#TelNo').val() === "") {
        msg[i] = "Tel No is required.";
        i = i + 1;
    }

    if ($('#Email').val() === "") {
        msg[i] = "Email is required.";
        i = i + 1;
    }

    if ($('#Address').val() === "") {
        msg[i] = "Address is required.";
        i = i + 1;
    }

    if ($('#City').val() === "") {
        msg[i] = "City is required.";
        i = i + 1;
    }

    if ($('#PostCode').val() === "") {
        msg[i] = "Post Code is required.";
        i = i + 1;
    }

    if ($('#StateID').val() === "" || $('#StateName').val() === "") {
        msg[i] = "State is required.";
        i = i + 1;
    }

    if ($('#CountryID').val() === "" || $('#CountryName').val() === "") {
        msg[i] = "Country is required.";
        i = i + 1;
    }

    if ($('#TermID').val() === "" || $('#TermName').val() === "") {
        msg[i] = "Term is required.";
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
    window.location.href = `/Master/CustomerForm`
}