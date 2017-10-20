drop table if exists topping;
drop table if exists size;
drop table if exists pizza_order;

create table topping (
    id integer primary key autoincrement,
    name text not null
);

create table size (
    id integer primary key autoincrement,
    name text not null
);

create table pizza_order (
    id integer primary key autoincrement,
    id_topping integer references topping(id) not null,
    id_size integer references size(id) not null,
    created_at timestamp not null
);

insert into topping(name) values ('Pepperoni'), ('Bacon'), ('Mushrooms'), ('Sausage');
insert into size(name) values ('Small'), ('Medium'), ('Large'), ('Colossal');
