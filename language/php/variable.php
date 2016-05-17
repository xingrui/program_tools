<?php
class mapping {
    function test(){
        $this->abcd="123";
        var_dump("mapping_{$this->abcd}");
    }
}
$obj = new mapping();
$obj->test();
