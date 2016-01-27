<?php
function get_php($rand) {
    $jumpTypeArr = Array();
    $jumpTypeArr[0] = 1;
    $jumpTypeArr[5] = 8;
    $jumpTypeArr[6] = 8;
    $jumpTypeSum = array_sum($jumpTypeArr);
    $randValueSum = 0;

    foreach ($jumpTypeArr as $jumpType => $randValue) {
        $randValueSum += ceil($randValue / $jumpTypeSum * 100);
        if ($rand < $randValueSum) {
            break;
        }
    }
    return $jumpType;
}
for($i=0; $i<=100; $i++){
    echo "$i\t" . get_php($i) . "\n";
}
