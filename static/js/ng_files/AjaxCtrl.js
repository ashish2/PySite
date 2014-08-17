// AngularJs Needed
// Works on top of AngularJs

app.controller("AjaxCtrl", function($scope, $http){
	$scope.data = {};

	$scope.runAjax = function(){

		data = {};
		// var responsePromise = $http.post();
		var responsePromise = $http.get('/read/23/', data);

		responsePromise.success( function(data, status, headers, config){
			$scope.data = data;
			console.log("data");
			console.log(data);
		});
		
		responsePromise.error( function(data, status, headers, config){
			// show error in the <div>
			error_div = $(".error");
			error_div.append("Some error while making request, please try again later.");
		});
		
	};


});


