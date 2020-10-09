PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    username VARCHAR(25) primary key,
    password VARCHAR(50),
    email VARCHAR(50)
);

INSERT INTO users(username,password,email) VALUES ('Testing','Password123','sample@gmail.com');