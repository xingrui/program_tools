<?php
$pdo = new PDO("pgsql:host=adndataup.cj0ro5bbcusg.us-east-1.redshift.amazonaws.com;port=5439;dbname=data", "root", "adn2015DATA");
$current = time();
$startTime = floor($current / 3600 - 3 * 24) * 3600;
$current_threshold = 0;
$sql = "select campaign_id from (select campaign_id,count(*) as click_num from log_click where created >= '" . $startTime . "' group by campaign_id) as t1 where click_num >= " . $current_threshold;
$sql = "select sum(click_num) from (select campaign_id,count(*) as click_num from log_click where created >= '" . $startTime . "' group by campaign_id) as t1 where click_num >= " . $current_threshold;
$current_threshold = 500;
$sql = "select count(campaign_id) from (select campaign_id,count(*) as click_num from log_click where created >= '" . $startTime . "' group by campaign_id) as t1 where click_num >= " . $current_threshold;
$prepare = $pdo->prepare($sql);
$prepare->execute();
$rz = $prepare->fetchAll(PDO::FETCH_ASSOC);
var_dump($rz);

$current_threshold = 400;
$sql = "select count(campaign_id) from (select campaign_id,count(*) as click_num from log_click where created >= '" . $startTime . "' group by campaign_id) as t1 where click_num >= " . $current_threshold;
$prepare = $pdo->prepare($sql);
$prepare->execute();
$rz = $prepare->fetchAll(PDO::FETCH_ASSOC);
var_dump($rz);

$current_threshold = 0;
$sql = "select count(campaign_id) from (select campaign_id,count(*) as click_num from log_click where created >= '" . $startTime . "' group by campaign_id) as t1 where click_num >= " . $current_threshold;
$prepare = $pdo->prepare($sql);
$prepare->execute();
$rz = $prepare->fetchAll(PDO::FETCH_ASSOC);
var_dump($rz);
echo $sql;
?>
