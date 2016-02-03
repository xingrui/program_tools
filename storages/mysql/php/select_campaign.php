<?php
require_once 'Medoo-master/medoo.php';
$db_config = array(
    'database_type' => 'mysql',
    'database_name' => 'mob_adn',
    'server'        => 'adn-mysql-external.mobvista.com',
    'port'      =>3306,
    'charset'   => 'utf8',
    'username'  => 'mob_adn_ro',
    'password'  => 'blueriver123',
);
$db_ins = new \medoo($db_config);
$conds = array();
// WRONG USAGE : $conds['status'] = 1;
// status = 1 will have no effect after following conds.
$conds['AND']['direct_trace_app_id[!]'] = '';
$conds['AND']['platform'] = 1;
// $conds['AND']['status'] = 1;
// $conds['AND']['id'] = 4620446;
$conds['ORDER'] = array(
'id DESC',
);
$rz = $db_ins->select('campaign_list', '*', $conds);
var_dump($rz);
