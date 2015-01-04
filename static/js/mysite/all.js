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


	// Delete the PTS id
	function ptsD(data){
		data = JSON.parse(data);
		div = $('*[data-pts-id="'+data['pk']+'"]');
		div.parents(".each-posts").fadeOut(300);
	}

	$('.j-del-pts').on('click', function (e) {
		// do something…
		// ajaxCall( ASYNC_URL, "fwers_list", "GET", '', showFwersList, errorCallBack );
		$(e.target).removeClass("glyphicon-remove-circle").addClass("fa fa-spinner fa-spin");

		resp = {"pts_id": $(e.target).data("pts-id") };
		ajaxCall( ASYNC_URL, "ptsD", "GET", resp, ptsD, errorCallBack );

	});	
	// Delete the PTS id-


	//======== Hide & Show js ====================
	
	// Delete post js
	some_user_funcs = $(".disp_none_show_on_parent_hover");
	some_user_funcs_each_posts = some_user_funcs.parents(".each-posts");
	some_user_funcs_each_posts.mouseenter( function(e){ 
		$(e.currentTarget).find(some_user_funcs).fadeIn(500);
	}).mouseleave(function(e){
		$(e.currentTarget).find(some_user_funcs).fadeOut(800);
	});
	// Delete post js-
	

	//======== Hide & Show js- ====================

	//======== Shrink ====================
	$(window).scroll( function () {
		if( $(document).scrollTop() > 100 ){
			$("nav").removeClass("main-nav");
		} else {
			$("nav").addClass("main-nav");
		}

	});


	//======== Shrink- ====================


})(jQuery);


/*

some_user_funcs_each_posts.mouseenter( function(e){ 
 	// div = $(e.target);
 	div = $(e.currentTarget);
 	console.log("div");
 	console.log(div);
 	th = $(this);
 	console.log("th");
 	console.log(th);
 	div_ss = div.find(some_user_funcs);
 	console.log("div ss");
 	console.log(div_ss);
 	th_ss = th.find(some_user_funcs);
 	console.log("th ss");
 	console.log(th_ss);
})
	 */
