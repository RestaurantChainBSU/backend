use rzfm_app;

drop table if exists RESTAURANT;

create table RESTAURANT(
	rest_id int primary key auto_increment,
    rest_name varchar(100) not null,
    rest_descr varchar(1000) not null,
    address varchar(200) not null,
    latitude decimal(8, 6) not null,
    longitude decimal(9, 6) not null,
    image_link varchar(500) not null
);


insert into RESTAURANT(rest_name, rest_descr, address, latitude, longitude, image_link) values("Pogrebok", "The best restaurant ever", "Minks, Oktybrskaya 10 912", 53.892333, 27.567430, "https://i.mycdn.me/i?r=AyH4iRPQ2q0otWIFepML2LxRP1tP-whoDx6D6ZKX3Tk8nw");
insert into RESTAURANT(rest_name, rest_descr, address, latitude, longitude, image_link) values("Pena", "The best beer restaurant ever", "Minks, Kubisheva 45", 53.914952, 27.570008, "https://avatars.mds.yandex.net/get-altay/1981910/2a0000016f9d7173f481aa28076b6e7ec93d/XXXL");
insert into RESTAURANT(rest_name, rest_descr, address, latitude, longitude, image_link) values("Shawarma-express", "The best shawarma restaurant ever", "Minks, Leningradskaya 2", 53.895182, 27.550843, "https://avatars.mds.yandex.net/get-altay/2838749/2a0000017033f93f136cf80724a7a9d6133c/XXXL");

