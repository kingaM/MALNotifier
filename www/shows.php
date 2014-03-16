<?php

require_once('libs/FirePHPCore/FirePHP.class.php');            
$firephp = FirePHP::getInstance(true);
$firephp->log($_SERVER["QUERY_STRING"]);
$output = shell_exec('python ../backend/mal.py ' . $_SERVER["QUERY_STRING"] . ' 2>&1');
$firephp->log($output);
echo $output;

?>