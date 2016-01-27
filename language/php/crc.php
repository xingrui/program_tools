<?php
$fp = fopen("php://stdin", "r");
while($input=fgets($fp, 10000000)) {
    $items = explode(' ', $input);
    echo crc32($items[0]) . " | " . $items[1] . " | " . $items[2];
}
