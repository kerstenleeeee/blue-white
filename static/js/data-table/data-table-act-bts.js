(function ($) {
 "use strict";
	
	$(document).ready(function() {
		$('#data-table-basic thead tr:eq(1) th').each(function (i) {
			var title = $(this).text();
			if (title != "") {
				$(this).html('<input type="text" placeholder="Search ' + title + '" />');
			}
			//window.alert(title);


			$('input', this).on('keyup change', function () {
				if (table.column(i).search() !== this.value) {
					//window.alert(i);
					if (i == 8) {
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
                    'targets'       : [8],
               	},
			],
			"bLengthChange": false,
			"scrollY":        "200px",
			"scrollX":        "200px",
        	"scrollCollapse": true,
        	"paging":         false,
        	"aoColumnDefs": [
        		{
					'searchable' 	: false, 
                    'targets'       : [5],
               	},
        	]
		});


		//get the list of ip addresses
		var cData = table.column(1).data();

		var editButton;
		var deleteButton;
		$('#data-table-basic tbody').on('click', 'td', function () {
			if ($(this).index() == 8) {
				return;
			}
			
			var data = table.row(this).data();
			
			// window.alert(data[7]);


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

			
			//window.alert(data[7]);

			if (data[6] == "TM500") {
				// $("#labelTMU").text("Username:");
				// $("#labelTMP").text("Password:");
				$("#labelTMT").text("TENV:");

				// $('#infoTMU').text(data[7]);
				// $('#infoTMP').text(data[8]);
				$('#infoTMT').text(data[7]);
			}
			else{
				// $("#labelTMU").text("");
				// $("#labelTMP").text("");
				$("#labelTMT").text("");

				// $('#infoTMU').text("");
				// $('#infoTMP').text("");
				$('#infoTMT').text("");
				document.getElementById("btsFetch").style.display = "table";
				// window.alert("yes")
				if (data[7] == 1) {
					// window.alert("Hello");
					document.getElementById("btsInfoButton").style.display = "table";
					$('#labelFetch').text("Last Fetch: ");
					$('#labelWCDMAPilot').text("workspaceWCDMA_Pilot: ");
					$('#labelGTAPluginGiant').text("GTA_Plugin_Giant: ");
					$('#labelDSPExplorer').text("DSPExplorer: ");

					$('#infoFetch').text(data[9]);
					$('#infoWCDMAPilot').text(data[10]);
					$('#infoGTAPluginGiant').text(data[11]);
					$('#infoDSPExplorer').text(data[12]);
				}
				else{
					document.getElementById("btsInfoButton").style.display = "none";
				}
			}		

			// alert('You clicked on ' + data[0] + '\'s row');
		});
	});
 
})(jQuery); 