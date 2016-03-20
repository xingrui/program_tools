// 当值是非空字符串和非零数字返回true，当值是空字符串、0、undefined或者null返回false。
var a = " "; console.log(!!a);   //true
var a = "s"; console.log(!!a);   //true
var a = true; console.log(!!a);   //true
var a = 1; console.log(!!a);   //true
var a = -1; console.log(!!a);   //true
var a = -2; console.log(!!a);   //true
 
var a = 0; console.log(!!a);   //false
var a = ""; console.log(!!a);   //false
var a = false; console.log(!!a);   //false
var a = null; console.log(!!a);   //false

var a = {a:'b'}; console.log(!!a);   //false
var a = undefined; console.log(!!a);   //false

