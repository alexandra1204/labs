<?php
class ApiClient {
    private $baseUrl;
    private $authToken;
    private $authType;

    public function __construct($baseUrl, $auth = null, $authType = 'token') {
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->authToken = $auth;
        $this->authType = $authType;
    }

    private function sendRequest($endpoint, $method = 'GET', $data = null) {
        $url = $this->baseUrl . '/' . ltrim($endpoint, '/');
        $headers = ['Accept: application/json'];

        if ($this->authToken) {
            if ($this->authType === 'basic') {
                $headers[] = 'Authorization: Basic ' . base64_encode($this->authToken);
            } else {
                $headers[] = 'Authorization: Bearer ' . $this->authToken;
            }
        }

        $options = [
            'http' => [
                'method' => $method,
                'header' => implode("\r\n", $headers),
                'ignore_errors' => true
            ]
        ];

        if ($data) {
            $options['http']['content'] = json_encode($data);
            $headers[] = 'Content-Type: application/json';
        }

        $context = stream_context_create($options);
        $response = file_get_contents($url, false, $context);
        
        return [
            'status' => $http_response_header[0] ?? '',
            'body' => json_decode($response, true)
        ];
    }

    public function get($endpoint) {
        return $this->sendRequest($endpoint);
    }

    public function post($endpoint, $data) {
        return $this->sendRequest($endpoint, 'POST', $data);
    }

    public function put($endpoint, $data) {
        return $this->sendRequest($endpoint, 'PUT', $data);
    }

    public function delete($endpoint) {
        return $this->sendRequest($endpoint, 'DELETE');
    }
}

$client = new ApiClient('https://jsonplaceholder.typicode.com');

$posts = $client->get('posts');
print_r($posts['body'][0]);

$newPost = $client->post('posts', [
    'title' => 'foo',
    'body' => 'bar',
    'userId' => 1
]);
print_r($newPost['body']);

// Example with authentication
$protectedClient = new ApiClient(
    'https://api.example.com',
    'username:password', 
    'basic' 
);
$userData = $protectedClient->get('user');
print_r($userData['body']);

// Simple weather app example
class WeatherApp {
    private $api;
    
    public function __construct() {
        $this->api = new ApiClient('https://api.openweathermap.org/data/2.5', 'YOUR_API_KEY');
    }
    
    public function getWeather($city) {
        $response = $this->api->get("/weather?q=$city&units=metric");
        return $response['body']['main']['temp'] ?? null;
    }
}

$weather = new WeatherApp();
echo "Current temperature: " . $weather->getWeather('London') . "°C";
?>