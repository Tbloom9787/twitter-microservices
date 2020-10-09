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

DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets (
    id INTEGER PRIMARY KEY,
    text VARCHAR(500),
    timestamp DATE,
    author VARCHAR(25),
    FOREIGN KEY(author) REFERENCES users(username)
);

INSERT INTO users(username,password,email) VALUES ('Testing','Password123','sample@gmail.com');

INSERT INTO followers(username,follower) VALUES ('Postman', 'Testing');

INSERT INTO tweets(text,timestamp,author) VALUES ('Cheese and biscuits cream cheese feta emmental pepper jack hard cheese cheeseburger lancashire','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Tootsie roll tootsie roll icing soufflé topping fruitcake carrot cake chocolate cake candy.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Soufflé tiramisu cake muffin tootsie roll bonbon brownie. Muffin biscuit chocolate cake macaroon sweet danish muffin sweet soufflé. Donut macaroon chupa chups.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Cake biscuit gummies bonbon muffin soufflé lemon drops carrot cake.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Tiramisu liquorice cookie jujubes. Bear claw topping oat cake jelly beans cupcake bear claw toffee bonbon. Lollipop pudding oat cake marshmallow gummi bears.','2020-05-09 07:34:04','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Croissant chupa chups fruitcake icing chocolate cake.','2020-05-09 07:34:04','Joe Biden');
INSERT INTO tweets(text,timestamp,author) VALUES ('Pudding icing fruitcake carrot cake pudding pudding tootsie roll. Gingerbread candy icing chocolate cake.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Jelly cookie icing soufflé chocolate sweet roll caramels. Bear claw candy canes pastry cotton candy lollipop jelly tootsie roll tart.','2020-05-09 07:34:04','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Lemon drops dragée jelly-o topping. Jelly macaroon sesame snaps cheesecake powder powder brownie chupa chups jelly.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Bonbon caramels ice cream marzipan chupa chups oat cake. Tiramisu brownie cupcake pie pie jujubes chocolate cake cheesecake chocolate cake.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Gummi bears donut cake jelly lemon drops liquorice sweet brownie chocolate bar. Gummies cheesecake candy tiramisu sweet roll sweet roll icing pastry. Liquorice pie jelly pastry.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Biscuit tart danish jujubes sweet roll toffee sesame snaps sweet candy canes.','2020-05-09 07:34:04','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Sesame snaps cupcake cookie sweet. Topping topping sugar plum toffee fruitcake cake lollipop.','2020-05-09 07:34:04','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Cupcake chupa chups sweet. Muffin gummi bears cake oat cake chocolate.','2020-05-09 07:34:04','Joe Biden');
INSERT INTO tweets(text,timestamp,author) VALUES ('Cake toffee chocolate cake gummies candy. Cotton candy pie sugar plum cupcake jelly beans sesame snaps sugar plum.','2020-05-09 07:34:04','Joe Biden');
INSERT INTO tweets(text,timestamp,author) VALUES ('Biscuit cheesecake marshmallow. Cake dragée brownie cookie marshmallow danish powder sugar plum.','2020-05-09 07:34:04','Joe Biden');
INSERT INTO tweets(text,timestamp,author) VALUES ('Dragée pastry cotton candy dragée jujubes jelly beans. Muffin sugar plum topping powder.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm.','2020-10-08 04:07:32','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Pinnace holystone mizzenmast quarter crows nest nipperkin grog yardarm hempen', '2020-05-24 12:43:21','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.','2020-12-22 03:12:46','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors.','2020-05-09 07:34:04','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Bring a spring upon her cable holystone blow the man down spanker','2020-05-09 07:34:04','Joe Biden');
INSERT INTO tweets(text,timestamp,author) VALUES ('Shiver me timbers to go on account lookout wherry doubloon chase.','2020-05-09 07:34:04','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.','2020-05-09 07:34:04','Joe Biden');
INSERT INTO tweets(text,timestamp,author) VALUES ('Trysail Sail ho Corsair red ensign hulk smartly boom jib rum gangway.','2020-05-09 07:34:04','Joe Biden');
INSERT INTO tweets(text,timestamp,author) VALUES ('ase shot Shiver me timbers gangplank crack Jennys tea cup ballast Blimey lee snow crows nest rutters.','2020-05-09 07:34:04','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Fluke jib scourge of the seven seas boatswain schooner gaff booty Jack Tar transom spirits.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Cheesy feet blue castello jarlsberg. Emmental cream cheese blue castello lancashire say cheese cheesy grin manchego fromage.','2020-05-09 07:34:04','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Goat camembert de normandie jarlsberg taleggio red leicester pecorino stilton the big cheese. Cauliflower cheese goat.','2020-05-09 07:34:04','Postman');
INSERT INTO tweets(text,timestamp,author) VALUES ('Chalk and cheese danish fontina macaroni cheese cauliflower cheese roquefort pepper jack cheeseburger rubber cheese.','2020-05-09 07:34:04','Donald Trump');
INSERT INTO tweets(text,timestamp,author) VALUES ('Who moved my cheese boursin cheesy feet. ','2020-05-09 07:34:04','Joe Biden');

COMMIT;