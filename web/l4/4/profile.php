<?php
session_start();

if (!isset($_SESSION['user_data'])) {
    header('Location: form.php');
    exit;
}

$userData = $_SESSION['user_data'];
?>

<!DOCTYPE html>
<html>
<head>
    <title>Профиль</title>
    <meta charset="UTF-8">
    <style>
        .profile { max-width: 400px; margin: 20px auto; }
        .data-item { margin-bottom: 10px; }
        .label { font-weight: bold; }
    </style>
</head>
<body>
    <div class="profile">
        <h2>Ваши данные:</h2>
        
        <div class="data-item">
            <span class="label">Имя:</span>
            <?= $userData['name'] ?>
        </div>
        
        <div class="data-item">
            <span class="label">Email:</span>
            <?= $userData['email'] ?>
        </div>
        
        <div class="data-item">
            <span class="label">Телефон:</span>
            <?= $userData['phone'] ?>
        </div>
        
        <a href="form.php">Изменить данные</a>
    </div>
</body>
</html>
