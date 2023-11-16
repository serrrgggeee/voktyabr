(function () {
    'use strict';
    App.article_context_views = function (data) {
        var url = '/article/api/add/';
        console.log(data);
        $.ajax({
            method: 'POST',
            data,
            xhrFields: {
              withCredentials: true
            },
            url: url
        }).done(function (resp) {
            $('#article_add_result').html(resp);
        });
    };

    $('#form').submit(function (e) {
        e.preventDefault();
        var form = $(this);
        var name = form.attr('name');
        App.article_context_views(form.serialize())
    });
})();
