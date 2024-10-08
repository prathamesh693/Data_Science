-- average()
-- max()
-- min()
-- groupby()	

SELECT company, division, SUM(sales)
FROM finance_table
GROUP BY company
ORDER BY SUM(sales)

select * from payment

select staff_id, customer_id, sum(amount) -- catagorical column
from payment
group by staff_id,customer_id
order by sum(amount)
-- if the catagorical column are change then the output column are also change

select staff_id, customer_id, sum(amount) -- catagorical column
from payment
group by staff_id,customer_id
order by staff_id

select staff_id, customer_id, sum(amount) -- catagorical column
from payment
group by staff_id,customer_id
order by staff_id, customer_id
-- both staff and customer id are order and group together

select * from payment
	
select date(payment_date),sum(amount) from payment
group by date(payment_date)

select date(payment_date),sum(amount) from payment
group by date(payment_date)
order by sum(amount) desc

-- challenges
/* we have two ...
to give a bonus to the staff that handled the most payment
*/
select staff_id, count(amount)
from payment
group by staff_id

select rating, avg(replacement_cost)
from film
group by rating

select rating, ROUND(avg(replacement_cost),2)
from film
group by rating

select customer_id, sum(amount) from payment
group by customer_id
order by sum(amount) desc -- top to botoom list
limit 5 -- top 5 rows

select customer_id,sum(amount) from payment
group by customer_id
order by sum(amount)

-- having allows us to use the aggregate 
select customer_id,sum(amount) from payment
where customer_id not in (184,87,477)
group by customer_id

select customer_id,sum(amount) from payment
group by customer_id
having sum(amount)>100











