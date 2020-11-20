use rzfm_app;

delimiter $$

drop procedure if exists get_order_dishes;

create procedure get_order_dishes(in order_id int)
begin 
select
	d.*
from 
	`ORDER` as o 
		inner join ORDER_DISH as od 
			on o.id = od.order_id
		inner join DISH as d 
			on d.id = od.dish_id
where o.id = order_id;

end$$