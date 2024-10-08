/*DELETE
1. To delete any rows from the table
syntax::
DELETE FROM table 
WHERE rows_id = 1
2.We can delete rows based on their presence in other tables
syntax::
DELETE FROM tableA
USING tableB
WHERE tableA.id = tableB.id
*/

INSERT INTO job(job_name)
VALUES ('Cowboy')
SELECT * FROM job

DELETE FROM job
WHERE job_id = 4
RETURNING job_id, job_name

/* ALTER 
allows for changes to an existing table structure such as:
adding,dropping changing data types, set default values, Add check constraints  and 
Rename table

syntax:: 
ALTER TABLE table_name action 
*/
CREATE TABLE information(
	info_id SERIAL PRIMARY KEY,
	title VARCHAR(500) NOT NULL,
	person VARCHAR(50) NOT NULL UNIQUE
)
SELECT * FROM information

INSERT INTO information(title,person)
VALUES ('name','ritesh')
-- we can't give any null value if there is not null type 

ALTER TABLE information
RENAME TO new_info

ALTER TABLE new_info
RENAME COLUMN person TO people
	
UPDATE new_info
SET title = 'find me'

INSERT INTO new_info(title)
VALUES ('name')

ALTER TABLE new_info
ALTER COLUMN people DROP NOT NULL

SELECT * FROM new_info
/* DROP 
1.ALLOWS FOR THE COMPLETE REMOVAL OF A COLUMN IN A TABLE
2.REMOVAL OF ALL INDEXES AND CONTRAINTS INVOLVING COLUMN 

SYNTAX::
ALTER TABLE table_name
DROP COLUMN col_name 

# to remove all dependancy
ALTER TABLE table_name
DROP COLUMN col_name CASCADE

# to check existence to avoid error
ALTER TABLE table_name
DROP COLUMN IF EXIST col_name 

# multiple column drop 
ALTER TABLE table_name
DROP COLUMN col_name1,
DROP COLUMN col_name2 
*/
SELECT * FROM new_info

ALTER TABLE new_info 
DROP COLUMN people

ALTER TABLE new_info 
DROP COLUMN IF EXISTS people
-- GIVE only notice that the column are not exist 
/*CHECK
1. allows us to create more customized constraints that adhere to a certain condition
2. such as making sure all inserted integer value fall below a certain threshold
syntax::
CREATE TABLE example(ex_id SERIAL PRIMARY KEY,
age SMALLINT 
)
*/

CREATE TABLE employee(emp_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthdate DATE CHECK (birthdate>'1900-01-01'),
	hire_date DATE CHECK (hire_date>birthdate),
	salary INTEGER CHECK (salary>0)
);

SELECT * FROM employee
/* give an error because of check constraint
INSERT INTO employee(first_name,last_name,birthdate,hire_date,salary)
VALUES ('Jose','Postilla','1899-11-03','2010-01-01',50000)*/
	
INSERT INTO employee(first_name,last_name,birthdate,hire_date,salary)
VALUES ('Jose','Postilla','1999-11-03','2010-01-01',50000)

INSERT INTO employee(first_name,last_name,birthdate,hire_date,salary)
VALUES ('samay','smith','1990-11-03','2010-01-01',70000)






