$(document).ready(function () {
    $("#checkall").change(function () {
        if (this.checked) {
            $(".bill").each(function () {
                this.checked = true;
            })
        } else {
            $(".bill").each(function () {
                this.checked = false;
            })
        }
    });

    $("#checkall").change(function () {
        totalIt()
    });

    $(".bill").click(function () {
        if ($(this).is(":checked")) {
            var isAllChecked = 0;
            $(".bill").each(function () {
                if (!this.checked)
                    isAllChecked = 1;
            })
            if (isAllChecked == 0) { $("#checkall").prop("checked", true); }
        } else {
            $("#checkall").prop("checked", false);
        }
    });
});

function totalIt() {
    var input = document.getElementsByClassName("bill");
    var total = 0;
    var items = 0;
    for (var i = 0; i < input.length; i++) {
        if (input[i].checked) {
            total += parseFloat(input[i].value);
            items += 1
        }
    }
    document.getElementsByName("billtotal")[0].value = "$" + total.toFixed(2);
    document.getElementsByName("itemtotal")[0].value = items.toFixed(0);
}