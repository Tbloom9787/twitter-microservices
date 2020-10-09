-- $ sqlite3 microservices.db < schema.sql

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    username VARCHAR(25) primary key,
    password VARCHAR(50),
    email VARCHAR(50)
);

DROP TABLE IF EXISTS followers;
CREATE TABLE followers (
    username VARCHAR(20),
    follower VARCHAR(20),
    PRIMARY KEY (username, follower),
    FOREIGN KEY (username) REFERENCES users(username)
);

INSERT INTO users(username,password,email) VALUES ('Testing','Password123','sample@gmail.com');

INSERT INTO followers(username,follower) VALUES ('Postman', 'Testing');