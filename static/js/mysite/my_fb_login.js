
$(function(){

	// // Get csrf token cookie
	// function getCookie(name) {
	// 	var cookieValue = null;
	// 	if (document.cookie && document.cookie != '') {
	// 		var cookies = document.cookie.split(';');
	// 		for (var i = 0; i < cookies.length; i++) {
	// 			var cookie = $.trim(cookies[i]);
	// 			// Does this cookie string begin with the name we want?
	// 			if (cookie.substring(0, name.length + 1) == (name + '=')) {
	// 				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	// 				break;
	// 			}
	// 		}
	// 	}
	// 	return cookieValue;
	// }
	// var csrftoken = getCookie('csrftoken');
	// var ASYNC_URL = '/async/';


	// This is called with the results from from FB.getLoginStatus().
	function statusChangeCallback(response) {
		console.log('statusChangeCallback');
		console.log(response);
		// The response object is returned with a status field that lets the
		// app know the current login status of the person.
		// Full docs on the response object can be found in the documentation
		// for FB.getLoginStatus().
		if (response.status === 'connected') {
			ajaxCall( ASYNC_URL, "fb_data", "POST", response );
			// Logged into your app and Facebook.
			/* testAPI(); */
		} else if (response.status === 'not_authorized') {
			// The person is logged into Facebook, but not your app.
			document.getElementById('status').innerHTML = 'Please log ' + 'into this app.';
		} else {
			// The person is not logged into Facebook, so we're not sure if
			// they are logged into this app or not.
			/* document.getElementById('status').innerHTML = 'Please log ' + 'into Facebook.'; */
			checkLoginState();
		}
	}


	// This function is called when someone finishes with the Login
	// Button.  See the onlogin handler attached to it in the sample
	// code below.
	function checkLoginState() {
		FB.getLoginStatus(function(response) {
			// sending access_token comes here
			statusChangeCallback(response);
		}, { scope:"public_profile,email"} );
	}

	window.fbAsyncInit = function() {
		FB.init({
			appId      : '486040541424813',
			cookie     : true,  // enable cookies to allow the server to access 
								// the session
			xfbml      : true,  // parse social plugins on this page
			version    : 'v2.0' // use version 2.0
		});

		// Now that we've initialized the JavaScript SDK, we call 
		// FB.getLoginStatus().  This function gets the state of the
		// person visiting this page and can return one of three states to
		// the callback you provide.  They can be:
		//
		// 1. Logged into your app ('connected')
		// 2. Logged into Facebook, but not your app ('not_authorized')
		// 3. Not logged into Facebook and can't tell if they are logged into
		//    your app or not.
		//
		// These three cases are handled in the callback function.
		
		/*
		FB.getLoginStatus(function(response) {
			statusChangeCallback(response);
		});
		*/
		// auto login as soon as landing on Login page
		// checkLoginState();
		
	};

	// Here we run a very simple test of the Graph API after login is
	// successful.  See statusChangeCallback() for when this call is made.
	function testAPI() {
		console.log('Welcome!  Fetching your information.... ');
		FB.api('/me', function(response) {
			console.log('Successful login for: ' + response.name);
			document.getElementById('status').innerHTML = 'Thanks for logging in, ' + response.name + '!';
			
			ajaxCall( ASYNC_URL, "fb_data", "POST", response, successCallBack, errorCallBack );
		});
		
	}

	function successCallBack(data){
		console.log("Success");
		console.log(data);
	}

	function errorCallBack(data){
		console.log("Error");
		console.log(data);	
	}

	// function ajaxCall(ASYNC_URL, func_to_run, method, response, successCallBack, errorCallBack ){
	// 	$.ajax({
	// 		url: ASYNC_URL,
	// 		data: { func_to_run: func_to_run, fb_response: response,  },
	// 		type: method,
	// 		async: true,
			
	// 		beforeSend: function( xhr) {
	// 			xhr.setRequestHeader("X-CSRFToken", csrftoken);
	// 		},
			
	// 		error: errorCallBack,
	// 		success: successCallBack,

	// 	});
	// }

});

// Load the SDK asynchronously
(function(d, s, id) {
	var js, fjs = d.getElementsByTagName(s)[0];
	if (d.getElementById(id)) return;
	js = d.createElement(s); js.id = id;
	js.src = "//connect.facebook.net/en_US/sdk.js";
	fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

