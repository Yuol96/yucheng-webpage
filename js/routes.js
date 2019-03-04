(function(){
'use strict';

angular.module('WebPageApp')
.config(RoutesConfig);

RoutesConfig.$inject = ['$stateProvider', '$urlRouterProvider'];
function RoutesConfig($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/');

	$stateProvider
	.state('home', {
		url: '/',
		templateUrl: 'templates/home.view.html'
	})
	.state('cvView', {
		url: '/cv',
		templateUrl: 'templates/cv.view.html',
		// contorller: 'cvController as cvController'
	})
	.state('experienceView', {
		url: '/experience',
		templateUrl: 'templates/experience.view.html',
		contorller: 'experienceController as experienceController'
	})
	.state('publicationView', {
		url: '/publication',
		templateUrl: 'templates/publication.view.html'
	})
	.state('courseView', {
		url: '/courses',
		templateUrl: 'templates/courses.view.html',
		controller: 'courseController as courseController',
		resolve: {
			courseraInfo: ['dataService', function(dataService){
				return dataService.getCourseraInfo();
			}]
		}
	})
	.state('leetcodeView', {
		url: '/leetcode',
		templateUrl: 'https://yuol96.github.io/MyNotes/leetcode/notes.html'
		// controller: 'leetcodeController as leetcodeController',
		// resolve: {
		// 	leetcodeInfo: ['dataService', function(dataService){
		// 		return dataService.getLeetcodeInfo();
		// 	}]
		// }
	})
	;
}

})();