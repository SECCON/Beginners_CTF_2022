<?php

require_once '/var/www/html/database.php';

if (!isset($_POST['name']) || !isset($_POST['pass'])) {
    echo '<!DOCTYPE html>
    <html>
    
    <head>
        <title>Todo List</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>
    
    <body>
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-xl-10">
    
    
                    <div class="card" style="border-radius: 15px;">
                        <div class="card-body p-5">
                            <h1 class="text-center">User Signup</h1>
                            <form action="/signup.php" method="post" class="form-inline d-flex justify-content-center align-items-center mb-4">
                                <input type="text" class="form-control" name="name" placeholder="username" />
                                <input type="password" class="form-control" name="pass" placeholder="pass"/>
                                <input type="submit" value="Register" class="btn btn-primary ms-2"/>
                            </form>
    
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    
    </html>';
    return;
}

$name = $_POST['name'];
$pass = password_hash($_POST['pass'], PASSWORD_DEFAULT);
$user = new User(-1, $name, $pass);

try {
    $db = new Database();
    $db->insertUser($user);

    $user = $db->findUserByName($user);
    if (!$user->isValid()) {
        throw new Exception("invalid user: " . $user->__toString());
    }
} catch (Exception $e) {
    var_dump($e->getMessage());
}

setcookie("__CRED", base64_encode(serialize($user)));

header('Location: /');
