<?php

require_once('database.php');

function error() {
    http_response_code(400);
    die();
}

function addUser($email, $mal, $ova = 0, $unaired = 1, $minRating = 10, $facebook = null) {

    if($minRating < 0 || $minRating > 10)
        error();
    if($unaired !== 0 && $unaired !== 1)
        error();
    if($ova !== 0 && $ova !== 1)
        error();

    //TODO: Make (mal, email) unique instead of mal and then overwrite settings accordingly

    $db = new DatabaseHelper();
    $db->execute("INSERT INTO 
        users(email, mal, facebook, ova, unaired, minRating)
        VALUES (:email, :mal, :facebook, :ova, :unaired, :minRating);",
        array(':email' => $email, ':mal' => $mal, ':facebook' => $facebook, ':ova' => $ova, ':unaired' => $unaired, ':minRating' => $minRating));

    echo "Registered";
}

addUser($_POST['email'], $_POST['mal'], (int) $_POST['ova'], (int) $_POST['unaired'], (int) $_POST['minRating']);

?>
