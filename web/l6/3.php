<?php
class ApiClient {
//Универсальный метод для выполнения HTTP-запросов
    public static function makeRequest($url, $method = 'GET', $data = null, $headers = []) {
        $context = [
            'http' => [
                'method' => $method,
                'header' => implode("\r\n", $headers),
                'ignore_errors' => true 
            ]
        ];
        
        if ($data) {
            $context['http']['content'] = is_array($data) ? json_encode($data) : $data;
            $context['http']['header'] .= "\r\nContent-Type: application/json";
        }

        $response = @file_get_contents($url, false, stream_context_create($context));
        $status = $http_response_header[0] ?? '';

        if ($response === false) {
            throw new Exception("Request failed: " . error_get_last()['message']);
        }
        
        preg_match('/HTTP\/\d\.\d (\d{3})/', $status, $matches);
        $statusCode = $matches[1] ?? 0;
        
        $body = json_decode($response, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            $body = $response;
        }
        
        return [
            'status' => $statusCode,
            'body' => $body
        ];
    }
    
    //cURL-версия с обработкой исключений
    public static function makeCurlRequest($url, $method = 'GET', $data = null, $headers = []) {
        $ch = curl_init($url);
        
        $options = [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_CUSTOMREQUEST => $method,
            CURLOPT_FAILONERROR => false,
            CURLOPT_HTTPHEADER => array_merge(['Accept: application/json'], $headers)
        ];
        
        if ($data) {
            $options[CURLOPT_POSTFIELDS] = is_array($data) ? json_encode($data) : $data;
        }
        
        curl_setopt_array($ch, $options);
        
        try {
            $response = curl_exec($ch);
            $status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            
            if (curl_errno($ch)) {
                throw new Exception(curl_error($ch), curl_errno($ch));
            }
            
            $body = json_decode($response, true);
            if (json_last_error() !== JSON_ERROR_NONE) {
                $body = $response;
            }
            
            return [
                'status' => $status,
                'body' => $body
            ];
        } finally {
            curl_close($ch);
        }
    }
}