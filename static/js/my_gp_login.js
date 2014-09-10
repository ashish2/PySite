
// $(function(){

	/*
	// function signinCallback(authResult) {
	function signInCallback(authResult) {

		if (authResult['access_token']) {
			// Successfully authorized
			document.getElementById('signinButton').setAttribute('style', 'display: none');
		} else if (authResult['error']) {
		// There was an error.
		// Possible error codes:
		//   "access_denied" - User denied access to your app
		//   "immediate_failed" - Could not automatially log in the user
		// console.log('There was an error: ' + authResult['error']);
		}
	}
	*/

	// Get csrf token cookie
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = $.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');
	var ASYNC_URL = '/async/';

	function signInCallback(authResult) {
		console.log("authResult");
		console.log(authResult);
		
		if (authResult['code']) {

			// Hide the sign-in button now that the user is authorized, for example:
			$('#signinButton').attr('style', 'display: none');

			/*
			// Send the code to the server
			$.ajax({
				type: 'POST',
				url: ASYNC_URL,
				contentType: 'application/octet-stream; charset=utf-8',

				beforeSend: function( xhr) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				},

				success: function(result) {
					// Handle or verify the server response if necessary.

					// Prints the list of people that the user has allowed the app to know
					// to the console.
					console.log("result");
					console.log(result);
					if (result['profile'] && result['people']){
						$('#results').html('Hello ' + result['profile']['displayName'] + '. You successfully made a server side call to people.get and people.list');
					} else {
						$('#results').html('Failed to make a server-side call. Check your configuration and console.');
					}

				},

				processData: false,
				data: authResult['code']
			});
			*/
			
			ajaxCall( ASYNC_URL, "gp_data", "POST", authResult );

		} else if (authResult['error']) {
			// There was an error.
			// Possible error codes:
			//   "access_denied" - User denied access to your app
			//   "immediate_failed" - Could not automatially log in the user
			console.log('There was an error: ' + authResult['error']);
		}
	}

	function disconnectUser(access_token) {
		var revokeUrl = 'https://accounts.google.com/o/oauth2/revoke?token=' + access_token;

		// Perform an asynchronous GET request.
		$.ajax({
			type: 'GET',
			url: revokeUrl,
			async: false,
			contentType: "application/json",
			dataType: 'jsonp',
			success: function(nullResponse) {
				// Do something now that user is disconnected
				// The response is always undefined.
			},
			error: function(e) {
				// Handle the error
				// console.log(e);
				// You could point users to manually disconnect if unsuccessful
				// https://plus.google.com/apps
			}
		});
	}
	// Could trigger the disconnect on a button click
	$('#revokeButton').click(disconnectUser);


	// client.plus.* will start existing here.
	// gapi.client.load('plus','v1', function(){ 
		// once we get this call back, gapi.client.plus.* will exist
	// });

	function profile(){
		var user = gapi.client.plus.people.get( {'userId' : 'me'} );
		user.execute(function(profile) {
			$('#profile').append(
				$('<p><img src=\"' + profile.image.url + '\"></p>') 
			);
			$('#profile').append(
					$('<p>Hello ' + profile.displayName + '</p>')
			);
		});
	};

	function people() {
		var request = gapi.client.plus.people.list({
			'userId': 'me',
			'collection': 'visible'
		});
		request.execute(function(people) {
			for (var personIndex in people.items) {
				person = people.items[personIndex];
				$('#visiblePeople').append('<img src="'+person.image.url + '">');
			}
		});
	};
	
// });


// G+ Response
// _aa: "0"
// access_token: "ya29.ewDBRIL5-gfAIwGzsk_VkknY9XXzMCA0jIRXIbYE26RQkEEBFjLAqRTe"
// authuser: "0"
// client_id: "874514271696-28jvsre44909p210nul82r5imhrk3i7f.apps.googleusercontent.com"
// code: "4/Zl0eXAG1UGlCpEWRelo-GosDj2Di.kiSX65Kvvl4Wcp7tdiljKKbPDpi3kAI"
// cookie_policy: "single_host_origin"
// expires_at: "1410292411"
// expires_in: "3600"
// g_user_cookie_policy: "single_host_origin"
// id_token: "eyJhbGciOiJSUzI1NiIsImtpZCI6IjNmOTJjMGQ0ZWZkOTJjMWJhYWY5OTBjZGYyNTMxMDI5ZTg3NWNkMDMifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwic3ViIjoiMTE1MjU0NjQ2MTcyMjc5MTMyMzgzIiwiYXpwIjoiODc0NTE0MjcxNjk2LTI4anZzcmU0NDkwOXAyMTBudWw4MnI1aW1ocmszaTdmLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXRfaGFzaCI6InNwR1g4TGdBeTFmNi03R0FpTmgyRnciLCJhdWQiOiI4NzQ1MTQyNzE2OTYtMjhqdnNyZTQ0OTA5cDIxMG51bDgycjVpbWhyazNpN2YuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJjX2hhc2giOiJxa0k5X3lrZXpUQjI2aDdQS21VVG1nIiwiaWF0IjoxNDEwMjg4OTUwLCJleHAiOjE0MTAyOTI4NTB9.tfohPQsC6GKOr6h79HRqph2jAgmIZxVerzFbsBwmfFPRa_Regc030oTPs59iC5Z7HzbWjfy1K4SW9glvE6b7Gl2nyYIabMlEi7z-q_HYJYnYhWtxOlo_xtUbO9_7C5lAMJYlk83vwuEhOO1eD3MCd-lmDSACvS188-q3VX8rmMs"
// issued_at: "1410288811"
// num_sessions: "1"
// prompt: "none"
// response_type: "code token id_token gsession"
// scope: "https://www.googleapis.com/auth/plus.login https://www.googleapis.com/auth/plus.moments.write https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/plus.profile.agerange.read https://www.googleapis.com/auth/plus.profile.language.read https://www.googleapis.com/auth/plus.circles.members.read"
// session_state: "7fcf1801facffdf60d0c6245f8b47552eb2685ee..a994"
// state: ""
// status: Object
// token_type: "Bearer"

