-- TIME ZONE 
CREATE TABLE timezones(
	ts TIMESTAMP WITHOUT TIME ZONE,
	tz TIMESTAMP WITH TIME ZONE
);

SELECT * FROM timezones

INSERT INTO timezones VALUES(
	TIMESTAMP WITHOUT TIME ZONE '2023-03-07 10:50',
	TIMESTAMP WITH TIME ZONE '2023-03-07 10:50'
)

SELECT now()::date;
SELECT CURRENT_DATE
-- to take a date in formate we want 
SELECT TO_CHAR (CURRENT_DATE,'dd/mm/yy')
-- TO CALCULATE DAY'S
SELECT TO_CHAR (CURRENT_DATE,'DDD')
-- TO calculate week's
SELECT TO_CHAR (CURRENT_DATE,'WW')
-- to calculate month's
SELECT TO_CHAR (CURRENT_DATE,'mm')
-- calculate age
SELECT age (date'1800-01-01')
-- calculate age between date's
SELECT age(date'1992/11/12',date'1800/01/01')
-- Extract day,Month,Year from date's
SELECT EXTRACT (DAY FROM date'1992/11/13') AS DAY
SELECT EXTRACT (MONTH FROM date'1992/11/13') AS MONTH
SELECT EXTRACT (YEAR FROM date'1992/11/13') AS YEAR
-- 
SELECT DATE_TRUNC('year',date'1992/11/13')

SELECT age(birth_date),* FROM employees
WHERE(
	EXTRACT (YEAR FROM age(birth_date))
	)>60

SELECT count(emp_no) FROM employees
WHERE(
	EXTRACT (MONTH FROM hire_date)=2
);

SELECT count(emp_no) FROM employees
WHERE(
	EXTRACT (MONTH FROM hire_date)=11
);

SELECT MAX(age(birth_date)) FROM employees;

-- Remove Duplicates from the table
SELECT MAX(salary) FROM salaries;
/* Give an error
SELECT * , 
	MAX(salary) 
	FROM salaries;
*/
--ex.1
SELECT * , 
	MAX(salary) OVER()
	FROM salaries
--ex.2
SELECT * , 
	MAX(salary) OVER()
	FROM salaries
LIMIT 100;
--ex.3
SELECT * , 
	MAX(salary) OVER()
	FROM salaries
WHERE salary<70000
-- to apply partition in the window
--ex.1
SELECT * , 
	AVG(salary) OVER()
FROM salaries
--ex.2
SELECT * ,
	d.dept_name,
	AVG(salary) OVER()
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no)
-- department wise avg salary
--ex.1
SELECT * ,
	d.dept_name,
	AVG(salary) OVER()
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no)
WHERE dept_name = 'Production'; -- give only one department
--ex.2
-- partition a department
SELECT * ,
	d.dept_name,
	AVG(salary) OVER(PARTITION BY d.dept_name)
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no) -- give two dept_name column 
--ex.3
SELECT * ,
	AVG(salary) OVER(PARTITION BY d.dept_name)
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no) -- give only one dept_name column 

/* Window function create a new column based on functions performed on a subset or 
'WINDOW' of the data.
# interview 
*/







