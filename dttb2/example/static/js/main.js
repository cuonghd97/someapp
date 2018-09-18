$(document).ready(function () {
    var table = $('#example').DataTable({
        "ajax": {
            "type": "GET",
            "url": "/index",
            "contentType": "application/json; charset=utf-8",
            "data": function (result) {
                data = JSON.stringify(result)
                return data
            },
            "displayLength": 10,
        },
        "columnDefs": [ {
            "targets": 3,
            "data": null,
            "defaultContent": "<button>Click!</button>"
        } ],
        createdRow: function( row, data, dataIndex ) {
            $(row).find('button').attr('data-id', data[0]).attr('data-toggle', 'modal').attr('data-target', '#myModal');
        },
        
    })
    // $('body').on('click','button', function() {
    //     console.log($(this).data('id'));
    // });
    $('#example tbody').on( 'click', 'button', function () {
        let data = table.row( $(this).parents('tr') ).data();
        $("#name").val(data[1]);
        $("#age").val(data[2]);
        $("#id").val(data[0]);
    } );

    $("#btnpost").on("click", function () {
        var id = $("#id").val()
        var names = $("#name").val()
        var age = $("#age").val()
        $.ajax({
            type: 'POST',
            url: location.href,
            data: {
                'id': id,
                'names': names,
                'age': age,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                // $("#myModal").modal('hide')
                console.log(id + " " + names + " " + age)
                // alert("success")
                // $('#example').DataTable().ajax.reload(null,false);
                table.ajax.reload(null, false)
            }
        })
    });
});