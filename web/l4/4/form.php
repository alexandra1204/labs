<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $_SESSION['user_data'] = [
        'name' => htmlspecialchars($_POST['name']),
        'email' => htmlspecialchars($_POST['email']),
        'phone' => htmlspecialchars($_POST['phone'])
    ];
    
    header('Location: profile.php');
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Ввод данных</title>
    <meta charset="UTF-8">
    <style>
        form { max-width: 400px; margin: 20px auto; }
        .field { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input { width: 100%; padding: 8px; }
    </style>
</head>
<body>
    <form method="POST">
        <div class="field">
            <label>Имя:</label>
            <input type="text" name="name" required>
        </div>
        
        <div class="field">
            <label>Email:</label>
            <input type="email" name="email" required>
        </div>
        
        <div class="field">
            <label>Телефон:</label>
            <input type="tel" name="phone" pattern="\+?[0-9\s\-]+" required>
        </div>
        
        <button type="submit">Отправить</button>
    </form>
</body>
</html>
