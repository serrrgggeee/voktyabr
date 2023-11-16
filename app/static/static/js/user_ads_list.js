(function () {
    'use strict';
    function inser_ads(ads) {
        for(const ad in ads) {
            $('#article_ad_result').html(ads[ad].name);
        }
    }
    App.article_context_views = function (data) {
        var url = '/article/api/user_ads_list/';
        $.ajax({
            method: 'GET',
            data,
            xhrFields: {
              withCredentials: true
            },
            url: url
        }).done(function (resp) {
            inser_ads(resp)
        });
    };

})();