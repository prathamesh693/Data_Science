/* july_7
we are launching a platinium service for our most loyal customers
we will assign a platinium status to customer that have 40 or more transition paymentj
Q. what customer id are to elligible for platinium service
*/
select customer_id,count(*) from payment
group by customer_id
having count(*)>=40

/*
Q. what are the customer ids ofcustomer who have spent more than 100 
in payment transitions with our staff id member 2
*/
select customer_id,sum(amount) from payment
where staff_id=2
group by customer_id
having sum(amount)>100
-- group by and having important for interview

/*
AS AGRRIGATES
select column AS new name from table # AS clause
also changes the output column name 
	but this is temperary name of the column 
*/
-- ex.1
select amount as rental_price 
from payment
--ex.2
select sum(amount) as net_revenue
from payment;
--ex.3
select count(amount) as num_transactions
from payment;
select count(*) as num_transactions
from payment;
--ex.4
select customer_id, sum(amount) as total_spent
from payment
group by customer_id
--ex.5
select customer_id, sum(amount) as total_spent
from payment
group by customer_id
having sum(amount)>100
--ex.6 give an error 
/*
select customer_id, sum(amount) as total_spent
from payment
group by customer_id
having total_spent>100
*/
--ex.7 give an error 
/* not use for upcoming purpose 
select customer_id, amount as new_name
from payment
where new_name>2 
*/
/* IMPORTANT 
order of excution 
1.FROM
2.WHERE
3.GROUP BY
4.HAVING
5.SELECT
6.ORDER
*/
/*
join allows us to combine multiple tables together.
the main reason for the different join types is to decide how to deal
with information only present in one of the joined tables.

# Joining of the table 
1. inner join #will result with the set of records that match in both the tables.
2. outer join # 
3. full join
4. 
*/
--ex.of INNER JOIN
/* remember that table order won't matter in an INNER JOIN
Also if you see just JOIN without the INNER, PostgreSQL will treat
it as an INNER JOIN */
SELECT * FROM payment
SELECT * FROM customer
--ex.1
SELECT payment_id,payment.customer_id, first_name FROM payment
INNER JOIN customer
ON payment.customer_id = customer.customer_id
--ex.2
SELECT payment_id,payment.customer_id,first_name
FROM customer
INNER JOIN payment
ON payment.customer_id = customer.customer_id
/* OUTER JOIN has three type 
1. full outer join 
2. right outer join
3. left outer join
*/
--ex.1
SELECT * FROM payment 
FULL OUTER JOIN customer
ON payment.customer_id = customer.customer_id
-- GIVE AN ERROR ...... WHERE payment_id IS NULL OR customer_id IS NULL
/* LEFT OUTER JOIN
# matches only records and which are not matching it shows as null
# the left table (catagorial column) is same but the right column(table) will be 
change or check for matches and shows null value
# in LEFT OUTER JOIN ** ORDER MATTERS
# for use WHERE to get unique to the rows
*/
SELECT * FROM film
SELECT * FROM inventory
--ex.1
SELECT film.film_id,inventory_id,title
FROM film
LEFT JOIN inventory 
ON inventory.film_id = film.film_id
-- ex.2
SELECT film.film_id,title,inventory_id,store_id
FROM film
LEFT JOIN inventory 
ON inventory.film_id = film.film_id
--ex.3 (apply where clause)
SELECT film.film_id,inventory_id,title
FROM film
LEFT JOIN inventory 
ON inventory.film_id = film.film_id
WHERE inventory.film_id IS NULL
/* RIGHT JOIN 
# matches only records and which are not matching it shows as null
# the right table is same but the left column(table) will be 
change or check for matches and shows null value
# in RIGHT OUTER JOIN ** ORDER MATTERS
# for use WHERE to get unique to the rows
*/
--ex.1
SELECT film.film_id,inventory_id,store_id,title
FROM film
RIGHT JOIN inventory 
ON inventory.film_id = film.film_id
--ex.2 (apply where clause)
SELECT inventory.film_id,inventory_id,store_id,title
FROM inventory
RIGHT JOIN film 
ON film.film_id = inventory.film_id
WHERE inventory.film_id IS NULL


