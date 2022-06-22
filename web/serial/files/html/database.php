<?php

require_once '/var/www/html/user.php';
require_once '/var/www/html/todo.php';

class Database
{

    /**
     * $_con is a instance of mysqli
     */
    protected $_con;

    public function __construct()
    {
        $this->connect();
    }

    public function __destruct()
    {
        $this->close();
    }

    /**
     * connect connects to the database
     */
    public function connect()
    {
        $this->_con = new mysqli('mysql', 'ctf4b', 'ctf4b', 'serial');
        if ($this->_con->connect_error) {
            throw new Exception('Connect Error ' . $this->_con->connect_errno . ': ' . $this->_con->connect_error, $this->_con->connect_errno);
        } else {
            $this->_con->set_charset("utf8mb4");
        }

        if (!$this->_con->ping()) {
            throw new Exception('failed ping()');
        }

        return $this->_con;
    }

    /**
     * close closes connection
     */
    public function close()
    {
        if (!isset($this->_con)) {
            return;
        }
        $this->_con->close();
    }

    /**
     * findUserByName finds a user from database by given userId.
     * 
     * @deprecated this function might be vulnerable to SQL injection. DO NOT USE THIS FUNCTION.
     */
    public function findUserByName($user = null)
    {
        if (!isset($user->name)) {
            throw new Exception('invalid user name: ' . $user->user);
        }

        $sql = "SELECT id, name, password_hash FROM users WHERE name = '" . $user->name . "' LIMIT 1";
        $result = $this->_con->query($sql);
        if (!$result) {
            throw new Exception('failed query for findUserByNameOld ' . $sql);
        }

        while ($row = $result->fetch_assoc()) {
            $user = new User($row['id'], $row['name'], $row['password_hash']);
        }
        return $user;
    }

    /**
     * findUserByName finds a user from database by given userId.
     */
    public function findUserByNameNew($name = null)
    {
        if (!isset($name)) {
            throw new Exception('invalid user name: ' . $name);
        }

        $stmt = $this->_con->stmt_init();
        if (!$stmt->prepare("SELECT id, password_hash FROM users WHERE name = ?")) {
            throw new Exception('failed prepare for findUserByName');
        }
        if (!$stmt->bind_param("s", $name)) {
            throw new Exception('failed bind_param for findUserByName');
        }
        if (!$stmt->execute()) {
            throw new Exception('failed execute for findUserByName');
        }

        $id = null;
        $password_hash = null;

        if (!$stmt->bind_result($id, $password_hash)) {
            throw new Exception('failed bind_result for findUserByName');
        }
        $stmt->fetch();

        return new User($id, $name, $password_hash);
    }

    /**
     * insertUser inserts a given user into database.
     */
    public function insertUser($user = null)
    {
        if (!isset($user->name) || !isset($user->password_hash)) {
            throw new Exception('invalid name: ' . $user->name . ', or password: ' . $user->password_hash);
        }

        $stmt = $this->_con->stmt_init();
        if (!$stmt->prepare("INSERT INTO users(name, password_hash) VALUE (?, ?)")) {
            throw new Exception('failed prepare for findUserByName');
        }
        if (!$stmt->bind_param('ss', $user->name, $user->password_hash)) {
            throw new Exception('failed bind_param for findUserByName: ' . $user->name);
        }
        if (!$stmt->execute()) {
            throw new Exception('failed execute for findUserByName');
        }
    }

    /**
     * findTodos find all todos which is not done.
     */

    public function findTodos()
    {
        $sql = "SELECT * FROM todos WHERE done = false ORDER BY id";
        $result = $this->_con->query($sql);
        if (!$result) {
            throw new Exception('failed query for findUserByNameOld ' . $sql);
        }

        $todos = array();
        while ($row = $result->fetch_assoc()) {
            $t = new Todo($row["id"], $row["body"], $row["done"]);
            array_push($todos, $t);
        }
        return $todos;
    }

    /**
     * insertTodo insert a todo with given body.
     */
    public function insertTodo($todo = null) 
    {
        if (!isset($todo->body)) {
            throw new Exception('invalid message: ' . $todo->body);
        }

        $stmt = $this->_con->stmt_init();
        if (!$stmt->prepare("INSERT INTO todos(body) VALUE (?)")) {
            throw new Exception('failed prepare for insertTodo');
        }
        if (!$stmt->bind_param('s', $todo->body)) {
            throw new Exception('failed bind_param for insertTodo: ' . $todo->body);
        }
        if (!$stmt->execute()) {
            throw new Exception('failed execute for insertTodo');
        }
    }

    /**
     * doneTodo update a done column true with a given id.
     */
    public function doneTodo($todo = null)
    {
        if (!isset($todo->id)) {
            throw new Exception('invalid id: ' . $todo);
        }

        $stmt = $this->_con->stmt_init();
        if (!$stmt->prepare("UPDATE todos SET done = 1 WHERE id = ?")) {
            // TODO:
            throw new Exception('failed prepare for doneTodo' . "UPDATE todos SET done = true WHERE id = ?");
        }
        if (!$stmt->bind_param('i', $todo->id)) {
            throw new Exception('failed bind_param for doneTodo: ' . $todo->id);
        }
        if (!$stmt->execute()) {
            throw new Exception('failed execute for doneTodo');
        }
    }
}
