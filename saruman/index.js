// var memwatch = require('memwatch-next');
var heapdump = require('heapdump');
/*
const get_first_snapshot = function(){
  var hd = new memwatch.HeapDiff();
  return hd;
}

const get_snapshot_diff = function(heap_diff){
  var diff = heap_diff.end();
  return diff;
}
*/
const heap_dump = function(file_path){
  var file_name = file_path || '/Users/nilayan/Documents/Sauron/heap_dump_'+Date.now()+'.heapsnapshot'
  heapdump.writeSnapshot(file_name, function(err, filename) {
    console.log('dump written to', file_name);
  });
}

// exports.get_first_snapshot = get_first_snapshot;
// exports.get_snapshot_diff = get_snapshot_diff;
exports.heap_dump = heap_dump;
