<?php
require_once '/var/www/html/database.php';
require_once '/var/www/html/todo.php';

if (!login()) {
    header('Location: /signup.php');
    return;
}

if (empty($_POST['body'])) {
	header("Location: /");
	return;
}

$db = new Database();
$db->insertTodo(new Todo(-1, $_POST['body']), false);

header("Location: /");
