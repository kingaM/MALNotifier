<?php
require_once('database.php');

function updateSettings($score, $mal) {
    $db = new DatabaseHelper();
    $db->execute("UPDATE
        users SET score = :score WHERE mal = :mal ;",
        array(':score' => $score, ':mal' => $mal));
}

require_once('libs/FirePHPCore/FirePHP.class.php');            
$firephp = FirePHP::getInstance(true);
$firephp->log($_POST);
updateSettings($_POST['score'], $_SERVER["QUERY_STRING"]);

echo '{"valid" : 1}';

?>