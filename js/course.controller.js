(function(){
'use strict';

angular.module('WebPageApp')
.controller('courseController', courseController);

courseController.$inject = ['dataService', 'courseraInfo'];
function courseController(dataService, courseraInfo) {
	var ctrl = this;

	ctrl.courseraInfo = courseraInfo;
	console.log(ctrl.courseraInfo);
}

})();