use rzfm_app;

drop table if exists APP_USER;

create table APP_USER(
	id int primary key auto_increment,
    login varchar(25) not null,
    pass varchar(25) not null,
    email varchar(40) not null, 
    first_name varchar (30) not null,
	role_type int not null # 0 - regular user, 1 - admin 
);


insert into APP_USER(login, pass, email, first_name, role_type) values("kirillzhelt", "fitbitteam", "kzhelt@fitbit.com", "kirill", "1");
insert into APP_USER(login, pass, email, first_name, role_type) values("volodya", "vov!vov", "vovandroid@milo.com", "vova", "0");
insert into APP_USER(login, pass, email, first_name, role_type) values("dima1337", "1337dima", "furs1348@rdp.com", "rdprule", "1");
insert into APP_USER(login, pass, email, first_name, role_type) values("sanya", "bigdata", "sanya@issoft.by", "mmsanya", "0");

