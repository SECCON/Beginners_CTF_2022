<?php
require_once '/var/www/html/database.php';
require_once '/var/www/html/user.php';

if (!login()) {
    header('Location: /signup.php');
    return;
}
?>

<!DOCTYPE html>
<html>

<head>
    <title>Todo List</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>

<body>
    <nav class="navbar navbar-light bg-light float-right">
        <a href="logout.php">Logout</a>
    </nav>
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col col-xl-10">


                <div class="card" style="border-radius: 15px;">
                    <div class="card-body p-5">

                        <h1>Todo List</h1>

                        <form action="todo_create.php" method="POST" class="form-inline d-flex justify-content-center align-items-center mb-4">
                            <div class="form-outline flex-fill">
                                <input type="text" class="form-control" name="body" placeholder="Enter your task here!" />
                                <input type="submit" value="Register" class="btn btn-primary ms-2">
                            </div>
                        </form>
                        <hr>

                        <ul class="list-group mb-0">
                            <?php
                            $db = new Database();
                            $todos = $db->findTodos();
                            foreach ($todos as $todo) {
                                echo "<form action='todo_update.php' method='POST'><tr>
                                <li class='list-group-item d-flex justify-content-between align-items-center border-start-0 border-top-0 border-end-0 border-bottom rounded-0 mb-2'>
                                <div class='d-flex align-items-center'>" .  $todo->body . "</div>
                                <input type='hidden' name='id' value='" . $todo->id . "' />
                                <input type='submit' value='done' />
        </form>";
                            }
                            unset($todo);

                            print "</table>";
                            ?>
                        </ul>
                    </div>

                </div>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>

</html>