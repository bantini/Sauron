const process_request = function(request_body){
  console.log(request_body);
}

const process_response = function(response_body){
  console.log(response_body);
}

exports.process_request = process_request;
exports.process_response = process_response;
