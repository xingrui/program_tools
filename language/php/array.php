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
