(function(){
'use strict';

angular.module('WebPageApp')
.controller('leetcodeController', leetcodeController);

leetcodeController.$inject = ['dataService', 'leetcodeInfo'];
function leetcodeController(dataService, leetcodeInfo) {
	var ctrl = this;

	ctrl.stat = leetcodeInfo.stat;
	ctrl.category2infoList = leetcodeInfo.category2infoList;
	for(var category in ctrl.category2infoList){
		var infoList = ctrl.category2infoList[category];
		for(var idx in infoList){
			var info = infoList[idx];
			if(!("version" in info)){
				info['version'] = ['solution'];
			}
			if(!("tags" in info)){
				info['tags'] = [];
			}
		}
	}
	console.log(ctrl.category2infoList);
}

})();