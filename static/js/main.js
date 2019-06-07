(function ($) {
 "use strict";

		$(".chosen")[0] && $(".chosen").chosen({
            width: "100%",
            allow_single_deselect: !0
        });
		/*--------------------------
		 auto-size Active Class
		---------------------------- */	
		$(".auto-size")[0] && autosize($(".auto-size"));
		/*--------------------------
		 Collapse Accordion Active Class
		---------------------------- */	
		$(".collapse")[0] && ($(".collapse").on("show.bs.collapse", function(e) {
            $(this).closest(".panel").find(".panel-heading").addClass("active")
        }), $(".collapse").on("hide.bs.collapse", function(e) {
            $(this).closest(".panel").find(".panel-heading").removeClass("active")
        }), $(".collapse.in").each(function() {
            $(this).closest(".panel").find(".panel-heading").addClass("active")
        }));
		/*----------------------------
		 jQuery tooltip
		------------------------------ */
		$('[data-toggle="tooltip"]').tooltip();
		/*--------------------------
		 popover
		---------------------------- */	
		$('[data-toggle="popover"]')[0] && $('[data-toggle="popover"]').popover();
		/*--------------------------
		 File Download
		---------------------------- */	
		$('.btn.dw-al-ft').on('click', function(e) {
			e.preventDefault();
		});
		/*--------------------------
		 Sidebar Left
		---------------------------- */	
		$('#sidebarCollapse').on('click', function () {
			 $('#sidebar').toggleClass('active');
			 
		 });
		$('#sidebarCollapse').on('click', function () {
			$("body").toggleClass("mini-navbar");
			SmoothlyMenu();
		});
		$('.menu-switcher-pro').on('click', function () {
			var button = $(this).find('i.nk-indicator');
			button.toggleClass('notika-menu-befores').toggleClass('notika-menu-after');
			
		});
		$('.menu-switcher-pro.fullscreenbtn').on('click', function () {
			var button = $(this).find('i.nk-indicator');
			button.toggleClass('notika-back').toggleClass('notika-next-pro');
		});
		/*--------------------------
		 Button BTN Left
		---------------------------- */	
		
		$(".nk-int-st")[0] && ($("body").on("focus", ".nk-int-st .form-control", function() {
            $(this).closest(".nk-int-st").addClass("nk-toggled")
        }), $("body").on("blur", ".form-control", function() {
            var p = $(this).closest(".form-group, .input-group"),
                i = p.find(".form-control").val();
            p.hasClass("fg-float") ? 0 == i.length && $(this).closest(".nk-int-st").removeClass("nk-toggled") : $(this).closest(".nk-int-st").removeClass("nk-toggled")
        })), $(".fg-float")[0] && $(".fg-float .form-control").each(function() {
            var i = $(this).val();
            0 == !i.length && $(this).closest(".nk-int-st").addClass("nk-toggled")
        });
	
		
	

	
	var editID = null;
	$(".editButton").click(function () {
		editID = $(this).attr("value");
		$("#idValue").attr("value", editID);

		var parent = $(this).parent();
		var row = $(parent).siblings();

		$("#TC_OwnerEdit").val(row.eq(0).text());
		$("#TC_IDEdit").val(row.eq(1).text());
		$("#HW_RELEASEEdit").val(row.eq(2).text());
		$("#descriptionEdit").val(row.eq(3).text());
		$("#ws_folderEdit").val(row.eq(4).text());
		$("#activated_featuresEdit").val(row.eq(5).text());
		$("#UE_TYPEEdit").val(row.eq(6).text());
		$("#CELL_SETUPEdit").val(row.eq(7).text());
		$("#no_of_active_cellsEdit").val(row.eq(8).text());
		$("#numOfLCGEdit").val(row.eq(9).text());
		$("#UE_NUMEdit").val(row.eq(10).text());
		$("#user_typeEdit").val(row.eq(11).text());
		$("#fdeEdit").val(row.eq(12).text());
		$("#ePICEdit").val(row.eq(13).text());
		$("#nbicEdit").val(row.eq(14).text());
		$("#ca_mc_dcEdit").val(row.eq(15).text());
		$("#handoverEdit").val(row.eq(17).text());
		$("#recoveryEdit").val(row.eq(18).text());
		$("#handoverEdit").val(row.eq(19).text());
		$("#QCEdit").val(row.eq(20).text());
		$("#CIEdit").val(row.eq(21).text());
		$("#commentEdit").val(row.eq(22).text());
	});

	var deleteID = null;
	var currentID = null;
	$(".deleteButton").click(function () {
		deleteID = $(this).attr("value");
		$("#idDelValue").attr("value", deleteID);
	});
 
	var inputs = document.querySelectorAll('.inputfile');
	Array.prototype.forEach.call(inputs, function (input) {
		var label = input.nextElementSibling,
			labelVal = label.innerHTML;

		input.addEventListener('change', function (e) {
			var fileName = '';
			if (this.files && this.files.length > 1)
				fileName = (this.getAttribute('data-multiple-caption') || '').replace('{count}', this.files.length);
			else
				fileName = e.target.value.split('\\').pop();

			if (fileName)
				label.querySelector('span').innerHTML = fileName;
			else
				label.innerHTML = labelVal;
		});
	});

	$("#importForm").submit(function(e){
		var option = 0;
		if (confirm("Do you want to delete the exisiting database? \n             OK(yes) \n             Cancel(no) \n	 NOTE: To cancel, refresh the page.")){
			option = 1
		}
		else{
			option = 0
		}
		$('<input />').attr('type', 'hidden')
			.attr('name', "option")
			.attr('value', option)
			.appendTo('#importForm');
		return true;
	});
})(jQuery); 
