<?php

require_once('database.php');

function addUser($email, $mal, $xml, $facebook = null) {
    $allowedExts = array("xml");
    $temp = explode(".", $xml["name"]);
    $extension = end($temp);
    if (($xml["type"] == "text/xml") && in_array($extension, $allowedExts)) {
        if ($xml["error"] > 0) {
            echo "Return Code: " . $xml["error"] . "<br>";
        }
        else {
            if (file_exists("../backend/" . $mal . ".xml")) {
                echo $mal . " already exists. ";
            }
            else {
                move_uploaded_file($xml["tmp_name"], "../backend/" . $mal . ".xml");
                echo "Stored in: " . "../backend/" . $mal;
            }
        }
    } else {
        echo "Invalid file";
    }

    $db = new DatabaseHelper();
    $db->execute("INSERT INTO 
        users(email, mal, facebook)
        VALUES (:email, :mal, :facebook);",
        array(':email' => $email, ':mal' => $mal, ':facebook' => $facebook));
}

require_once('libs/FirePHPCore/FirePHP.class.php');            
$firephp = FirePHP::getInstance(true);
$firephp->log($_POST);
addUser($_POST['email'], $_POST['mal'], $_FILES[0]);

?>
