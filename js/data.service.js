(function(){
'use strict';

angular.module('data')
.service('dataService', dataService);

dataService.$inject = ['$http'];
function dataService($http) {
	var service = this;

	service.getLeetcodeInfo = function () {
		return $http({
			method: "GET",
			url: 'https://yuol96.github.io/leetcode-notes/infos.json'
		}).then(function(response){
			return response.data;
		});
	};
}

})();