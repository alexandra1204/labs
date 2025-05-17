<?php
// GET
function getPosts() {
    $url = 'https://jsonplaceholder.typicode.com/posts';
    $response = file_get_contents($url);
    return json_decode($response, true);
}

// POST
function createPost($title, $body, $userId = 1) {
    $url = 'https://jsonplaceholder.typicode.com/posts';
    $data = [
        'title' => $title,
        'body' => $body,
        'userId' => $userId
    ];
    
    $options = [
        'http' => [
            'method' => 'POST',
            'header' => "Content-Type: application/json\r\n",
            'content' => json_encode($data)
        ]
    ];
    
    $context = stream_context_create($options);
    $response = file_get_contents($url, false, $context);
    return json_decode($response, true);
}

// PUT
function updatePost($postId, $title, $body, $userId = 1) {
    $url = "https://jsonplaceholder.typicode.com/posts/$postId";
    $data = [
        'id' => $postId,
        'title' => $title,
        'body' => $body,
        'userId' => $userId
    ];
    
    $options = [
        'http' => [
            'method' => 'PUT',
            'header' => "Content-Type: application/json\r\n",
            'content' => json_encode($data)
        ]
    ];
    
    $context = stream_context_create($options);
    $response = file_get_contents($url, false, $context);
    return json_decode($response, true);
}

// DELETE
function deletePost($postId) {
    $url = "https://jsonplaceholder.typicode.com/posts/$postId";
    
    $options = [
        'http' => [
            'method' => 'DELETE'
        ]
    ];
    
    $context = stream_context_create($options);
    $response = file_get_contents($url, false, $context);
    return $response === '{}';
}

getPosts()[0]['title'];                     
createPost('A', 'B')['id'];                 
updatePost(1, 'X', 'Y')['title'];           
deletePost(1); 
?>