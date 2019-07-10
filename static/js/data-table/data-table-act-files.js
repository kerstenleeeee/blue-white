(function ($) {
 "use strict";
	
	$(document).ready(function() {
		var table = $('#data-table-basic-files').DataTable({
			orderCellsTop: true,
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
		$('#data-table-basic-files tbody').on('click', 'td', function () {
			
			var data = table.row(this).data();
		});
	});
 
})(jQuery); 