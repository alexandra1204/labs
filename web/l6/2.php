<?php
// GET с заголовками
function getWithHeaders($url, $headers) {
    $context = stream_context_create(['http' => ['header' => $headers]]);
    return json_decode(file_get_contents($url, false, $context), true);
}
// POST JSON
function postJson($url, $data) {
    $context = stream_context_create([
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/json\r\n",
            'content' => json_encode($data)
        ]
    ]);
    return json_decode(file_get_contents($url, false, $context), true);
}
// GET с параметрами
function getWithParams($url, $params) {
    $query = http_build_query($params);
    return json_decode(file_get_contents("$url?$query"), true);
}

getWithHeaders('https://api.example.com/data', "Auth: token\r\n")[0];
postJson('https://api.example.com/posts', ['title' => 'Test'])['id'];
getWithParams('https://api.example.com/search', ['q' => 'php'])['items'];
?>
