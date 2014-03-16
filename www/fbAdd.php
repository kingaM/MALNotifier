<?php

require_once('database.php');

$db = new DatabaseHelper();
$db->execute("UPDATE users SET facebook=:id WHERE mal=:mal",
    array(':id' => $_POST['fbId'], ':mal' => $_POST['mal']));

?>