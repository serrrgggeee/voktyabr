(function () {
    'use strict';
    var url = '/years/1/';
    App.years = function (url) {
        $.ajax({
            method: 'GET',
            xhrFields: {
	          withCredentials: true
	        },
            url: url
        }).done(function (resp) {
            var result = "<ul>";
            console.log(resp.years);
            resp.years.forEach(function(element) {
              result = result + "<li id='date_" + element + "'><a onclick='App.article_context_views(" + element + ")'; data-toggle='modal' data-target='#myModal' href='#'>" + element + "</a></li>"; 
            });
            result = result + "</ul>";
            console.log(result);
            $('#date_result').html(result);
            return resp
        });
    };
    App.years(url);

})();