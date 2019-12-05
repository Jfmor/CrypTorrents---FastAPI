function init_button(id, magnet)
{
    $("#" + id).on("click", function () {
        prompt("Copy this with CTRL + C", magnet);
    });
}


$(document).ready(function () {
    $("#my-btn-search").on("click", function () {
        let url = "/torrents/" + $("#my-form-query").val();
        document.location.href = url;
    });
});