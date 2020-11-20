use rzfm_app;

drop table if exists DISH;

create table DISH(
	id int primary key auto_increment,
	dish_name varchar(200) not null,
    dish_descr varchar(500) not null,
    price decimal(9, 2) not null,
    image_link varchar(500) not null
);

insert into DISH(dish_name, dish_descr, price, image_link) values("Pancakes", "Pancakes with barries", 10.50, "https://static.independent.co.uk/s3fs-public/thumbnails/image/2017/03/14/14/pancakes-istock-stephaniefrey-.jpg?width=982&height=726");
insert into DISH(dish_name, dish_descr, price, image_link) values("Rice with seafood", "Spicy rice with mussels and shrimps", "15.00", "https://loveincorporated.blob.core.windows.net/contentimages/gallery/8af07ba5-d39f-487d-aa37-4e62a9fdad37-worlds-most-delicious-dishes-youll-want-to-try.jpg");
insert into DISH(dish_name, dish_descr, price, image_link) values("Chicken Burger", "Burger with chicken", 12.00, "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/mexican-chicken-burger_1-b5cca6f.jpg?quality=90&resize=440%2C400");
insert into DISH(dish_name, dish_descr, price, image_link) values("Salmon steak", "Salmon steak with vegetables", 22.70, "https://i.artfile.ru/2880x1800_921205_[www.ArtFile.ru].jpg");