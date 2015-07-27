angular.module('messageboard.controllers', ['messageboard.services', 'messageboard.directives'])

.controller('messageCtrl', function($scope, $interval, msgclient) {

    //TODO: encode the file to base64 and add it the POST request

    $scope.delete = msgclient.delete;
    $scope.save = msgclient.save;

    var get_data = function(){
            msgclient.refresh_data().success(function(data){
                $scope.messages = data;
            });
    }
    $interval(get_data,1000);

});
