$(document).ready(function(){
    $('#btnsubmit').on('click', function(){
        var username = $('#username').val()
        var password = $('#password').val()
        
        $.ajax({
            type: 'POST',
            url: '',
            data: {
                'username': username,
                'password': password,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                alert('success')
            }
        })
    })
})