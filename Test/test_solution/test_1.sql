/*
1st question
*/
CREATE TABLE countries(country_id SERIAL NOT NULL PRIMARY KEY, country_name Varchar(22) NOT NULL, region_id INT NOT NULL);

/*2nd question
*/
CREATE TABLE sales(sale_id INT NOT NULL PRIMARY KEY,product_id INT NOT NULL, quantity_so_id INT NOT NULL, sale_date DATE NOT NULL, total_price FLOAT NULL)
CREATE TABLE products(product_id INT NOT NULL PRIMARY KEY, product_name VARCHAR(22) NOT NULL,category VARCHAR(22) NOT NULL,unit_price FLOAT NULL)

INSERT INTO sales Values(24,125,50,'12-8-2000',2500.125)
INSERT INTO sales Values(29,128,40,'11-8-2001',2800.598)
INSERT INTO sales Values(21,195,90,'12-9-2001',2100.357)
	
INSERT INTO products(product_id,product_name,category,unit_price) Values(125,'transistor','Electronics',150.156)
INSERT INTO products(product_id,product_name,category,unit_price) Values(153,'Resistor','Electronics',160.25668)
INSERT INTO products(product_id,product_name,category,unit_price) Values(167,'Motor','mechanics',250.25894)

/*
3rd question
*/
SELECT total_price as total_price_of_sales from sales
/*
4th question
*/
SELECT SUM(total_price) as totla_revenue from sales
inner join sales.product_id = products.product_id
where category="Electronics"

/*
5th question
*/
Select product_name,category from products order by category;


