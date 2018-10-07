$(document).ready(function () {
    // $("#btnsubmit").on('click', function () {
    //     var username = $("#username").val()
    //     var email = $("#email").val()
    //     var address = $("#address").val()
    //     var birthday = $("#birthday").val()
    //     console.log(username)
    //     console.log(email)
    //     console.log(address)
    //     console.log(birthday)
    //     $.ajax({
    //         type: 'POST',
    //         url: '/thankyou',
    //         data: {
    //             'userName': username,
    //             'email': email,
    //             'address': address,
    //             'birthDay': birthday,
    //             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    //         }
    //     })
    // })

    var table = $("#tbl").DataTable({
        "ajax": {
            "type": "GET",
            "url": "/data",
            "contentType": "application/json; charset=utf-8",
            "data": function (result) {
                data = JSON.stringify(result)
                return data
            },
            "displayLength": 10,
        },
        dom: 'Bfrtip',
        buttons: {
            buttons: [{
                    extend: 'copy',
                    className: 'copyButton'
                },
                {
                    extend: 'excel',
                    className: 'excelButton'
                },
                {
                    extend: 'pdf',
                    className: 'pdfButton'
                },
                {
                    extend: 'print',
                    className: 'printButton'
                }
            ]
        }
    });
    // $("body").find(".addButton").attr("data-toggle", "modal").attr("data-target", "#myModal")
    $("#btnadd").on("click", function () {
        var code = $("#addcode").val()
        $.ajax({
            type: 'POST',
            url: location.href,
            data: {
                'code': code,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                table.ajax.reload(null, false)          
            }
        })
    })
});