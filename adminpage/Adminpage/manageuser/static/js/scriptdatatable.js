$(document).ready(function () {
    var table = $('#userinfo').on( 'order.dt',  function () { eventFired( 'Order' ); } )
    .on( 'search.dt', function () { eventFired( 'Search' ); } )
    .on( 'page.dt',   function () { eventFired( 'Page' ); } )
    .DataTable({
        "ajax": {
            "type": "GET",
            "url": "/info",
            "contentType": "application/json; charset=utf-8",
            "data": function (result) {
                data = JSON.stringify(result)
                return data
            },
            "displayLength": 10,
        },
        "columnDefs": [
            {
                "targets": [ 0 ],
                "visible": false,
                "searchable": false
            },
            {
                "targets": [ 1 ],
                "visible": false
            },
            {
                "targets": [ 2 ],
                "visible": false
            },
            {
                "targets": [ 7 ],
                "visible": false
            }
        ]
    })

});