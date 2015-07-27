angular.module('messageboard.services', [])

.provider('msgclient', function() {
    var urlBase = '/messages';

    this.setBaseUrl = function (url) {
      console.log(url);
      urlBase = url;
    }

    this.$get = function($http) {
      return new MsgClient($http);
    };

    function MsgClient($http){
        this.refresh_data = function(){
            return $http.get(urlBase + '/all');
        }
        this.delete = function(id){
            return $http.delete(urlBase + '/' + id);
        }

        this.save = function(msg){
            $http.post(urlBase + "/", {message:msg}).
                success(function(data, status, headers, config) {
                    console.log("Message sent!");
                  }).
                error(function(data, status, headers, config) {
                    console.log("Error on sending message!");
            });
        }
    }
});