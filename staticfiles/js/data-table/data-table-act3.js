(function ($) {
 "use strict";
	
	$(document).ready(function() {
		$('#data-table-basic-ue thead tr:eq(1) th').each(function (i) {
					
			//window.alert(title);


			$('input', this).on('keyup change', function () {
				if (table.column(i).search() !== this.value) {
					//window.alert(i);
					if (i == 1) {
						return;
					}
					table
						.column(i)
						.search(this.value)
						.draw();
				}
			});
		});
		var table = $('#data-table-basic-ue').DataTable({
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
		$('#data-table-basic-ue tbody').on('click', 'td', function () {
			if ($(this).index() == 1) {
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