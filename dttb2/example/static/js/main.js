$(document).ready(function () {

    var table = $('#example').DataTable({
        "ajax": {
            "type": "GET",
            "url": "/index",
            "contentType": "application/json; charset=utf-8",
            "data": function (result) {
                return JSON.stringify(result)
            },
            "displayLength": 10
        },
        "columnDefs": [ {
            "targets": 2,
            "data": null,
            "defaultContent": "<button>Click!</button>"
        } ],
        createdRow: function( row, data, dataIndex ) {
            // Set the data-status attribute, and add a class
            $( row ).find('td:eq(0)')
                .attr('data-status', data.status ? 'locked' : 'unlocked')
                .addClass('asset-context box');
        }
    })

    
});