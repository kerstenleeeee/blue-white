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
			
			//window.alert(data[6]);


			// labels

			$("#labelDisplayName").text("Display Name:");
			$("#labelServerName").text("Server Name:");
			$("#labelUsername").text("Username:");
			$("#labelPasssword").text("Password:");
			$("#labelDomain").text("Domain:");

			$("#labelLocation").text("LOCATION");
			$("#labelPCRack").text("PC Rack:");
			$("#labelBTSRack").text("BTS Rack:");
			$("#labelTTRack").text("Test Terminal Rack:");

			// info
			$("#infoHeader").text(data[0] + " " + "(" + data[1] + ")");
			$('#infoDisplayName').text(data[0]);
			$('#infoServerName').text(data[1]);
			$('#infoUsername').text(data[2]);
			$('#infoPassword').text(data[3]);
			$('#infoDomain').text(data[4]);
			// window.alert(data[11]);
			$('#infoPCRack').text(data[11]);
			$('#infoBTSRack').text(data[13]);
			$('#infoTTRack').text(data[14]);
			//window.alert(data[6]);

			if (data[6] == "TM500") {
				// $("#labelTMU").text("Username:");
				// $("#labelTMP").text("Password:");
				//window.alert(data[6]);
				$("#labelTM").text("TM500 IP:");

				// $('#infoTMU').text(data[7]);
				// $('#infoTMP').text(data[8]);
				$('#infoTM').text(data[12]);
				$("#labelTMRack").text("");
				$('#infoTMRack').text("");
			}
			else{
				$("#labelTM").text("");
				$('#infoTM').text("");
				$("#labelTMRack").text("");
				$('#infoTMRack').text("");
			}

			//window.alert(data[15]);
			if (data[15] == 1) {
				$("#labelBTS").text("BTS:");
				$("#labelUE").text("UE:");
				$('#infoBTS').text(data[5]);
				$('#infoUE').text(data[6]);
			}
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
					//window.alert(data[10])
					var toolInfo = data[10].split("<br>")
					//var toolInfo = data[10].match(/\b[\w']+(?:[^\w\n]+[\w']+){0,2}\b/g);
					//window.alert(toolInfo)
					$('#infoTool').text(toolInfo);
					//$('#infoGTAPluginGiant').text(data[11]);
					//$('#infoDSPExplorer').text(data[12]);
				}
				else{
					document.getElementById("btsInfoButton").style.display = "none";
				}
			// alert('You clicked on ' + data[0] + '\'s row');
		});
	});
 
})(jQuery); 