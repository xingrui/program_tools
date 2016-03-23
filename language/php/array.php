<?php
$superCountryCode = array("US","SG","IE","DE","JP","AU","BR","ID","IN");
var_dump(in_array("IN", $superCountryCode));
var_dump(in_array("CN", $superCountryCode));
$s = array();
foreach($superCountryCode as $countryCode){
    $s[$countryCode] = 0;
}
for($i=0;$i<10;$i++){
    var_dump(array_rand($s));
}

$one=array('1'=>'123', '2'=>'456');
$two=array('1'=>'123', '3'=>'456');
var_dump($one + $two);
