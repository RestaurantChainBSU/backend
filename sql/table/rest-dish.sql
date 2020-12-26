use rzfm_app;

drop table if exists REST_DISH;

create table REST_DISH(
	rd_id int primary key auto_increment,
    rest_id int not null,
    dish_id int not null,
	foreign key(rest_id) references RESTAURANT(id) on delete cascade,
    foreign key(dish_id) references DISH(id) on delete cascade
);

insert into REST_DISH(rest_id, dish_id) values(1, 1);
insert into REST_DISH(rest_id, dish_id) values(1, 3);
insert into REST_DISH(rest_id, dish_id) values(2, 2);
insert into REST_DISH(rest_id, dish_id) values(2, 1);
insert into REST_DISH(rest_id, dish_id) values(3, 1);
insert into REST_DISH(rest_id, dish_id) values(3, 3);