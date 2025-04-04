<?php

$str = 'bahb bacb abeb aebb badcb bxeb';

preg_match_all('/b..b/', $str, $matches3); 
print_r($matches3[0]); 