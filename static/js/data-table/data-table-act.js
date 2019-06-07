(function ($) {
 "use strict";
	
	$(document).ready(function() {
		$('#data-table-basic thead tr').clone(true).appendTo('#data-table-basic thead');
		$('#data-table-basic thead tr:eq(1) th').each(function (i) {
			var title = $(this).text();
			if (title != "") {
				$(this).html('<input type="text" placeholder="Search ' + title + '" />');
			}
			//window.alert(title);


			$('input', this).on('keyup change', function () {
				if (table.column(i).search() !== this.value) {
					//window.alert(i);
					if (i == 7) {
						return;
					}
					table
						.column(i)
						.search(this.value)
						.draw();
				}
			});
		});
		var table = $('#data-table-basic').DataTable({
			orderCellsTop: true,
			"columnDefs": [
				{
					'orderable' 	: false, 
                    'targets'       : [7],
               	},
			]
		});


		//get the list of ip addresses
		var cData = table.column(1).data();

		var editButton;
		var deleteButton;
		$('#data-table-basic tbody').on('click', 'td', function () {
			if ($(this).index() == 7) {
				return;
			}

			var data = table.row(this).data();
			//window.alert(data);

			// labels
			$("#labelDisplayName").text("Display Name:");
			$("#labelServerName").text("Server Name:");
			$("#labelUsername").text("Username:");
			$("#labelPasssword").text("Password:");
			$("#labelDomain").text("Domain:");
			$("#labelBTS").text("BTS:");
			$("#labelUE").text("UE:");

			// info
			$("#infoHeader").text(data[0] + " " + "(" + data[1] + ")");
			$('#infoDisplayName').text(data[0]);
			$('#infoServerName').text(data[1]);
			$('#infoUsername').text(data[2]);
			$('#infoPassword').text(data[3]);
			$('#infoDomain').text(data[4]);
			$('#infoBTS').text(data[5]);
			$('#infoUE').text(data[6]);

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