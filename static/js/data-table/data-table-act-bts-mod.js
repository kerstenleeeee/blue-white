(function ($) {
 "use strict";
	
	$(document).ready(function() {
		var table = $('#data-table-basic-mod').DataTable({
			orderCellsTop: true,
			"bLengthChange": false,
        	"scrollCollapse": true,
        	"paging":         false,
        	"bFilter": false
		});


		//get the list of ip addresses
		var cData = table.column(1).data();

		var editButton;
		var deleteButton;
		$('#data-table-basic-mod tbody').on('click', 'td', function () {
			if ($(this).index() == 7) {
				return;
			}
			
			var data = table.row(this).data();
			
			//window.alert(data[6]);


			// labels

			
		});
	});
 
})(jQuery); 