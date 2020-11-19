use rzfm_app;

drop table if exists ORDER_DISH;

create table ORDER_DISH(
	id int primary key auto_increment,
    order_id int not null,
    dish_id int not null,
    foreign key(order_id) references `ORDER`(id),
	foreign key(dish_id) references DISH(id)
);