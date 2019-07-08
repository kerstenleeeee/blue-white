(function ($) {
 "use strict";
	
	$(document).ready(function() {
		var table = $('#data-table-basic-tm500-info').DataTable({
			orderCellsTop: true,
			"columnDefs": [
				{
					'orderable' 	: false, 
                    'targets'       : [1],
               	},
			],
			"bLengthChange": false,
        	"scrollCollapse": true,
        	"paging":         false,
        	"bFilter": false,
		});

		table.draw();


		//get the list of ip addresses
		var cData = table.column(1).data();

		var editButton;
		var deleteButton;
		$('#data-table-basic-tm500-info tbody').on('click', 'td', function () {
			if ($(this).index() == 0) {
				return;
			}
			
			var data = table.row(this).data();
			
			//window.alert(data[6]);


			// labels

			
		});
	});
 
})(jQuery); 