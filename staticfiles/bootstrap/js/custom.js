function popupFunction(link) {
    window.open(link, "popup", "width=800, height=600");
}

$(document).ready(function () {
    /*Photos*/
    var modalDiv = $("#photoContent");
    $(".btn-photo").on("click", function () {
        $.ajax({
            url: $(this).attr("href"),
            success: function (data) {
                modalDiv.html(data);
                $("#photoModal").modal('show');
                $(".modal").on("hidden.bs.modal", function () {
                    $("#photoContent").html("");
                });
            }
        });
    });
});