// jQuery Needed
// Works on top of jQuery

(function($){

	var ASYNC_URL = '/async/';

	// Expand Search bar
	nav_search = $("#nav-search");
	nav_search
	.focus( function(e){ nav_search.animate( {width: "100%"}, 750 ); })
	.blur( function(e) { nav_search.animate( {width: "50%"}, 750 ); })
	;
	// Expand Search bar-
	
	// Show and Hide Login and Registeration Forms
	var form_login_registeration = $("#form-login-registeration");
	var form_login_registeration_links = $("#form-login-registeration-links");
	form_login_registeration_links.children("a").click(function(ev){
		var hide = $(ev.target).data("hide");
		var show = $(ev.target).data("show");
		
		form_login_registeration.children("div#"+hide).hide(700);
		form_login_registeration.children("div#"+show).show(700);
	});
	// Show and Hide Login and Registeration Forms-

	// Tooltip
	options = {placement: "left"};
	js_show_tooltip = $(".j-ttip");
	js_show_tooltip.tooltip();
	// Tooltip-


	// function successCallBack(){
	// 	console.log("scCB");
	// }

	function errorCallBack(){
		console.log("errCB");
	}

	function showFwersList(data){
		console.log("data");
		console.log(data);
	}

	// Followers List modal
	$('#fwersList').on('shown.bs.modal', function (e) {
		// do something…
		console.log("e");
		console.log(e);
		console.log("ASYNC_URL");
		console.log(ASYNC_URL);
		ajaxCall( ASYNC_URL, "fwers_list", "GET", '', showFwersList, errorCallBack );
	});
	// Followers List modal-

})(jQuery);

