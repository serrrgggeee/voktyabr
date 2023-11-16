(function () {
    'use strict';
    function add_to_publication(pk) {
        return `<div  data-pk=${pk} class='unmute'>Поставить на публикацию</div>`
    }

    function remove_from_publication(pk) {
        return `<div data-pk=${pk} class='mute'>Снять с публикации</div>`
    }

    function ad_template_item_managment(data) {
        let publication = add_to_publication(data.pk)

        if(data.show) {
            publication = remove_from_publication(data.pk)
        }

        const result = `
            <div class='management'>
                ${publication}
            </div>
        `;
        return result;

    }

    function ad_template_item(data){
        let result = '';
        if(data.name) {
            result += `
                <div class='title'>
                    ${data.name}
                </div>`;
            result += `
                <div class='description'>
                    ${data.description}
                </div>`;
        }
        if(result.length > 0) {
            result += ad_template_item_managment(data);
        }

        return result;
    }

    function inser_ads(ads) {
        for(const ad in ads) {
            $('#article_ad_result').html(ad_template_item(ads[ad]));
        }
    }

    function mute_ad(e) {
        const pk = $(this).attr('data-pk');
        ad_hide(pk).then((res) => {
            App.article_context_views({'username': username, 'password': password });
        });
    }

    function unmute_ad(e) {
        const pk = $(this).attr('data-pk');
        ad_show(pk).then((res) => {
            App.article_context_views({'username': username, 'password': password });
        });
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

    function ad_show (pk) {
        var url = `/article/api/user_ad_show_api/${pk}/`;
        return $.ajax({
            method: 'GET',
            xhrFields: {
              withCredentials: true
            },
            url: url
        }).done(function (resp) {
            console.log(resp)
        });
    };

    function ad_hide (pk) {
        var url = `/article/api/user_ad_hide_api/${pk}/`;
        return $.ajax({
            method: 'GET',
            xhrFields: {
              withCredentials: true
            },
            url: url
        }).done(function (resp) {
            console.log(resp)
        });
    };

    $(document).on("click",".mute",mute_ad);
    $(document).on("click",".unmute",unmute_ad);

})();