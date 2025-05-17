<?php
$mysqli = new mysqli('db', 'root', 'helloworld', 'web');

if (mysqli_connect_errno()) {
    printf("Could not connect to MySQL: %s\n", mysqli_connect_error());
    exit;
}

$mysqli->query("CREATE TABLE IF NOT EXISTS ads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(100) NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)");

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $mysqli->real_escape_string($_POST['email']);
    $title = $mysqli->real_escape_string($_POST['title']);
    $category = $mysqli->real_escape_string($_POST['category']);
    $description = $mysqli->real_escape_string($_POST['description']);

    $query = "INSERT INTO ads (email, title, description, category) VALUES ('$email', '$title', '$description', '$category')";
    $mysqli->query($query);
}

$advertisements = [];
if ($result = $mysqli->query('SELECT * FROM ads ORDER BY created DESC')) {
    while ($row = $result->fetch_assoc()) {
        $advertisements[] = $row;
    }
    $result->close();
}
$mysqli->close();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Bulletin Board</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        form { margin-bottom: 20px; padding: 20px; background: #f5f5f5; border-radius: 5px; }
        input, textarea, select { width: 100%; padding: 8px; margin-bottom: 10px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Bulletin Board</h1>
    
    <form method="post">
        <label>Email: <input type="email" name="email" required></label><br>
        <label>Title: <input type="text" name="title" required></label><br>
        <label>Category:
            <select name="category" required>
                <option value="Electronics">Electronics</option>
                <option value="Furniture">Furniture</option>
                <option value="Clothing">Clothing</option>
            </select>
        </label><br>
        <label>Description: <textarea name="description" required></textarea></label><br>
        <button type="submit">Submit</button>
    </form>

    <h2>Advertisements:</h2>
    <table>
        <tr>
            <th>Email</th>
            <th>Title</th>
            <th>Description</th>
            <th>Category</th>
        </tr>
        <?php foreach ($advertisements as $ad): ?>
        <tr>
            <td><?= htmlspecialchars($ad['email']) ?></td>
            <td><?= htmlspecialchars($ad['title']) ?></td>
            <td><?= nl2br(htmlspecialchars($ad['description'])) ?></td>
            <td><?= htmlspecialchars($ad['category']) ?></td>
        </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>