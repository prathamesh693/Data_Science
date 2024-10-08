CREATE TABLE product(
	log_id SERIAL PRIMARY KEY NOT NULL,
	machine_id INTEGER NOT NULL,
	production_date DATE NOT NULL,
	production_shift VARCHAR(50) NOT NULL,
	products_produced INTEGER NOT NULL,
	defects INTEGER NULL,
	runtime FLOAT NULL
);

INSERT INTO product( machine_id,production_date, production_shift,
	products_produced, defects,runtime	)
VALUES ((1, '2024-06-01', 'Morning', 500, 5, 8.0), (1, '2024-06-01', 'Evening', 450, 3, 7.5),
	(2, '2024-06-01', 'Morning', 480, 2, 7.8), (2, '2024-06-01', 'Evening', 470, 4, 8.1),
	(3, '2024-06-01', 'Morning', 510, 6, 8.2), (3, '2024-06-01', 'Evening', 520, 1, 7.9),
	(1, '2024-06-02', 'Morning', 490, 3, 8.0), (1, '2024-06-02', 'Evening', 460, 2, 7.6),
	(2, '2024-06-02', 'Morning', 475, 1, 7.9), (2, '2024-06-02', 'Evening', 465, 5, 8.3),
	(3, '2024-06-02', 'Morning', 505, 4, 8.0), (3, '2024-06-02', 'Evening', 515, 3, 8.2)
	);

SELECT * FROM product

CREATE TABLE institute_track(
	grade_id SERIAL PRIMARY KEY UNIQUE,
	student_id INTEGER NOT NULL,
	course_id INTEGER NOT NULL,
	grade FLOAT NOT NULL,
	grade_date DATE NOT NULL
)

INSERT INTO institute_track(
	student_id, course_id, grade,grade_date
)
VALUES ((1, 101, 85.5, '2024-01-15'), 
	(1, 102, 78.0, '2024-02-20'), 
	(2, 101, 92.0, '2024-01-15'), 
	(2, 103, 88.5, '2024-03-10'),
	(3, 102, 74.0, '2024-02-20'),
	(3, 103, 81.5, '2024-03-10'),
	(4, 101, 67.0, '2024-01-15'), 
	(4, 104, 90.0, '2024-04-05'),
	(5, 102, 85.0, '2024-02-20'),
	(5, 104, 87.0, '2024-04-05')
	);
SELECT * FROM institute_track

CREATE TABLE customer_address(
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(250) NOT NULL,
	phone_number VARCHAR(15),
	address VARCHAR(250) NOT NULL,
	city VARCHAR (50) NOT NULL,
	state VARCHAR(50) NOT NULL,
	zip_code INTEGER NOT NULL,
	plan_id INTEGER NOT NULL,
	last_call_date DATE NOT NULL
);

INSERT INTO customer_address(
	first_name, last_name, email,phone_number,address,city, state, zip_code,plan_id,last_call_date
)
VALUES (('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St', 'Springfield', 'IL', '62701', 1, '2024-06-01'),
	('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St', 'Springfield', 'IL', '62701', 2, '2024-05-15'), 
	('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567', '789 Pine St', 'Shelbyville', 'IL', '62565', 3, '2024-04-20'),
	('Bob', 'Brown', 'bob.brown@example.com', '444-555-6666', '101 Maple St', 'Capital City', 'IL', '62702', 1, '2024-06-10'),
	('Charlie', 'Davis', 'charlie.davis@example.com', '333-444-5555', '202 Cedar St', 'Springfield', 'IL', '62701', 2, '2024-03-30'),
	('Diana', 'Evans', 'diana.evans@example.com', '222-333-4444', '303 Birch St', 'Shelbyville', 'IL', '62565', 3, '2024-06-20'),
	('Ethan', 'Foster', 'ethan.foster@example.com', '111-222-3333', '404 Spruce St', 'Capital City', 'IL', '62702', 1, '2024-02-14'), 
	('Fiona', 'Garcia', 'fiona.garcia@example.com', '999-888-7777', '505 Ash St', 'Springfield', 'IL', '62701', 2, '2024-05-05'),
	('George', 'Harris', 'george.harris@example.com', '888-777-6666', '606 Walnut St', 'Shelbyville', 'IL', '62565', 3, '2024-01-25'), 
	('Hannah', 'Irvine', 'hannah.irvine@example.com', '777-666-5555', '707 Hickory St', 'Capital City', 'IL', '62702', 1, '2024-06-22')
	);
SELECT * FROM customer_address

CREATE TABLE inventory(
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(50) NOT NULL,
	category VARCHAR (50) NOT NULL,
	quantity INTEGER NOT NULL,
	price FLOAT NOT NULL,
	supplier VARCHAR(50) NOT NULL,
	last_restock_date DATE NOT NULL
);

INSERT INTO inventory(
	product_name, category, quantity,price, supplier,last_restock_date
)
VALUES ('Laptop', 'Electronics', 50, 799.99, 'TechSupplier Inc.', '2024-06-01'), ('Smartphone', 'Electronics', 150, 499.99, 'MobileDistributors Ltd.', '2024-05-25'), ('Desk Chair', 'Furniture', 80, 89.99, 'OfficeSupplies Co.', '2024-05-15'), ('Notebook', 'Stationery', 200, 2.99, 'PaperGoods Inc.', '2024-06-10'), ('Water Bottle', 'Accessories', 120, 9.99, 'Lifestyle Products', '2024-06-05'), ('Headphones', 'Electronics', 70, 149.99, 'TechSupplier Inc.', '2024-06-08'), ('Desk Lamp', 'Furniture', 60, 29.99, 'OfficeSupplies Co.', '2024-05-20'), ('Backpack', 'Accessories', 90, 49.99, 'TravelGear Ltd.', '2024-06-12'), ('Pen', 'Stationery', 300, 1.49, 'PaperGoods Inc.', '2024-06-03'), ('Monitor', 'Electronics', 40, 199.99, 'TechSupplier Inc.', '2024-06-15'));

