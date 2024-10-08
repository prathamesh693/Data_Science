/* Conditional Expressions
1. There are two main ways to use a CASE statement, either a general CASE
or a CASE expression
2.CASE and CASE expression give same output

General SYNTAX::
CASE 
	WHEN condition THEN result
	WHEN condition1 THEN result1
ELSE other_result
END
ex.1
SELECT a,
CASE 
WHEN a = 1 THEN 'one'
WHEN a = 2 THEN 'two'
ELSE 'other'
END
FROM test

CASE expression SYNTAX::
CASE expression
	WHEN value1 THEN 'result1'
	WHEN value2 THEN 'result2'
	ELSE 'some_other_result'
END
# case expression syntax first evaluates an expression then compares the result
with each value in the WHEN clauses sequentially
*/

SELECT * FROM customer
-- ex.1
SELECT customer_id,
CASE
	WHEN (customer_id<=100) THEN 'Premium'
	WHEN (customer_id BETWEEN 100 AND 200) THEN 'Plus'
	ELSE 'Normal'
END
FROM customer
-- ex.2
-- Change column name
SELECT customer_id,
CASE
	WHEN (customer_id<=100) THEN 'Premium'
	WHEN (customer_id BETWEEN 100 AND 200) THEN 'Plus'
	ELSE 'Normal'
END AS customer_class
FROM customer
-- ex.3
SELECT customer_id,
CASE customer_id
	WHEN 2 THEN 'Winner'
	WHEN 5 THEN 'Second Place'
	ELSE 'Normal'
END AS raffle_results
FROM customer

SELECT * FROM film
-- ex.1
SELECT
CASE rental_rate
	WHEN 0.99 THEN 1
	WHEN 2.99 THEN 3
	WHEN 4.99 THEN 5
ELSE 0
END	
FROM film
-- ex.2
SELECT
SUM(CASE rental_rate
	WHEN 0.99 THEN 1
	WHEN 2.99 THEN 3
	WHEN 4.99 THEN 5
    ELSE 0
END) AS number_of_bargains
FROM film

