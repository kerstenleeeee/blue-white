(function ($) {
 "use strict";
	
	$(document).ready(function() {
		var table = $('#data-table-basic-tm500').DataTable({
			orderCellsTop: true,
			"columnDefs": [
				{
					'orderable' 	: false, 
                    'targets'       : [8],
               	},
			],
			"bLengthChange": false,
			"dom": '<"toolbar">frtip',
			"scrollY":        "200px",
			"scrollX":        "200px",
        	"scrollCollapse": true,
        	"paging":         false,
        	"aoColumnDefs": [
        		{
					'searchable' 	: false, 
                    'targets'       : [2, 3, 4, 5, 6, 7],
               	},
        	] 
		});


		//get the list of ip addresses
		var cData = table.column(1).data();

		var editButton;
		var deleteButton;
		$('#data-table-basic-tm500 tbody').on('click', 'td', function () {
			if ($(this).index() == 8) {
				return;
			}

			var data = table.row(this).data();
			window.alert(data);

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

			if (data[6] == "TM500") {
				// $("#labelTMU").text("Username:");
				// $("#labelTMP").text("Password:");
				$("#labelTMT").text("TENV:");

				// $('#infoTMU').text(data[7]);
				// $('#infoTMP').text(data[8]);
				$('#infoTMT').text(data[7]);
				document.getElementById("btsFetch").style.display = "table";
				// window.alert("no")
				if (data[7] == 0) {
					// window.alert(data[7])
				}
			}
			else{
				// $("#labelTMU").text("");
				// $("#labelTMP").text("");
				$("#labelTMT").text("");

				// $('#infoTMU').text("");
				// $('#infoTMP').text("");
				$('#infoTMT').text("");
			}		


			
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