(function ($) {
 "use strict";
	
	$(document).ready(function() {
		var table = $('#data-table-basic-tm500').DataTable({
			orderCellsTop: true,
			"columnDefs": [
				{
					'orderable' 	: false, 
                    'targets'       : [5],
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
                    'targets'       : [2, 3, 4, 5],
               	},
        	] 
		});


		//get the list of ip addresses
		var cData = table.column(1).data();

		var editButton;
		var deleteButton;
		$('#data-table-basic-tm500 tbody').on('click', 'td', function () {
			if ($(this).index() == 5) {
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
			$("#labelPCRack").text("PC Rack:");
			$("#labelTMRack").text("TM500 Rack:");

			// info
			$("#infoHeader").text(data[0] + " " + "(" + data[1] + ")");
			$('#infoDisplayName').text(data[0]);
			$('#infoServerName').text(data[1]);
			$('#infoUsername').text(data[2]);
			$('#infoPassword').text(data[3]);
			$('#infoDomain').text(data[4]);
			$('#infoPCRack').text(data[7]);
			$('#infoTMRack').text(data[8]);

			if (data[9] == 2) {
				$("#labelBTS").text("");
				$("#labelUE").text("");
				$('#infoBTS').text("");
				$('#infoUE').text("");
				$("#labelTM").text("");
				$('#infoTM').text("");
				$("#labelBTSRack").text("");
				$("#labelTTRack").text("");
				$('#infoBTSRack').text("");
				$('#infoTTRack').text("");
			}

			document.getElementById("btsFetch").style.display = "table";
			// window.alert("yes")
			if (data[6] == 1) {
				window.alert("Hello");
			}
			else{
				document.getElementById("btsInfoButton").style.display = "none";
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