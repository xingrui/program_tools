var Q = require('q');
var mongodb = require('mongodb');
var mongodbConnection = function (config) {
    return Q.ninvoke(mongodb.MongoClient, 'connect', config.connect, config.options);
}

var config = require('./config.json').mongodb_newadn;
var runtime = {};
mongodbConnection(config).then(function(conn){
    runtime.conn = conn;
    return Q.ninvoke(conn.collection('unit'), 'findOne', {
        unitId:7
    });
}).then(function(data){
    console.log(JSON.stringify(data, null, 4));
    runtime.conn.close();
}).done();
