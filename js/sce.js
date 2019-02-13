(function(){

angular.module('WebPageApp').config(function($sceDelegateProvider) {
 $sceDelegateProvider.resourceUrlWhitelist([
   // Allow same origin resource loads.
   'self',
   // Allow loading from our assets domain.  Notice the difference between * and **.
   'https://yuol96.github.io/**']); //srv*.assets.example.com/**
 });

})();