SELECT * FROM inventory

CREATE TABLE patient_records(
	patient_id SERIAL PRIMARY KEY NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	date_of_birth DATE NOT NULL,
	gender VARCHAR(50) NOT NULL,
	phone_number VARCHAR(15),
	email VARCHAR(250) NOT NULL,
	address VARCHAR(250) NOT NULL,
	city VARCHAR (50) NOT NULL,
	state VARCHAR(50) NOT NULL,
	zip_code INTEGER NOT NULL,
	medical_history VARCHAR(50) NULL,
	last_visit_date DATE NOT NULL
)

INSERT INTO patient_records(
	first_name,last_name,date_of_birth,gender,phone_number,email,address,city,state,zip_code,medical_history,last_visit_date
)
VALUES (('John', 'Doe', '1980-01-15', 'Male', '123-456-7890', 'john.doe@example.com', '123 Elm St', 'Springfield', 'IL', '62701', 'Hypertension', '2024-06-01'), 
	('Jane', 'Smith', '1990-02-20', 'Female', '987-654-3210', 'jane.smith@example.com', '456 Oak St', 'Springfield', 'IL', '62701', 'Diabetes', '2024-05-25'), 
	('Alice', 'Johnson', '1975-03-30', 'Female', '555-123-4567', 'alice.johnson@example.com', '789 Pine St', 'Shelbyville', 'IL', '62565', 'Asthma', '2024-06-10'), 
	('Bob', 'Brown', '1965-04-10', 'Male', '444-555-6666', 'bob.brown@example.com', '101 Maple St', 'Capital City', 'IL', '62702', 'High Cholesterol', '2024-05-15'), 
	('Charlie', 'Davis', '1985-05-20', 'Male', '333-444-5555', 'charlie.davis@example.com', '202 Cedar St', 'Springfield', 'IL', '62701', 'Allergies', '2024-06-05'), 
	('Diana', 'Evans', '2000-06-25', 'Female', '222-333-4444', 'diana.evans@example.com', '303 Birch St', 'Shelbyville', 'IL', '62565', 'Migraine', '2024-06-20'), 
	('Ethan', 'Foster', '1970-07-15', 'Male', '111-222-3333', 'ethan.foster@example.com', '404 Spruce St', 'Capital City', 'IL', '62702', 'Arthritis', '2024-06-12'), 
	('Fiona', 'Garcia', '1995-08-10', 'Female', '999-888-7777', 'fiona.garcia@example.com', '505 Ash St', 'Springfield', 'IL', '62701', 'Depression', '2024-05-30'), 
	('George', 'Harris', '1988-09-05', 'Male', '888-777-6666', 'george.harris@example.com', '606 Walnut St', 'Shelbyville', 'IL', '62565', 'Hypertension', '2024-04-25'), 
	('Hannah', 'Irvine', '1992-10-12', 'Female', '777-666-5555', 'hannah.irvine@example.com', '707 Hickory St', 'Capital City', 'IL', '62702', 'Diabetes', '2024-06-22')
	);

SELECT * FROM patient_records

CREATE TABLE financial_budget(
	transaction_id SERIAL PRIMARY KEY NOT NULL,
	account_id INTEGER NOT NULL,
	transaction_date TIMESTAMP NOT NULL,
	transaction_amount FLOAT NOT NULL,
	transaction_type VARCHAR(50) NOT NULL,
	merchant VARCHAR(50) NOT NULL,
	location VARCHAR(50) NOT NULL,
	status VARCHAR(50) NOT NULL
)

INSERT INTO financial_budget(
	transaction_id,account_id,transaction_date,transaction_amount,transaction_type,merchant,location,status
)
VALUES ((1, '2024-06-01 10:00:00', 1000.00, 'Credit', 'Amazon', 'Online', 'Completed'), 
	(1, '2024-06-01 12:30:00', 500.00, 'Debit', 'Walmart', 'Springfield', 'Completed'), 
	(2, '2024-06-02 09:45:00', 15000.00, 'Credit', 'Apple Store', 'Chicago', 'Pending'), 
	(2, '2024-06-02 11:00:00', 200.00, 'Debit', 'Starbucks', 'Chicago', 'Completed'), 
	(3, '2024-06-03 14:15:00', 250.00, 'Debit', 'Target', 'Springfield', 'Completed'), 
	(3, '2024-06-03 16:20:00', 30000.00, 'Credit', 'Tesla', 'San Francisco', 'Pending'), 
	(4, '2024-06-04 08:30:00', 120.00, 'Debit', 'McDonalds', 'Springfield', 'Completed'), 
	(4, '2024-06-04 10:50:00', 6000.00, 'Credit', 'Best Buy', 'Chicago', 'Pending'), 
	(5, '2024-06-05 15:10:00', 70.00, 'Debit', 'CVS Pharmacy', 'Springfield', 'Completed'), 
	(5, '2024-06-05 17:00:00', 22000.00, 'Credit', 'Louis Vuitton', 'New York', 'Pending')
	);


