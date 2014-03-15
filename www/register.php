<?php

 require_once('database.php');

function addUser($email, $mal, $facebook = null) {
    $db = new DatabaseHelper();
    $db->execute("INSERT INTO 
        users(email, mal, facebook)
        VALUES (:email, :mal, :facebook);",
        array(':email' => $email, ':mal' => $mal, ':facebook' => $facebook));
}

require_once('libs/FirePHPCore/FirePHP.class.php');            
$firephp = FirePHP::getInstance(true);
$firephp->log($_POST);
addUser($_POST['email'], $_POST['mal']);
    
?>