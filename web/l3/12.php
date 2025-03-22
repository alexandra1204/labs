<?php
$numbers = [2, 4, 6, 8];
$average = array_sum($numbers) / count($numbers);
echo "Среднее: $average\n"; 

$sum = (1 + 100) * 100 / 2;
echo "Сумма 1-100: $sum\n"; 

$original = [4, 9, 16];
$sqrtArray = array_map('sqrt', $original);
print_r($sqrtArray); 

$letters = range('a', 'z');
$values = range(1, 26);
$alphabet = array_combine($letters, $values);
print_r($alphabet); 

$str = '1234567890';
$pairs = str_split($str, 2);
$sumPairs = array_sum(array_map('intval', $pairs));
echo "Сумма пар: $sumPairs\n"; 
