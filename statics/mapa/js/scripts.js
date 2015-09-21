$(function () {
    $('a').click(function () {
        var url = $(this).attr('rel');
        $('#iframe').attr('src', url);
    });
    $('.area').click(function () {
        var url = $(this).attr('rel');
        $('#iframe').attr('src', url);
    });
});
