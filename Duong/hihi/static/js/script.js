$(document).ready(function () {
    $("#btnsubmit").on('click', function () {
        var username = $("#username").val()
        var email = $("#email").val()
        var address = $("#address").val()
        var birthday = $("#birthday").val()
        console.log(username)
        console.log(email)
        console.log(address)
        console.log(birthday)
        $.ajax({
            type: 'POST',
            url: '/thankyou',
            data: {
                'userName': username,
                'email': email,
                'address': address,
                'birthDay': birthday,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            }
        })
    })
});