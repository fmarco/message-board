angular.module('messageboard', ['messageboard.controllers'])

.config(['$httpProvider', 'msgclientProvider', function($httpProvider, msgclientProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    msgclientProvider.setBaseUrl('/messages');
    }]);
