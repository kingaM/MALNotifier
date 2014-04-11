<?php

//TODO: Implement this properly in PHP

$output = shell_exec('python ../backend/mal.py ' . $_SERVER["QUERY_STRING"] . ' 2>&1');
echo $output;

?>