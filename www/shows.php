<?php

require_once('libs/FirePHPCore/FirePHP.class.php');            
$firephp = FirePHP::getInstance(true);
$firephp->log($_POST);
$output = shell_exec('python ../backend/mal.py 2>&1');
$firephp->log($output);
echo $output;

?>