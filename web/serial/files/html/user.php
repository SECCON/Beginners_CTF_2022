<?php

class User
{
    private const invalid_keywords = array("UNION", "'", "FROM", "SELECT", "flag");

    public $id;
    public $name;
    public $password_hash;

    public function __construct($id = null, $name = null, $password_hash = null)
    {
        $this->id = htmlspecialchars($id);
        $this->name = htmlspecialchars(str_replace(self::invalid_keywords, "?", $name));
        $this->password_hash = $password_hash;
    }

    public function __toString()
    {
        return "id: " . $this->id . ", name: " . $this->name . ", pass: " . $this->password_hash;
    }

    public function isValid()
    {
        return isset($this->id) && isset($this->name) && isset($this->password_hash);
    }
}

function login()
{
    if (empty($_COOKIE["__CRED"])) {
        return false;
    }

    $user = unserialize(base64_decode($_COOKIE['__CRED']));

    // check if the given user exists
    try {
        $db = new Database();
        $storedUser = $db->findUserByName($user);
    } catch (Exception $e) {
        die($e->getMessage());
    }
    // var_dump($user);
    // var_dump($storedUser);
    if ($user->password_hash === $storedUser->password_hash) {
        // update stored user with latest information
        // die($storedUser);
        setcookie("__CRED", base64_encode(serialize($storedUser)));
        return true;
    }
    return false;
}

function logout()
{
    setcookie("__CRED", "", time() - 30);
}
