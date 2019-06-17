(function ($) {
 "use strict";
	
	$(document).ready(function() {
		var table = $('#data-table-basic-bts').DataTable({
			orderCellsTop: true,
			"columnDefs": [
				{
					'orderable' 	: false, 
                    'targets'       : [1],
               	},
			]
		});


		//get the list of ip addresses
		var cData = table.column(1).data();

		var editButton;
		var deleteButton;
		$('#data-table-basic-bts tbody').on('click', 'td', function () {
			if ($(this).index() == 7) {
				return;
			}

			var data = table.row(this).data();
			//window.alert(data[0]);

			// labels
			$("#labelBTS").text(data[0]);

			deleteButton = $(this).find(".deleteButton");
			
			// alert('You clicked on ' + data[0] + '\'s row');
		});
		$(".infoEditButton").click(function () {
			$(editButton).click();
		});

		$(".infoDeleteButton").click(function () {
			$(deleteButton).click();
		});
		$('.modal').on('hidden.bs.modal', function () {
			$("body").css("padding","0");
		})
	});
 
})(jQuery); 