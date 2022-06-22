<?php

require_once '/var/www/html/database.php';
require_once '/var/www/html/todo.php';

if (!login()) {
    header('Location: /signup.php');
    return;
}

if (!isset($_POST['id'])) {
    return;
}

try {
    $db = new Database();
    $db->doneTodo(new Todo($_POST['id'], "", false));
} catch (Exception $e) {
    var_dump($e->getMessage());
}

header('Location: /');
