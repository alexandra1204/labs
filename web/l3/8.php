<?php

function increaseEnthusiasm($str) {
    return $str . "!";
}
echo increaseEnthusiasm("hello") . "\n";

function repeatThreeTimes($str) {
    return $str . $str . $str; 
}
echo repeatThreeTimes("PHP ") . "\n"; 

echo increaseEnthusiasm(repeatThreeTimes("php")) . "\n";

function cut($str, $length = 10) {
    return substr($str, 0, $length);
}

echo cut("43654654345653") . "\n";
echo cut("43654654345653", 5) . "\n";

function printArrayRecursive($arr) {
    if (empty($arr)) return;
    echo array_shift($arr) . " ";
    printArrayRecursive($arr);
}
printArrayRecursive([1, 2, 3, 4]); 
echo "\n";

function sumDigits($num) {
    $sum = array_sum(str_split(strval($num)));
    return ($sum > 9) ? sumDigits($sum) : $sum;
}
echo sumDigits(12345);
