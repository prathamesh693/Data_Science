# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:35:55 2024

@author: ratho
"""
import psycopg2 as pg2

# creating a connection with pgAdmin SQL
# password is we already set to the pgAdmin
conn = pg2.connect(database='dvdrental',user='postgres',password ='root1')

# establish connection and start cursor to be ready to query
cur = conn.cursor()

# pass in a postgresSQL query as a string 
cur.execute('SELECT * FROM payment')

# return a tuple of the first row as python objects
cur.fetchone()

# to shows 10 rows of the database
cur.fetchmany(10)

# to shows all rows of the database
cur.fetchall()

# to assing the value to variable
data = cur.fetchall()

conn.close()
