/*
california sales text laws have changed and we need to alert our customer to this
through email 
Q. what are the emails of the customer live in california
*/
SELECT district, email FROM address
INNER JOIN customer
ON address.address_id = customer.address_id
WHERE district='California'

/*
a customer walks in and is a huge fan of the actor "Nick Wahlberg" and wants to know 
which movies he is in.
Q. get a list of all the movies "Nick Wahlberg" has been in.
*/
SELECT title,first_name, last_name FROM actor
INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id
INNER JOIN film
ON film.film_id = film_actor.film_id
WHERE first_name ='Nick' and last_name='Wahlberg'

-- Creating Database and Tables
/*


*/

/*
SERIAL it will create a sequence object and set the next value generated by 
the sequence as the default value for the column
*/
CREATE TABLE players(
	player_id SERIAL PRIMARY KEY,
	age SMALLINT NOT NULL
);


