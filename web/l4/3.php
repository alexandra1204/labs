<?php

ob_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['text'])) {
    $text = mb_strtolower($_POST['text']);
    

    $vowels = preg_match_all('/[aeiouyаеёиоуыэюя]/iu', $text, $matches);

    $consonants = preg_match_all('/[bcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщ]/iu', $text, $matches);
} else {

    $vowels = 0;
    $consonants = 0;
}
ob_end_flush();
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Подсчёт букв</title>
    <style>
        .result { margin-top: 20px; padding: 10px; border: 1px solid #ccc; }
    </style>
</head>
<body>
    <form method="POST">
        <textarea name="text" cols="50" rows="10" 
                  placeholder="Введите текст..."><?= isset($_POST['text']) ? htmlspecialchars($_POST['text']) : '' ?></textarea><br>
        <button type="submit">Посчитать</button>
    </form>

    <?php if ($_SERVER['REQUEST_METHOD'] === 'POST'): ?>
        <div class="result">
            <h3>Результат:</h3>
            <p>Гласных: <?= $vowels ?></p>
            <p>Согласных: <?= $consonants ?></p>
        </div>
    <?php endif; ?>
</body>
</html>