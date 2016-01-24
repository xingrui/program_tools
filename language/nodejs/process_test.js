var cluster = require("cluster");
// console.log(cluster);
process.on('exit', function () { process.nextTick(function () { console.log('This will not run'); }); console.log('About to exit.'); });
console.log(cluster);
cluster.fork();
