<?php

class Todo {
    private const invalid_keywords = array("UNION", "'", "FROM", "SELECT", "flag");

    public $id;
    public $body;
    public $done;

    public function __construct($id = null, $body = null, $done = null) {
        $this->id = htmlspecialchars($id);
        $this->body = htmlspecialchars(str_replace(self::invalid_keywords, "?", $body));
        $this->done = $done;
    }
}
