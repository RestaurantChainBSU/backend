use rzfm_app;

delimiter $$

drop procedure if exists get_restaurant_dishes;

create procedure get_restaurant_dishes(in rest_id int)
begin 
select
	d.*
from 
	RESTAURANT as r 
		inner join REST_DISH as rd 
			on r.id = rd.rest_id
		inner join DISH as d 
			on d.id = rd.dish_id
where r.id = rest_id;

end$$
