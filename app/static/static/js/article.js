(function () {
    'use strict';
    App.article_context_views = function (year) {
        var url = '/article/api/list/?year='+year;
        $.ajax({
            method: 'GET',
            xhrFields: {
              withCredentials: true
            },
            url: url
        }).done(function (resp) {
            var result = "<ul>";
            for(var key in resp) {
                result = result + "<li id='" + resp[key].pk + "'><a href='/article/" + resp[key].pk + "/'>" + resp[key].name + "</a></li>"; 
              console.log(resp[key]);
            };
            var result = result + "</ul>";

        
            $('#article_context').html(result);
        });
    };

})();