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


	function successCallBack(){
		console.log("scCB");
	}

	function errorCallBack(){
		console.log("errCB");
	}





	// Followers List modal
	function showFwersList(data){
		fwersList = JSON.parse(data);
		str = '<div class="json-data"><table class="table table-hover"><tbody>';
		s = '';
		$.each(fwersList, function(k, v){
			ava = v.userprofile__avatar;
			if (!ava)
				ava = '/uploads/avatar/random.jpg';
			ahref_img = '<a href="/users/'+v.pk+'/"><img class="img-responsive header-user-img" src="'+ava+'"></a>&nbsp;'+v.email;
			s += '<tr><td>'+ahref_img+'</td></tr>';
		});

		str += s;
		str += '</tbody></table></div>';

		fwersList_div = $("#fwersList").find(".modal-body");
		fwersList_div_jsonData = fwersList_div.find(".json-data");
		if(!fwersList_div_jsonData.length) 
			fwersList_div.empty().append(str);
	}

	$('#fwersList').on('shown.bs.modal', function (e) {
		// do something…
		ajaxCall( ASYNC_URL, "fwers_list", "GET", '', showFwersList, errorCallBack );
	});

	// Followers List modal-


})(jQuery);

