<?php
 if ($_POST['process'] == "every") {
   $price =  $_POST['price'];
   $a = [];
    for ($i = 0; $i < 1000; $i++) {
        $a[] = rand(0, rand(0, 10000));
    }
    if ($a[array_rand($a)] % 2) {
        echo strval(round(intval($price) - (rand(1, 35) / 100) * intval($price), 0)). substr(strval(round(intval($price) - (rand(1, 35) / 100) * intval($price), 0)), 0, -2);
    } else {
        echo strval(round(intval($price) + (rand(1, 35) / 100) * intval($price), 0)). substr(strval(round(intval($price) + (rand(1, 35) / 100) * intval($price), 0)), 0, -2);
    }
 }
?>
