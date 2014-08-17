// AngularJs Needed
// Works on top of AngularJs

app.controller("MyCtrl", function($scope) {
	$scope.message = "";
	$scope.left  = function() { return 100 - $scope.message.length; };
	$scope.clear = function() { $scope.message = ""; };
	$scope.save  = function() { $scope.message = ""; };


	// $scope.person = [ { firstname: "A", lastname: "O" }, { firstname: "V", lastname: "Oj" } ];
	$scope.person = { firstname: "A", lastname: "O" };
	$scope.changeName = function(){
		$scope.person = { firstname: "Ash", lastname: "Ojha" };
	}

});


app.controller("MainController", function($scope){
	$scope.selectedPerson = 0;
	$scope.selectedGenre = null;
	$scope.people = [
		{
			id: 0,
			name: 'Leon',
			music: [
				'Rock',
				'Metal',
				'Dubstep',
				'Electro'
			]
		},
		{
			id: 1,
			name: 'Chris',
			music: [
				'Indie',
				'Drumstep',
				'Dubstep',
				'Electro'
			]
		},
		{
			id: 2,
			name: 'Harry',
			music: [
				'Rock',
				'Metal',
				'Thrash Metal',
				'Heavy Metal'
			]
		},
		{
			id: 3,
			name: 'Allyce',
			music: [
				'Pop',
				'RnB',
				'Hip Hop'
			]
		}
	];
});


