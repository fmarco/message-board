var app = angular.module('messageboard', []);

app.controller('messageCtrl', function($scope, $http, $interval) {

    var urlBase = '/messages';
    var refresh_data = function(){
        $http.get(urlBase + '/all')
        .success(function(data){
            $scope.messages = data;
        });
    }
    
    $interval(refresh_data,1000);
});
