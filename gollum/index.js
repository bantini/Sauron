const onFinished = require('on-finished');
const response_handler = require('./handlers/response_handler');
const request_handler = require('./handlers/request_handler');
const error_handler = require('./handlers/error_handler');

const check_response_time = function(req, res, next) {
  t1 = process.hrtime();
  request_handler.handle_request(req, t1);
  onFinished(res, function(err, res) {
    if(err){
      error_handler.handle_error(err);
    } else {
      try{
        var response_time = process.hrtime(t1);
        var formatted_time = (response_time[0]*1000000000 + response_time[1])/1000000;
        console.log("The repsonse time taken was: " + formatted_time + "ms");
        response_handler.handle_response(res, formatted_time);
      } catch(err){
        error_handler.handle_error(err);
      }
    }
  });
  next();
}

const check_server_status = function(url){
  var http = require('http');
  http.get('url', function (res) {
    // If you get here, you have a response.
    // If you want, you can check the status code here to verify that it's `200` or some other `2xx`.

  }).on('error', function(e) {
    error_handler.handle_error(e);
  });;
}

const err_unknown_route = function(app, message) {
  var error_message = message || "API is not present";
  app.get('*', check_response_time, function(req, res){
    var temp = new Error(error_message);
    throw temp;
  });
}

const err_internal_server = function(app, api_missing_message){
  var error_message = api_missing_message || 'API is not present';
  app.use(function(err, req, res, next) {
    if(err.message == error_message){
      res.status(404).json({ message: JSON.stringify(err.stack) });
    } else {
      res.status(500).json({ message: JSON.stringify(err.stack) });
    }
  });
}

exports.check_response_time = check_response_time;
exports.err_unknown_route = err_unknown_route;
exports.err_internal_server = err_internal_server;
