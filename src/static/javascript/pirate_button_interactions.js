function init_button(id, magnet)
{
    $("#" + id).on("click", function () {
        prompt("Copy this with CTRL + C", magnet);
    });
}


$(document).ready(function () {
    $("#my-btn-search").on("click", function () {
        let query = $("#my-form-query").val();
        window.location.href = "/torrent/" + query;
    });
});