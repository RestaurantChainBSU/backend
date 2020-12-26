use rzfm_app;

drop table if exists `ORDER`;

create table `ORDER`(
	id int primary key auto_increment,
    address varchar(300) not null,
	total_price decimal(10, 2) not null,
    order_status int not null
);

