const express = require('express');
const app = express();
const capture_status = require('./capture_status.js');
const onFinished = require('on-finished');
const gollum = require('./gollum');
const saruman = require('./saruman');
var timeout = require('connect-timeout');


app.get('/hello', gollum.check_response_time, function(req, res, next){
  res.send("Hello world");
});
/*
app.get('/hello', function(req, res, next){
    capture_status.process_response(res);
    //res.send("Hello");
    // next();
  // capture_status.process_request(req);
});
*/
app.get('/bye', gollum.check_response_time, function(req, res, next){
    res.send("Bye");
  // capture_status.process_request(req);
});

app.get('/wrong', gollum.check_response_time, function(req, res, next){
    res.send(wrong);
  // capture_status.process_request(req);
});

app.get('/loads', gollum.check_response_time, function(req, res, next){
  // var hd = saruman.get_first_snapshot();
  var temp_list = [];
  for(var i =0; i<= 1000; i++){
    temp_list.push(i);
  }
  // var diff = saruman.get_snapshot_diff(hd);
  // console.log(diff);
});

app.get('*', gollum.check_response_time, function(req, res){
  var temp = new Error(" Error handled by app");
  throw temp;
});

gollum.err_unknown_route(app);
gollum.err_internal_server(app);
// saruman.heap_dump();




//app.timeout = 10;
var server = app.listen(3000, () =>
console.log('Example app listening on port 3000!'))
server.timeout = 0;
