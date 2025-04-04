<?php
$str = 'a1b2c3';

$result = preg_replace_callback(
    '/\d+/', 
    function ($matches) {
        $number = (int)$matches[0];
        return (string)($number * $number);
    },
    $str
);

echo $result;