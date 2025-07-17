CREATE TABLE authors(
id INT NOT NULL AUTO_INCREMENT,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
primary key (id)
);


insert into authors(first_name, last_name) values ('Федор', 'Достоевский');
insert into authors(first_name, last_name) values ('Вадим', 'Зеланд');
insert into authors(first_name, last_name) values ('Теодор', 'Драйзер');

select * from authors;

CREATE TABLE publishers(
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(100) NOT NULL,
primary key(id)
);

insert into publishers(name) values ('2');
insert into publishers(name) values ('1');

select * from publishers;

CREATE TABLE books(
id INT NOT NULL AUTO_INCREMENT,
title VARCHAR(100) NOT NULL,
author_id INT NOT NULL,
publisher_id INT NOT NULL,
year INT NOT NULL,
primary key(id),
foreign key (author_id) references authors(id),
foreign key (publisher_id) references publishers(id)
);

insert into books(title, author_id, publisher_id, year) values ('книга 1', 1, 1, 1999);
insert into books(title, author_id, publisher_id, year) values ('книга 2', 2, 2, 1789);
insert into books(title, author_id, publisher_id, year) values ('книга 3', 3, 1, 1987);
insert into books(title, author_id, publisher_id, year) values ('книга 4', 3, 2, 1956);

SELECT title FROM books where year = '1999';
update books set year = '1323' where title = 'книга 1';

DELETE FROM books WHERE year < 1800;
SELECT * FROM books;


select id from authors;
select id from publishers;
