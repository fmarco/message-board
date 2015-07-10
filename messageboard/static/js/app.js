var app = angular.module('messageboard', []);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);


app.controller('messageCtrl', function($scope, $http, $interval) {


    var urlBase = '/messages';

    var refresh_data = function(){
        $http.get(urlBase + '/all')
        .success(function(data){
            $scope.messages = data;
        });
    }
    
    $interval(refresh_data,1000);


    $scope.delete = function(id){
        $http.delete(urlBase + '/' + id)
        .success(function(data){
            console.log('ok');
        });
    }

    $scope.save = function(){
        $http.post(urlBase + "/", {message:$scope.message}).
            success(function(data, status, headers, config) {
                console.log("Message sent!");
              }).
            error(function(data, status, headers, config) {
                console.log("Error on sending message!");
        });
    }
});
