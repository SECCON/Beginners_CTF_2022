DROP TABLE IF EXISTS todos;

CREATE TABLE todos(
    id int AUTO_INCREMENT,
    body varchar(128) NOT NULL,
    done boolean default false NOT NULL,
    primary key(id)
);

DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id int AUTO_INCREMENT,
    name varchar(128) NOT NULL,
    password_hash varchar(128) NOT NULL,
    primary key(id),
    index(name)
);

DROP TABLE IF EXISTS flags;

CREATE TABLE flags(
    body varchar(128) NOT NULL
);

REVOKE ALL PRIVILEGES ON `serial`.* FROM 'ctf4b'@'%';
GRANT SELECT, INSERT, UPDATE ON `serial`.* TO 'ctf4b'@'%';
