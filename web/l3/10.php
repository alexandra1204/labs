<?php
function isSumOverTen($a, $b) {
    return ($a + $b) > 10;
}
echo isSumOverTen(6, 5) ? "true\n" : "false\n"; 

function areEqual($a, $b) {
    return $a == $b;
}
echo areEqual(4, 4) ? "true\n" : "false\n"; 

$test = 0;
if ($test == 0) echo "верно\n";

$age = 25;
if ($age < 10 || $age > 99) {
    echo "Число вне диапазона 10-99\n";
} else {
    $sum = array_sum(str_split(strval($age)));
    echo ($sum <= 9) ? "Сумма цифр однозначна: $sum\n" : "Сумма цифр двузначна: $sum\n";
}

$arr = [1, 2, 3];
if (count($arr) === 3) {
    echo array_sum($arr) . "\n"; 
}
