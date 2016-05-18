var array=[];
for(var i =0; i < 2000; i++) {
    array.push("array" + i);
}

var test_ref = function(options) {
    options.ref = '123456';
}

//console.log(array);
var options = {};
test_ref(options);
console.log(options);
console.log(array.indexOf("array1000"));
//console.log("array0" in array);
