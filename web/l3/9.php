<?php

$arrX = [];
for ($i = 1; $i <= 5; $i++) { 
    $arrX[] = str_repeat('x', $i);
}
print_r($arrX); 

function arrayFill($value, $count) {
    return array_fill(0, $count, $value);
}
print_r(arrayFill('x', 5)); 

$matrix = [[1, 2, 3], [4, 5], [6]];
$sum = 0;
foreach ($matrix as $row) {
    $sum += array_sum($row);
}
echo $sum."\n"; 

$resultArray = [];
$num = 1;
for ($i = 0; $i < 3; $i++) {
    $row = [];
    for ($j = 0; $j < 3; $j++) {
        $row[] = $num++;
    }
    $resultArray[] = $row;
}
print_r($resultArray);

$nums = [2, 5, 3, 9];
$result = ($nums[0] * $nums[1]) + ($nums[2] * $nums[3]);
echo $result."\n"; 

$user = [
    'name' => 'Alexandra',
    'surname' => 'Andreeva',
    'patronymic' => 'Danilovna'
];
echo "{$user['surname']} {$user['name']} {$user['patronymic']}\n"; 


$date = [
    'year' => date('Y'),
    'month' => date('m'),
    'day' => date('d')
];
echo "{$date['year']}-{$date['month']}-{$date['day']}\n"; 

$arr = ['a', 'b', 'c', 'd', 'e'];
echo count($arr)."\n"; 

echo end($arr) . "\n"; 
echo $arr[count($arr)-2] . "\n"; 
