function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = $.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            var csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function () {
    $('#calc_pickle_btn').click(function () {
        var params = {};
        $('.pickle-param').each(function () {
            if ($(this).val().length) {
                params[$(this).attr('id')] = $(this).val();
            }
            else {
                console.log(123);
                console.log('ID:' + $(this).attr('id') + ';');
                $.notify(
                    "Please set all pickle params",
                    {autoHide: false, style: 'bootstrap', className: 'error'}
                );
                return false;
            }
        });
        $.ajax({
            method: 'post',
            url: 'calc_pickle/',
            dataType: 'json',
            data: params,
            success: function(data) {
                data.error ?
                    $.notify(data.error, {autoHide: false, style: 'bootstrap', className: 'error'})
                    : $.notify(data['class'], {autoHide: true, autoHideDelay: 2500, style: 'bootstrap', className: 'success'});
            }
        });
    });
    $('#change_pickle_btn').click(function () {
        var pname = $('#new_pickle_name').val();
        if (!pname.length) {
            $.notify("Please set pickle name", {autoHide: false, style: 'bootstrap', className: 'error'});
        }
        $.ajax({
            method: 'get',
            url: 'change_pickle/',
            data: {pickle: pname},
            success: function(data) {
                data.error ? $.notify(data.error, {autoHide: false, style: 'bootstrap', className: 'error'}) : window.location.replace('');
            }
        });
    });
});
