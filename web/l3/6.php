<?php

$a = 10;
$b = 3;
$remainder = $a % $b;
echo "Остаток от деления $a на $b: $remainder\n"; 

if ($a % $b === 0) {
    echo "Делится. Результат: " . ($a / $b) . "\n";
} else {
    echo "Делится с остатком. Остаток: $remainder\n";
}


$st = pow(2, 10); 
echo "2^10: $st\n";

$sqrt245 = sqrt(245); 
echo "Корень из 245: $sqrt245\n";

$array = [4, 2, 5, 19, 13, 0, 10];
$sumSquares = 0;
foreach ($array as $num) {
    $sumSquares += $num ** 2;
}
echo "Корень суммы квадратов: " . sqrt($sumSquares) . "\n"; 

$sqrt379 = sqrt(379);
echo "Корень из 379:\n";
echo "Целые: " . round($sqrt379) . "\n"; 
echo "Десятые: " . round($sqrt379, 1) . "\n"; 
echo "Сотые: " . round($sqrt379, 2) . "\n"; 

$sqrt587 = sqrt(587);
$rounded = [
    'floor' => floor($sqrt587), 
    'ceil' => ceil($sqrt587) 
];
print_r($rounded);


$numbers = [4, -2, 5, 19, -130, 0, 10];
echo "Min: " . min($numbers) . ", Max: " . max($numbers) . "\n"; 


echo "Случайное число: " . rand(1, 100) . "\n";

$randomArray = [];
for ($i = 0; $i < 10; $i++) {
    $randomArray[] = rand();
}
print_r($randomArray);

$a = 15;
$b = 7;
echo "|a - b|: " . abs($a - $b) . "\n";


$original = [1, 2, -1, -2, 3, -3];
$positive = array_map('abs', $original);
print_r($positive);

$number = 15;
$divisors = [];
for ($i = 1; $i <= $number; $i++) {
    if ($number % $i === 0) {
        $divisors[] = $i;
    }
}
print_r($divisors);

$numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
$sum = 0;
$count = 0;
foreach ($numbers as $num) {
    $sum += $num;
    $count++;
    if ($sum > 10) {
        break;
    }
}
echo "Нужно сложить $count первых элементов \n"; 
